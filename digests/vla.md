# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-27 22:22 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Drive My Way: Preference Alignment of Vision-Language-Action Model for Personalized Driving](https://arxiv.org/abs/2603.25740v1)

**Authors:** Zehao Wang, Huaide Jiang, Shuaiwu Dong, Yuping Wang, Hang Qiu et al. (6 authors)

**Published:** 2026-03-26 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.25740v1) | [PDF](https://arxiv.org/pdf/2603.25740v1.pdf) | [Project Page](https://dmw-cvpr.github.io/)

<details>
<summary>Abstract</summary>

Human driving behavior is inherently personal, which is shaped by long-term habits and influenced by short-term intentions. Individuals differ in how they accelerate, brake, merge, yield, and overtake across diverse situations. However, existing end-to-end autonomous driving systems either optimize for generic objectives or rely on fixed driving modes, lacking the ability to adapt to individual preferences or interpret natural language intent. To address this gap, we propose Drive My Way (DMW), ...

</details>

---

### [Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance](https://arxiv.org/abs/2603.25661v1)

**Authors:** Wenxuan Song, Jiayi Chen, Shuai Chen, Jingbo Wang, Pengxiang Ding et al. (11 authors)

**Published:** 2026-03-26 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.25661v1) | [PDF](https://arxiv.org/pdf/2603.25661v1.pdf) | [Project Page](https://chris1220313648.github.io/Fast-dVLA/)

<details>
<summary>Abstract</summary>

This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Some advanced finetuning methods with auxiliary training objectives can improve performance and reduce the number of convergence steps. However, they typically incur significant computational overhead due to the additional losses from auxiliary tasks. To simultaneously achieve the enhanced c...

</details>

---

### [LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation](https://arxiv.org/abs/2603.25481v1)

**Authors:** Motonari Kambara, Koki Seno, Tomoya Kaichi, Yanan Wang, Komei Sugiura

**Published:** 2026-03-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.25481v1) | [PDF](https://arxiv.org/pdf/2603.25481v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

We address language-conditioned robotic manipulation using flow-based trajectory generation, which enables training on human and web videos of object manipulation and requires only minimal embodiment-specific data. This task is challenging, as object trajectory generation from pre-manipulation images and natural language instructions requires appropriate instruction-flow alignment. To tackle this challenge, we propose the flow-based Language Instruction-guided open-Loop ACtion generator (LILAC)....

</details>

---

### [LaMP: Learning Vision-Language-Action Policies with 3D Scene Flow as Latent Motion Prior](https://arxiv.org/abs/2603.25399v1)

**Authors:** Xinkai Wang, Chenyi Wang, Yifu Xu, Mingzhe Ye, Fu-Cheng Zhang et al. (10 authors)

**Published:** 2026-03-26 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.25399v1) | [PDF](https://arxiv.org/pdf/2603.25399v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation. Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly. This implicit learning strategy degrades under unfamiliar spatial dynamics. LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Ex...

</details>

---

### [Vega: Learning to Drive with Natural Language Instructions](https://arxiv.org/abs/2603.25741v1)

**Authors:** Sicheng Zuo, Yuxuan Li, Wenzhao Zheng, Zheng Zhu, Jie Zhou et al. (6 authors)

**Published:** 2026-03-26 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.25741v1) | [PDF](https://arxiv.org/pdf/2603.25741v1.pdf) | [GitHub](https://github.com/zuosc19/Vega)

<details>
<summary>Abstract</summary>

Vision-language-action models have reshaped autonomous driving to incorporate languages into the decision-making process. However, most existing pipelines only utilize the language modality for scene descriptions or reasoning and lack the flexibility to follow diverse user instructions for personalized driving. To address this, we first construct a large-scale driving dataset (InstructScene) containing around 100,000 scenes annotated with diverse driving instructions with the corresponding traje...

</details>

---

### [Unleashing Vision-Language Semantics for Deepfake Video Detection](https://arxiv.org/abs/2603.24454v1)

**Authors:** Jiawen Zhu, Yunqi Miao, Xueyi Zhang, Jiankang Deng, Guansong Pang

**Published:** 2026-03-25 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.24454v1) | [PDF](https://arxiv.org/pdf/2603.24454v1.pdf) | [GitHub](https://github.com/mala-lab/VLAForge)

<details>
<summary>Abstract</summary>

Recent Deepfake Video Detection (DFD) studies have demonstrated that pre-trained Vision-Language Models (VLMs) such as CLIP exhibit strong generalization capabilities in detecting artifacts across different identities. However, existing approaches focus on leveraging visual features only, overlooking their most distinctive strength -- the rich vision-language semantics embedded in the latent space. We propose VLAForge, a novel DFD framework that unleashes the potential of such cross-modal semant...

</details>

---

### [SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation](https://arxiv.org/abs/2603.24060v1)

**Authors:** Zhuoran Li, Zhiyang Li, Kaijun Zhou, Jinyu Gu

**Published:** 2026-03-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.24060v1) | [PDF](https://arxiv.org/pdf/2603.24060v1.pdf) | [Project Page](and) | [GitHub](https://github.com/LZY-1021/SOMA)

<details>
<summary>Abstract</summary>

Despite the promise of Vision-Language-Action (VLA) models as generalist robotic controllers, their robustness against perceptual noise and environmental variations in out-of-distribution (OOD) tasks remains fundamentally limited by the absence of long-term memory, causal failure attribution, and dynamic intervention capability. To address this, we propose SOMA, a Strategic Orchestration and Memory-Augmented System that upgrades frozen VLA policies for robust in-context adaptation without parame...

</details>

---

## Other Recent Papers

### [MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation](https://arxiv.org/abs/2603.25406v1)

**Authors:** Yang Liu, Pengxiang Ding, Tengyue Jiang, Xudong Wang, Wenxuan Song et al. (13 authors)

**Published:** 2026-03-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.25406v1) | [PDF](https://arxiv.org/pdf/2603.25406v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models aim to control robots for manipulation from visual observations and natural-language instructions. However, existing hierarchical and autoregressive paradigms often introduce architectural overhead, suffer from temporal inconsistency and long-horizon error accumulation, and lack a mechanism to capture environment dynamics without extra modules. To this end, we present MMaDA-VLA, a fully native pre-trained large diffusion VLA model that unifies multi-modal unde...

</details>

---

### [ThermoAct:Thermal-Aware Vision-Language-Action Models for Robotic Perception and Decision-Making](https://arxiv.org/abs/2603.25044v1)

**Authors:** Young-Chae Son, Dae-Kwan Ko, Yoon-Ji Choi, Soo-Chul Lim

**Published:** 2026-03-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.25044v1) | [PDF](https://arxiv.org/pdf/2603.25044v1.pdf)

<details>
<summary>Abstract</summary>

In recent human-robot collaboration environments, there is a growing focus on integrating diverse sensor data beyond visual information to enable safer and more intelligent task execution. Although thermal data can be crucial for enhancing robot safety and operational efficiency, its integration has been relatively overlooked in prior research. This paper proposes a novel Vision-Language-Action (VLA) framework that incorporates thermal information for robot task execution. The proposed system le...

</details>

---

### [$π$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation](https://arxiv.org/abs/2603.25038v1)

**Authors:** Johnathan Tucker, Denis Liu, Aiden Swann, Allen Ren, Javier Yu et al. (10 authors)

**Published:** 2026-03-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.25038v1) | [PDF](https://arxiv.org/pdf/2603.25038v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models such as $π_0$ have demonstrated remarkable generalization across diverse fixed-base manipulators. However, transferring these foundation models to aerial platforms remains an open challenge due to the fundamental mismatch between the quasi-static dynamics of fixed-base arms and the underactuated, highly dynamic nature of flight. In this work, we introduce AirVLA, a system that investigates the transferability of manipulation-pretrained VLAs to aerial pick-and-...

</details>

---

### [Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2603.24941v1)

**Authors:** Peiju Liu, Jinming Liu, Xipeng Qiu, Xuanjing Huang

**Published:** 2026-03-26 | **Categories:** cs.CV, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2603.24941v1) | [PDF](https://arxiv.org/pdf/2603.24941v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models excel in robotic manipulation but suffer from significant inference latency due to processing dense visual tokens. Existing token reduction methods predominantly rely on attention magnitude as a static selection. In this work, we challenge this assumption, revealing that high-attention tokens are task-dependent and can even degrade policy performance. To address this, we introduce \textbf{TIES} (\textbf{T}au-guided \textbf{I}nter-layer \textbf{E}fficient \text...

</details>

---

### [SABER: A Stealthy Agentic Black-Box Attack Framework for Vision-Language-Action Models](https://arxiv.org/abs/2603.24935v1)

**Authors:** Xiyang Wu, Guangyao Shi, Qingzi Wang, Zongxia Li, Amrit Singh Bedi et al. (6 authors)

**Published:** 2026-03-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.24935v1) | [PDF](https://arxiv.org/pdf/2603.24935v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable robots to follow natural-language instructions grounded in visual observations, but the instruction channel also introduces a critical vulnerability: small textual perturbations can alter downstream robot behavior. Systematic robustness evaluation therefore requires a black-box attacker that can generate minimal yet effective instruction edits across diverse VLA models. To this end, we present SABER, an agent-centric approach for automatically generatin...

</details>

---

### [TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models](https://arxiv.org/abs/2603.24584v1)

**Authors:** Jiaying Zhou, Zhihao Zhan, Ruifeng Zhai, Qinhan Lyu, Hao Liu et al. (8 authors)

**Published:** 2026-03-25 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.24584v1) | [PDF](https://arxiv.org/pdf/2603.24584v1.pdf)

<details>
<summary>Abstract</summary>

Vision--Language--Action (VLA) policies have shown strong progress in mapping language instructions and visual observations to robotic actions, yet their reliability degrades in cluttered scenes with distractors. By analyzing failure cases, we find that many errors do not arise from infeasible motions, but from instance-level grounding failures: the policy often produces a plausible grasp trajectory that lands slightly off-target or even on the wrong object instance. To address this issue, we pr...

</details>

---

### [3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models](https://arxiv.org/abs/2603.24393v1)

**Authors:** Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei et al. (11 authors)

**Published:** 2026-03-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.24393v1) | [PDF](https://arxiv.org/pdf/2603.24393v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models leverage Multimodal Large Language Models (MLLMs) for robotic control, but recent studies reveal that MLLMs exhibit limited spatial intelligence due to training predominantly on 2D data, resulting in inadequate 3D perception for manipulation tasks. While recent approaches incorporate specialized 3D vision models such as VGGT to enhance spatial understanding, they employ diverse integration mechanisms without systematic investigation, leaving the optimal fusion...

</details>

---
