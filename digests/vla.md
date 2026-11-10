# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-11-10 03:52 UTC

**Papers shown:** 49 (relevance ≥ 2, last 7 days)

[Dashboard](../docs/index.html) · [What's new](latest.md) · [Back to Home](../README.md)

---

### [Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation](https://arxiv.org/abs/2611.08577)

**Authors:** Meituan Robotics Team, Caicheng Wang, Chen Zhao, Chengpeng Jin, Duo Xu et al. (38 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08577) | [PDF](https://arxiv.org/pdf/2611.08577) | [Project Page](https://meituan-robotics.github.io/Meituan-Robotics-0/) | [Code](https://github.com/Meituan-Robotics/Meituan-Robotics-0)

<details>
<summary>Abstract</summary>

We present Meituan-Robotics-0 (MR0), a vision-language-action foundation model and embodied-agent system for stationary-base desktop manipulation. MR0 combines 147 million vision-language samples with 15,060 hours of curated robot trajectories spanning 12 embodiments. A three-stage training recipe aligns multimodal representations with robot behavior through discrete action-token pre-training, transfers these priors to continuous cross-embodiment control through flow-matching mid-training, and adapts the policy through real-world post-training. We introduce Rollback, which pairs replaced polic...

</details>

<details>
<summary>Share</summary>

```
Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation

We present Meituan-Robotics-0 (MR0), a vision-language-action foundation model and embodied-agent system for stationary-base desktop manipulation.

arXiv: https://arxiv.org/abs/2611.08577
Project page: https://meituan-robotics.github.io/Meituan-Robotics-0/
Code: https://github.com/Meituan-Robotics/Meituan-Robotics-0

#VLA #robotics
```

</details>

---

### [Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models](https://arxiv.org/abs/2611.10443)

**Authors:** Jungin Park, Chaoran Zhu, Changjae Oh, Kwanghoon Sohn

**Published:** 2026-11-07 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.10443) | [PDF](https://arxiv.org/pdf/2611.10443) | [Code](https://github.com/park-jungin/spark-vla)

<details>
<summary>Abstract</summary>

Understanding three-dimensional physical structure has become essential for vision-language-action models (VLAs). However, existing approaches either rely on explicit geometric inputs at inference time or adopt a single visual pathway, potentially compromising the visual-semantic knowledge inherited from pre-trained models. We present SPARK-VLA, Spatial Representation distillation and Knowledge routing for VLAs, a preserve-specialize-route framework for spatially adapting VLAs without requiring external 3D inputs or experts at inference. SPARK-VLA consists of two key components: (1) spatial re...

</details>

<details>
<summary>Share</summary>

```
Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models

Understanding three-dimensional physical structure has become essential for vision-language-action models (VLAs).

arXiv: https://arxiv.org/abs/2611.10443
Code: https://github.com/park-jungin/spark-vla

#VLA #robotics
```

</details>

---

### [VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models](https://arxiv.org/abs/2611.08698)

**Authors:** Luca Macesanu, Tianluo Zhang, Aditya Patil, Archit Sharma, Kevin Angers et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08698) | [PDF](https://arxiv.org/pdf/2611.08698) | [Project Page](https://ai4ce.github.io/VICTR/)

<details>
<summary>Abstract</summary>

Recent advances in robot foundation models have highlighted the potential of in-context learning (ICL) for adapting robot behavior from demonstrations without further fine-tuning. Previous work has used retrieval-based post-training to equip pretrained vision-language-action (VLA) models with the capability for ICL by teaching them to condition action predictions on retrieved visually-relevant demonstration chunks. However, the effectiveness of retrieval hinges on selecting context relevant to the current execution stage, which visual similarity alone may not capture. We introduce VICTR, a fra...

</details>

<details>
<summary>Share</summary>

```
VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models

Recent advances in robot foundation models have highlighted the potential of in-context learning (ICL) for adapting robot behavior from demonstrations without further fine-tuning.

arXiv: https://arxiv.org/abs/2611.08698
Project page: https://ai4ce.github.io/VICTR/

#VLA #robotics
```

</details>

---

### [Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing](https://arxiv.org/abs/2611.08425)

**Authors:** Michal P. Podolinsky, Yunhao Yang, Daniel Little, Hong Lu, Rohan Siva et al. (9 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08425) | [PDF](https://arxiv.org/pdf/2611.08425) | [Project Page](https://vla-tug.github.io)

<details>
<summary>Abstract</summary>

Vision-Language-Action models (VLAs) enable general-purpose embodied intelligence, but their performance is brittle under distribution shift, where unanticipated failures can damage equipment or endanger people. Deploying VLAs in real-world systems therefore requires a runtime monitor that is timely, calibrated, and informative while being efficient enough to run on the edge. Existing methods fail to fulfill these requirements. We present VLA-Tug, a lightweight probe over the latent layers of a VLA backbone that improves early failure detection and bounds the missed-detection and false-alarm r...

</details>

<details>
<summary>Share</summary>

```
Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing

Vision-Language-Action models (VLAs) enable general-purpose embodied intelligence, but their performance is brittle under distribution shift, where unanticipated failures can damage equipment or endanger people.

arXiv: https://arxiv.org/abs/2611.08425
Project page: https://vla-tug.github.io

#VLA #robotics
```

</details>

---

### [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](https://arxiv.org/abs/2611.08373)

**Authors:** Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang et al. (10 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08373) | [PDF](https://arxiv.org/pdf/2611.08373) | [Project Page](https://SLA.github.io/) | [Code](https://github.com/OpenHelix-Team/Spatial-Forcing)

<details>
<summary>Abstract</summary>

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience. We present SLA, a Spatial-Language-Action Model that scales implicit spatial alignment to continual pre-training and maintains it durin...

</details>

<details>
<summary>Share</summary>

```
SLA: Scaling Spatial-Language-Action Model via Continual Pre-training

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space.

arXiv: https://arxiv.org/abs/2611.08373
Project page: https://SLA.github.io/
Code: https://github.com/OpenHelix-Team/Spatial-Forcing

#VLA #robotics
```

</details>

---

### [From Pixels to Actions -- Towards Native Vision-Language-Action Policies](https://arxiv.org/abs/2611.06918)

**Authors:** Weichen Fan, Haiwen Diao, Penghao Wu, Siyuan Hu, Ziqi Huang et al. (17 authors)

**Published:** 2026-11-04 (updated 2026-11-06) | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.06918) | [PDF](https://arxiv.org/pdf/2611.06918) | [Code](https://github.com/EvolvingLMMs-Lab/NEO)

<details>
<summary>Abstract</summary>

Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation? We introduce NEO-VLA, a structurally encoder-free vision-language-action framework. Images are tokenized by lightweight patch c...

</details>

<details>
<summary>Share</summary>

```
From Pixels to Actions -- Towards Native Vision-Language-Action Policies

Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards.

arXiv: https://arxiv.org/abs/2611.06918
Code: https://github.com/EvolvingLMMs-Lab/NEO

#VLA #robotics
```

</details>

---

### [On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892)

**Authors:** Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi et al. (13 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.09892) | [PDF](https://arxiv.org/pdf/2611.09892) | [Project Page](https://apple-aiml-research.github.io/ml-amp/)

<details>
<summary>Abstract</summary>

Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged across single-arm, bimanual, and mobile manipulation. AMP1 achieves state-of-the-art results on the...

</details>

<details>
<summary>Share</summary>

```
On Agentic Manipulation Policies

Recent work on robot manipulation has focused on specialist policies trained on demonstrations.

arXiv: https://arxiv.org/abs/2611.09892
Project page: https://apple-aiml-research.github.io/ml-amp/

#VLA #robotics
```

</details>

---

### [DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking](https://arxiv.org/abs/2611.09041)

**Authors:** Shengjun Deng, Yinghan Zhang, Chengrui Wei, Liu Liang, Songyuan Liu et al. (11 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.09041) | [PDF](https://arxiv.org/pdf/2611.09041) | [Code](https://github.com/Dobot-Team/dobot_track)

<details>
<summary>Abstract</summary>

Language-guided embodied person tracking requires a mobile agent to identify a target from a referring description and consistently follow the target under egocentric observations. We present DobotTrack, a target-grounded vision-language-action (VLA) framework that integrates auxiliary grounding supervision with efficient temporal modeling. We systematically investigate five auxiliary tasks---person segmentation, bounding-box grounding, visual-spatial classification (VSC), future DINO feature prediction, and future-frame prediction---and adopt complementary mask and bounding-box supervision to...

</details>

<details>
<summary>Share</summary>

```
DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking

Language-guided embodied person tracking requires a mobile agent to identify a target from a referring description and consistently follow the target under egocentric observations.

arXiv: https://arxiv.org/abs/2611.09041
Code: https://github.com/Dobot-Team/dobot_track

#VLA #robotics
```

</details>

---

### [Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs](https://arxiv.org/abs/2611.04391)

**Authors:** Junhyeong Park, Wook Jung, Taeyoung Kim, Huiwon Jang, Jinwoo Shin

**Published:** 2026-11-03 | **Categories:** cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; project page

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

### [ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2611.08827)

**Authors:** Sungwon Moon, Minji Kim, Hyemin Boo, Daeun Song, Jiyoung Lee

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08827) | [PDF](https://arxiv.org/pdf/2611.08827)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models perform versatile manipulation tasks from language instructions, but their inference cost limits how fast a robot can respond in closed-loop control. Visual token pruning reduces this cost; however, prior methods estimate token redundancy from encoded visual embeddings or attention, only after the visual encoder has processed the entire observation. We propose \ours, a training-free token pruning method that moves the pruning decision ahead of the vision encoder by grounding it in a geometric prior derived from the robot's own action. The action chunk predic...

</details>

<details>
<summary>Share</summary>

```
ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models

Vision-language-action (VLA) models perform versatile manipulation tasks from language instructions, but their inference cost limits how fast a robot can respond in closed-loop control.

arXiv: https://arxiv.org/abs/2611.08827

#VLA #robotics
```

</details>

---

### [Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](https://arxiv.org/abs/2611.07513)

**Authors:** Chengcheng Wang, Wei He, Wenhao Li, Hongguang Li, Kai Han et al. (7 authors)

**Published:** 2026-11-05 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.07513) | [PDF](https://arxiv.org/pdf/2611.07513) | [Code](https://github.com/lose4578/Concertina)

<details>
<summary>Abstract</summary>

Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actions into discrete tokens whose errors bear no stable correspondence to physical displacements, or delegating continuous trajectory generation to a separate action expert whose gradients compete with or are blocked from updating the VLM backbone. We argue that manipulation and cognition should instead be embodied in the same model, shifting from a decoupled VLA to an Embodied Vision-Language Model (eVLM). We introduce C...

</details>

<details>
<summary>Share</summary>

```
Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model

Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actions into discrete tokens whose errors b...

arXiv: https://arxiv.org/abs/2611.07513
Code: https://github.com/lose4578/Concertina

#VLA #robotics
```

</details>

---

### [La-JEPA: Compact Robot Policies with Latent World Modeling](https://arxiv.org/abs/2611.08156)

**Authors:** Mateo Clémente, George Z. Xue, Amin Abyaneh, Liheng Ma, Rui Heng Yang et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08156) | [PDF](https://arxiv.org/pdf/2611.08156) | [Code](https://github.com/mt-clemente/lajepa)

<details>
<summary>Abstract</summary>

World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. It remains unclear how much these generation-oriented choices affect control. In this work, we introduce Latent Action JEPA (La-JEPA), a compact world-action model whose policy transformer is trained from scratch in the feature space of a pretrained V-JEPA 2.1 encoder. Following Fast-WAM, La-JEPA learns to predict future features jointly with acti...

</details>

<details>
<summary>Share</summary>

```
La-JEPA: Compact Robot Policies with Latent World Modeling

World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed fo...

arXiv: https://arxiv.org/abs/2611.08156
Code: https://github.com/mt-clemente/lajepa

#VLA #robotics
```

</details>

---

### [$A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation](https://arxiv.org/abs/2611.06447)

**Authors:** Shengzhe Zhang, Qi Zhang, Dazhong Shen, Chao Wang, Shaopeng Zhai et al. (6 authors)

**Published:** 2026-11-04 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.06447) | [PDF](https://arxiv.org/pdf/2611.06447)

<details>
<summary>Abstract</summary>

Vision-Language-Action Models (VLAs) enable robots to perform manipulation tasks by leveraging Vision-Language Models (VLMs) to process visual observations and language instructions. However, the action prediction objective itself lacks fine-grained task-specific perceptual supervision, making it prone to relying on task-irrelevant visual shortcuts, leading attention away from target objects and key interaction areas, thereby limiting its operational performance and generalization ability. To address this, we propose Automatic Perception-Guided Attention Alignment for Robot Manipulation ($A^3$...

</details>

<details>
<summary>Share</summary>

```
$A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation

Vision-Language-Action Models (VLAs) enable robots to perform manipulation tasks by leveraging Vision-Language Models (VLMs) to process visual observations and language instructions.

arXiv: https://arxiv.org/abs/2611.06447

#VLA #robotics
```

</details>

---

### [Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning](https://arxiv.org/abs/2611.05667)

**Authors:** Xinkai Jiang, Jing Jiang, Hongyi Zhou, Pankhuri Vanjani, Ahmad Baki et al. (10 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05667) | [PDF](https://arxiv.org/pdf/2611.05667) | [Project Page](https://intuitive-robots.github.io/PHIL-page/)

<details>
<summary>Abstract</summary>

This paper presents Proactive Human-in-the-Loop (PHIL), a framework for proactive policy correction and preference-based post-training. PHIL enables operators to preview policy-predicted future motion and intervene before anticipated undesirable actions. During takeover, PHIL continues querying the policy and displaying its predicted trajectories in the physical workspace through an extended reality (XR) interface. PHIL pairs rejected policy predictions with corrective action chunks subsequently executed from the same physical state over the same horizon, and preference-based post-training enc...

</details>

<details>
<summary>Share</summary>

```
Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning

This paper presents Proactive Human-in-the-Loop (PHIL), a framework for proactive policy correction and preference-based post-training.

arXiv: https://arxiv.org/abs/2611.05667
Project page: https://intuitive-robots.github.io/PHIL-page/

#VLA #robotics
```

</details>

---

### [PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](https://arxiv.org/abs/2611.05372)

**Authors:** Yuhan Liu, Xinqi Liu, Zixuan Dong, Keith W. Ross, Shenji Wan

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

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

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; project page

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; code repo

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

### [HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes](https://arxiv.org/abs/2611.09355)

**Authors:** Boran Zhao, Yanbin Hu, Jun Ye, Zhenxian Hu, Yuxin Zhai et al. (7 authors)

**Published:** 2026-11-06 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.09355) | [PDF](https://arxiv.org/pdf/2611.09355)

<details>
<summary>Abstract</summary>

Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes. However, existing VLA memory mechanisms suffer from memory noise, particularly in complex 3D scenes, as stored episodic memories contain extensive redundant details about scene layouts, object configurations, and robot-specific states, which obscure generalizable manipulation principles and hinder cross-task transfer. To address this challenge, we first introduce a hippocampus-inspired memory consolidation mechanism that synthesizes ex...

</details>

<details>
<summary>Share</summary>

```
HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes

Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes.

arXiv: https://arxiv.org/abs/2611.09355

#VLA #robotics
```

</details>

---

### [MotoVerse: A Benchmark for Predictive Perception of Motorized Two-Wheelers in Dense Unstructured Traffic](https://arxiv.org/abs/2611.06007)

**Authors:** Varun A. Paturkar, Shankar Gangisetty, C. V. Jawahar

**Published:** 2026-11-04 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; code repo

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.06007) | [PDF](https://arxiv.org/pdf/2611.06007) | [Code](https://github.com/VarunIIITH/MotoVerse)

<details>
<summary>Abstract</summary>

Motorized Two-Wheelers (MTWs) dominate personal transport across much of the Global South, yet remain largely overlooked in predictive perception research for autonomous driving and ADAS. We introduce MotoVerse, a benchmark for predictive perception from an MTW's ego-centric perspective. MotoVerse comprises 949 maneuver clips collected in dense, unstructured traffic and trajectory annotations for over 31,000 surrounding road agents, including over 16,000 MTWs, enabling two complementary tasks: Ego-Rider Maneuver Anticipation (ERMA) and Traffic Agent Trajectory Prediction (TATP). Each clip is f...

</details>

<details>
<summary>Share</summary>

```
MotoVerse: A Benchmark for Predictive Perception of Motorized Two-Wheelers in Dense Unstructured Traffic

Motorized Two-Wheelers (MTWs) dominate personal transport across much of the Global South, yet remain largely overlooked in predictive perception research for autonomous driving and ADAS.

arXiv: https://arxiv.org/abs/2611.06007
Code: https://github.com/VarunIIITH/MotoVerse

#VLA #robotics
```

</details>

---

### [Zero-Shot VLA Adaptation with Retrieved Guidance](https://arxiv.org/abs/2611.10894)

**Authors:** Subin Kim, Anh-Quan Pham, Dinesh Jayaraman

**Published:** 2026-11-07 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.10894) | [PDF](https://arxiv.org/pdf/2611.10894)

<details>
<summary>Abstract</summary>

Pre-training large parametric "Vision-Language-Action" (VLA) models on large demonstration datasets has recently yielded promising results for general-purpose manipulation. However, these models still struggle under even small domain shifts relative to the training data, such as changes in camera viewpoint, background, object identity, or robot morphology. Motivated by the success of Retrieval-Augmented Generation (RAG) in language models, we pursue retrieval to boost VLA performance. Specifically, we seek to leverage retrieval from domain-mismatched, "in-the-wild" demonstration datasets like...

</details>

<details>
<summary>Share</summary>

```
Zero-Shot VLA Adaptation with Retrieved Guidance

Pre-training large parametric "Vision-Language-Action" (VLA) models on large demonstration datasets has recently yielded promising results for general-purpose manipulation.

arXiv: https://arxiv.org/abs/2611.10894

#VLA #robotics
```

</details>

---

### [DreamVLA: From Generated Human Motions to Humanoid Vision-Language-Action Policies](https://arxiv.org/abs/2611.10872)

**Authors:** Kevin Park, Izat Rasyad, Dvij Kalaria, Shankar Sastry

**Published:** 2026-11-07 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.10872) | [PDF](https://arxiv.org/pdf/2611.10872)

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) policies typically depends on substantial robot demonstration data, making human teleoperation a costly and cumbersome bottleneck, particularly for whole-body humanoid interaction. Reinforcement learning in simulation offers an alternative for scaling this data, but designing task-specific rewards remains challenging. To address this, we propose DreamVLA, which uses generated motion trajectories to guide reinforcement learning (RL) in simulation, converting them into reliable task execution trajectories. These trajectories train VLA models in simulation wi...

</details>

<details>
<summary>Share</summary>

```
DreamVLA: From Generated Human Motions to Humanoid Vision-Language-Action Policies

Training vision-language-action (VLA) policies typically depends on substantial robot demonstration data, making human teleoperation a costly and cumbersome bottleneck, particularly for whole-body humanoid interaction.

arXiv: https://arxiv.org/abs/2611.10872

#VLA #robotics
```

</details>

---

### [SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning](https://arxiv.org/abs/2611.09684)

**Authors:** Jingye Zhang, Choo Sin Wai, Dake Zhong, Zhifang Liu, Yuhong Zhang et al. (11 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.09684) | [PDF](https://arxiv.org/pdf/2611.09684)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have become a promising paradigm for end-to-end robot control, but their effectiveness still depends heavily on large volumes of demonstration data. In manipulation tasks, this dependence is compounded by structured spatiotemporal uncertainty in the action space: multiple nearby actions or trajectories may successfully solve the same task, while semantically equivalent demonstrations often unfold at different speeds. Standard pointwise supervision treats each demonstrated action as an exact target, imposing an unnecessary learning burden under such uncerta...

</details>

<details>
<summary>Share</summary>

```
SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning

Vision-language-action (VLA) policies have become a promising paradigm for end-to-end robot control, but their effectiveness still depends heavily on large volumes of demonstration data.

arXiv: https://arxiv.org/abs/2611.09684

#VLA #robotics
```

</details>

---

### [VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models](https://arxiv.org/abs/2611.08987)

**Authors:** Takayuki Nishio

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.LG, cs.NI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08987) | [PDF](https://arxiv.org/pdf/2611.08987)

<details>
<summary>Abstract</summary>

Large vision-language-action (VLA) models generalize well but are difficult to run in real time on a robot, and small VLAs that run there fail more often. Remote inference over beyond-5G and 6G networks lets a robot use a large VLA on a server, but querying the server for every action chunk limits the number of robots per server. We propose VLA handover: the robot runs a small VLA (S-VLA) and switches to a large VLA (L-VLA) on a server only when the S-VLA is likely to fail. We formulate the switching as minimizing the request cost under a required success probability and, since this problem ca...

</details>

<details>
<summary>Share</summary>

```
VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models

Large vision-language-action (VLA) models generalize well but are difficult to run in real time on a robot, and small VLAs that run there fail more often.

arXiv: https://arxiv.org/abs/2611.08987

#VLA #robotics
```

</details>

---

### [PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation](https://arxiv.org/abs/2611.08917)

**Authors:** Jiachen Tao, Gengyu Zhang, Haoxuan Wang, Bing Liu, Yan Yan

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08917) | [PDF](https://arxiv.org/pdf/2611.08917)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models promise a single language-conditioned policy adaptable to many manipulation behaviors, yet deployment additionally requires skill retention and long-horizon composition: a policy must retain previously acquired skills and reuse them inside composite tasks whose behavior changes across phases. The standard recipe absorbs every new task into one shared update, which provides neither a parameter-level locus for reusable skills nor a mechanism for invoking each skill along the trajectory. We observe that this missing structure is latent rather than absent: per-s...

</details>

<details>
<summary>Share</summary>

```
PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation

Vision-Language-Action (VLA) models promise a single language-conditioned policy adaptable to many manipulation behaviors, yet deployment additionally requires skill retention and long-horizon composition: a policy mu...

arXiv: https://arxiv.org/abs/2611.08917

#VLA #robotics
```

</details>

---

### [Localizing and Editing the Goal Representation of a Vision-Language-Action Model](https://arxiv.org/abs/2611.08895)

**Authors:** Sudhanshu Srivastava, Faisal Aqlan

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08895) | [PDF](https://arxiv.org/pdf/2611.08895)

<details>
<summary>Abstract</summary>

Operators can state safety constraints for robots as prohibitions such as "do not put the bowl on the stove". We study whether OpenVLA follows such prohibitions and where it represents the goal it executes. The 10 tasks of LIBEROGoal share one scene, so we can label the goal that each rollout executes. We combine closed-loop rollouts with activation patching, linear probes, activation steering and runtime monitors. On LIBERO-Goal, negation had no detectable effect on which task OpenVLA executed. The model executed the forbidden task in 79% of negated rollouts and completed 78% of plain tasks....

</details>

<details>
<summary>Share</summary>

```
Localizing and Editing the Goal Representation of a Vision-Language-Action Model

Operators can state safety constraints for robots as prohibitions such as "do not put the bowl on the stove".

arXiv: https://arxiv.org/abs/2611.08895

#VLA #robotics
```

</details>

---

### [OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions](https://arxiv.org/abs/2611.08462)

**Authors:** Arpit Bahety, Skand Peri, Sriniket Ambatipudi, Chen Xu, Haruki Nishimura et al. (7 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08462) | [PDF](https://arxiv.org/pdf/2611.08462)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models can perform a wide range of robotic manipulation tasks, but often fail during deployment. Teaching them to recover from these failures requires substantial corrective data: existing approaches learn to recover from failures by directly associating corrective actions with the observations in which they were demonstrated. For instance, DAgger-like fine-tuning can require tens to hundreds of interactions, yet the resulting policy may still fail to generalize the learned corrections beyond the demonstrated scenarios. We hypothesize that semantics can capture the...

</details>

<details>
<summary>Share</summary>

```
OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions

Vision-Language-Action (VLA) models can perform a wide range of robotic manipulation tasks, but often fail during deployment.

arXiv: https://arxiv.org/abs/2611.08462

#VLA #robotics
```

</details>

---

### [Q-OIL: Optimistic Exploration in Learning from Human Interventions](https://arxiv.org/abs/2611.08576)

**Authors:** Pranav Teegavarapu, Sriyash Poddar, Rico Qi, Cleah Winston, Krisha Khandelwal et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.08576) | [PDF](https://arxiv.org/pdf/2611.08576) | [Project Page](https://weirdlabuw.github.io/qoil)

<details>
<summary>Abstract</summary>

As robots are deployed in the real world, they will inevitably make mistakes. Human interventions provide valuable feedback for improving their behavior, enabling them to adapt online to new scenarios. However, studying human-in-the-loop robot learning is difficult: real-world experiments are slow and expensive, so most algorithm development relies on simulated human models. We show that common human modeling assumptions do not match how real people intervene in practice. Through analyzing intervention data from human participants, we find that humans tend to intervene when agent progress stal...

</details>

<details>
<summary>Share</summary>

```
Q-OIL: Optimistic Exploration in Learning from Human Interventions

As robots are deployed in the real world, they will inevitably make mistakes.

arXiv: https://arxiv.org/abs/2611.08576
Project page: https://weirdlabuw.github.io/qoil

#VLA #robotics
```

</details>

---

### [T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models](https://arxiv.org/abs/2611.08413)

**Authors:** Mohammed Hassan, Zhenyang Chen, Zheng Wang, Zhixin Zhu, Tianlong Chen et al. (8 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.08413) | [PDF](https://arxiv.org/pdf/2611.08413)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models enable end-to-end robot control, but inference is increasingly expensive. Each decision processes hundreds of visual tokens, often across multiple cameras, leading to substantial computation while allowing irrelevant background content to distract action prediction under distribution shift. We argue that these issues stem from two complementary forms of redundancy: many visual tokens are spatially irrelevant, while attention over the remaining tokens is often misallocated. Based on this observation, we propose T3R, a Training-Free Two-Stage Token Refinement...

</details>

<details>
<summary>Share</summary>

```
T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models

Vision-Language-Action (VLA) models enable end-to-end robot control, but inference is increasingly expensive.

arXiv: https://arxiv.org/abs/2611.08413

#VLA #robotics
```

</details>

---

### [AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction](https://arxiv.org/abs/2611.07712)

**Authors:** Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina, Yara Mahmoud, Iana Zhura et al. (7 authors)

**Published:** 2026-11-05 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.07712) | [PDF](https://arxiv.org/pdf/2611.07712)

<details>
<summary>Abstract</summary>

Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent, generate contact-rich motions, and maintain safe physical contact. We present AffectiveVLA, an intent-gated Vision-Language-Action (VLA) pipeline deployed on a Unitree G1 humanoid with dexterous hands. A lightweight RGB-based model recognizes interaction intent from two onboard cameras and converts it into a language prompt for the VLA policy. Low-confidence predictions suppress motion execution, reducing unintended activations. During physical contact, interaction-specific compl...

</details>

<details>
<summary>Share</summary>

```
AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction

Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent, generate contact-rich motions, and maintain safe physical contact.

arXiv: https://arxiv.org/abs/2611.07712

#VLA #robotics
```

</details>

---

### [Where Is VLA Inference Time Spent? Bottlenecks and Optimization Interactions Across GPUs](https://arxiv.org/abs/2611.06710)

**Authors:** Muhammad Danish Waseem, Ahmed Ali-Eldin Hassan

**Published:** 2026-11-04 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.06710) | [PDF](https://arxiv.org/pdf/2611.06710)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models map camera observations and language instructions to robot actions. However, their large backbones and repeated action generation can make inference take longer than the robot's real-time requirements for its next action. To reduce the load of VLA computations, researchers have proposed multiple optimization approaches, including quantization and pruning. These optimizations can be combined with other general optimizations such as better kernel compilation or using CUDA graphs instead of the eager mode. However, most of these optimization results are usually...

</details>

<details>
<summary>Share</summary>

```
Where Is VLA Inference Time Spent? Bottlenecks and Optimization Interactions Across GPUs

Vision-language-action (VLA) models map camera observations and language instructions to robot actions.

arXiv: https://arxiv.org/abs/2611.06710

#VLA #robotics
```

</details>

---

### [Can Astra Solve RoboMME without Breaking the Bank?](https://arxiv.org/abs/2611.06184)

**Authors:** Bingao Chen, Haoquan Fang, C. Karen Liu

**Published:** 2026-11-04 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.06184) | [PDF](https://arxiv.org/pdf/2611.06184) | [Project Page](https://bingaochen.github.io/Astra-on-RoboMME/)

<details>
<summary>Abstract</summary>

Robotic manipulation often requires remembering information that is no longer visible, such as an object's location before occlusion or the order of a demonstrated action sequence. A large vision-language planner can read this history, but calling it before every action chunk is slow and costly. We present a three-tier system for the RoboMME benchmark. GPT-6 Astra (System 2) selects a grounded subtask from stored visual history, a $π_{0.5}$ vision-language-action policy (System 1) executes it, and a fine-tuned Qwen3-VL-4B monitor (System 1.5) checks after each action chunk whether the subtask...

</details>

<details>
<summary>Share</summary>

```
Can Astra Solve RoboMME without Breaking the Bank?

Robotic manipulation often requires remembering information that is no longer visible, such as an object's location before occlusion or the order of a demonstrated action sequence.

arXiv: https://arxiv.org/abs/2611.06184
Project page: https://bingaochen.github.io/Astra-on-RoboMME/

#VLA #robotics
```

</details>

---

### [MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](https://arxiv.org/abs/2611.05567)

**Authors:** Albert Wilcox, Frank Chang, Nhi Nguyen, Aishani Chakraborty, Jeremy A. Collins et al. (9 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.05567) | [PDF](https://arxiv.org/pdf/2611.05567) | [Project Page](https://pairlab.github.io/MESA)

<details>
<summary>Abstract</summary>

Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive. Existing benchmarks are either narrow and saturated, offering little signal on SOTA methods, broadly scoped, providing diversity at the cost of controlled experimentation, or require training on large, messy open-source datasets. We introduce MESA, an evaluation framework designed for precise, reproducible measurement of language-conditioned policy generalization. MESA provides five evaluation suites that isolate in-distribution performance and four distinct axes...

</details>

<details>
<summary>Share</summary>

```
MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics

Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive.

arXiv: https://arxiv.org/abs/2611.05567
Project page: https://pairlab.github.io/MESA

#VLA #robotics
```

</details>

---

### [Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs](https://arxiv.org/abs/2611.05249)

**Authors:** Asher James Hancock, Boyi Li, Yuxiao Chen, Shuhan Tan, Wenhao Ding et al. (9 authors)

**Published:** 2026-11-03 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

### [Future Representation Distillation for Imagination-free World Action Models](https://arxiv.org/abs/2611.04527)

**Authors:** Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye, Yekyung Nah et al. (8 authors)

**Published:** 2026-11-03 (updated 2026-11-04) | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.04527) | [PDF](https://arxiv.org/pdf/2611.04527) | [Project Page](https://harryjo97.github.io/dreamfree/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction. However, iterative video denoising is costly, and inaccurate visual predictions can compromise action prediction. Our key idea is to make this predictive knowledge available through visual representations computed from the current observation, enabling action prediction without generating future videos. We introduce DreamFree, a WAM that repurposes a pretrained video diffusion model as a predictive visual encoder through representation distillation. Th...

</details>

<details>
<summary>Share</summary>

```
Future Representation Distillation for Imagination-free World Action Models

World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction.

arXiv: https://arxiv.org/abs/2611.04527
Project page: https://harryjo97.github.io/dreamfree/

#VLA #robotics
```

</details>

---

### [RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training](https://arxiv.org/abs/2611.04368)

**Authors:** Shresth Grover, Andrey Kolobov, Dhruv Shah

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

**Published:** 2026-11-03 | **Categories:** cs.LG, cs.CR, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits

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

### [ODEAction: From Predicting Chunks to Evolving Actions](https://arxiv.org/abs/2611.09672)

**Authors:** Qishen Wang, Pengxiang Ding, Shifeng Bao, Mingyang Sun, Hengtao Li et al. (17 authors)

**Published:** 2026-11-06 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.09672) | [PDF](https://arxiv.org/pdf/2611.09672)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically generate actions in chunks, organizing continuous robot execution into separately predicted segments and thus introducing potential discontinuities at action-chunk transitions. We propose ODEAction, a chunk-free action generation paradigm that replaces action-chunk prediction with Continuous Action Evolution. Given visual observations, language instructions, and robot proprioceptive information, ODEAction learns an action transition field defined over action space, where a transition vector characterizes the evolution rate of the current action wit...

</details>

<details>
<summary>Share</summary>

```
ODEAction: From Predicting Chunks to Evolving Actions

Vision-language-action (VLA) models typically generate actions in chunks, organizing continuous robot execution into separately predicted segments and thus introducing potential discontinuities at action-chunk transit...

arXiv: https://arxiv.org/abs/2611.09672

#VLA #robotics
```

</details>

---

### [Asynchronous Robot Policies](https://arxiv.org/abs/2611.05155)

**Authors:** Sombit Dey, Luc Van Gool, Danda Pani Paudel

**Published:** 2026-11-03 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

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

### [Look Ahead: Search-Driven Reasoning in Embodied AI](https://arxiv.org/abs/2611.10769)

**Authors:** Ahmed Zeer, Osama Shbib, Muzaffer Kaan Yuce, Himmet Toprak Kesgin, Mehmet Fatih Amasyali

**Published:** 2026-11-07 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.10769) | [PDF](https://arxiv.org/pdf/2611.10769)

<details>
<summary>Abstract</summary>

Search allows a robotic policy to evaluate candidate futures before committing to an action. Motivated by test-time planning for vision-language action (VLA) models, we study selective search over action chunks in PushT using a frozen Action Chunking with Transformers (ACT) policy. Beam search generates perturbed alternatives around the policy prediction and scores them through rollouts from cloned simulator states. Across 50 evaluation episodes, beam search raises task success from 0% to 18% and increases average cumulative reward from 39.44 to 103.2. We introduce One Step Ahead (OSA), a gate...

</details>

<details>
<summary>Share</summary>

```
Look Ahead: Search-Driven Reasoning in Embodied AI

Search allows a robotic policy to evaluate candidate futures before committing to an action.

arXiv: https://arxiv.org/abs/2611.10769

#VLA #robotics
```

</details>

---

### [AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds](https://arxiv.org/abs/2611.04241)

**Authors:** Kailing Li, Ruoxuan Zhang, Zheyuan Zhou, Boyang Chu, Yingshan Lei et al. (8 authors)

**Published:** 2026-11-03 (updated 2026-11-06) | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

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

### [Can LLMs Debug Robots by Editing Their Weights?](https://arxiv.org/abs/2611.09376)

**Authors:** Jusheng Zhang, Keze Wang, Liang Lin

**Published:** 2026-11-06 | **Categories:** cs.RO, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.09376) | [PDF](https://arxiv.org/pdf/2611.09376)

<details>
<summary>Abstract</summary>

A language model can repair a robot policy's lexical instruction grounding by editing just 65 token-embedding rows. We bring weight-space programming to robot foundation policies: GPT-6 Astra reads weights and uses a CPU workspace and budgeted simulator feedback, without gradient updates or new demonstrations. Three independent sessions on $π_{0.5}$ all improve success on 765 held-out paraphrases; the best raises success from 86.3\% to 92.0\% (48 repairs, four regressions; exact paired $p=1.31\times10^{-10}$). Among the 335 instructions containing edited tokens, success rises from 74.3\% to 87...

</details>

<details>
<summary>Share</summary>

```
Can LLMs Debug Robots by Editing Their Weights?

A language model can repair a robot policy's lexical instruction grounding by editing just 65 token-embedding rows.

arXiv: https://arxiv.org/abs/2611.09376

#VLA #robotics
```

</details>

---

### [Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks](https://arxiv.org/abs/2611.07411)

**Authors:** Yuze Lu

**Published:** 2026-11-05 | **Categories:** cs.RO, cs.CV | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.07411) | [PDF](https://arxiv.org/pdf/2611.07411)

<details>
<summary>Abstract</summary>

Robots increasingly run large vision-language-action policies on remote servers, making the camera uplink the bottleneck. Existing video codecs spend bits on content the receiver could predict: the robot's own motion. We introduce the kinematic hypothesis context, a zero-rate conditioning signal that both ends build from joint states, the robot model and the camera calibration. Ego-motion homographies, per-link robot reprojections, an end-effector plane and a background memory warp the previous reconstruction into hypotheses that condition a learned video codec. We prove that history-only and...

</details>

<details>
<summary>Share</summary>

```
Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks

Robots increasingly run large vision-language-action policies on remote servers, making the camera uplink the bottleneck.

arXiv: https://arxiv.org/abs/2611.07411

#VLA #robotics
```

</details>

---

### [Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2611.06475)

**Authors:** Sihang Chen, Chen Ye, Wei Chen, Xiaohan Lei, Zhipeng Tang et al. (11 authors)

**Published:** 2026-11-04 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "VLA" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.06475) | [PDF](https://arxiv.org/pdf/2611.06475)

<details>
<summary>Abstract</summary>

In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable. However, existing benchmarks provide limited evaluation of such memory-dependent decision-making in mobile manipulation. To address this gap, we introduce RoboCasa-Mem, a new benchmark comprising nine mobile manipulation tasks that require agents to use interaction history at key decision points. Specifically, the tasks are grouped into two categories of memory: One is environment memory, which captures sp...

</details>

<details>
<summary>Share</summary>

```
Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation

In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable.

arXiv: https://arxiv.org/abs/2611.06475

#VLA #robotics
```

</details>

---
