# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-01-26 14:33 UTC

**Papers found:** 47

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers](https://arxiv.org/abs/2601.14133v1)

**Authors:** Bin Yu, Shijie Lian, Xiaopeng Lin, Yuliang Wei, Zhaolong Shen et al. (11 authors)

**Published:** 2026-01-20 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.14133v1) | [PDF](https://arxiv.org/pdf/2601.14133v1.pdf) | [GitHub](https://github.com/ZGC-EmbodyAI/TwinBrainVLA)

<details>
<summary>Abstract</summary>

Standard Vision-Language-Action (VLA) models typically fine-tune a monolithic Vision-Language Model (VLM) backbone explicitly for robotic control. However, this approach creates a critical tension between maintaining high-level general semantic understanding and learning low-level, fine-grained sensorimotor skills, often leading to "catastrophic forgetting" of the model's open-world capabilities. To resolve this conflict, we introduce TwinBrainVLA, a novel architecture that coordinates a general...

</details>

---

### [VLAgents: A Policy Server for Efficient VLA Inference](https://arxiv.org/abs/2601.11250v1)

**Authors:** Tobias Jülg, Khaled Gamal, Nisarga Nilavadi, Pierre Krack, Seongjin Bien et al. (8 authors)

**Published:** 2026-01-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.11250v1) | [PDF](https://arxiv.org/pdf/2601.11250v1.pdf) | [GitHub](https://github.com/RobotControlStack/vlagents)

<details>
<summary>Abstract</summary>

The rapid emergence of Vision-Language-Action models (VLAs) has a significant impact on robotics. However, their deployment remains complex due to the fragmented interfaces and the inherent communication latency in distributed setups. To address this, we introduce VLAgents, a modular policy server that abstracts VLA inferencing behind a unified Gymnasium-style protocol. Crucially, its communication layer transparently adapts to the context by supporting both zero-copy shared memory for high-spee...

</details>

---

### [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](https://arxiv.org/abs/2601.09708v1)

**Authors:** Chi-Pin Huang, Yunze Man, Zhiding Yu, Min-Hung Chen, Jan Kautz et al. (7 authors)

**Published:** 2026-01-14 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2601.09708v1) | [PDF](https://arxiv.org/pdf/2601.09708v1.pdf) | [Project Page](https://jasper0314-huang.github.io/fast-thinkact/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) tasks require reasoning over complex visual scenes and executing adaptive actions in dynamic environments. While recent studies on reasoning VLAs show that explicit chain-of-thought (CoT) can improve generalization, they suffer from high inference latency due to lengthy reasoning traces. We propose Fast-ThinkAct, an efficient reasoning framework that achieves compact yet performant planning through verbalizable latent reasoning. Fast-ThinkAct learns to reason efficie...

</details>

---

### [CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion](https://arxiv.org/abs/2601.09512v1)

**Authors:** Ralf Römer, Yi Zhang, Angela P. Schoellig

**Published:** 2026-01-14 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2601.09512v1) | [PDF](https://arxiv.org/pdf/2601.09512v1.pdf) | [Project Page](https://tum-lsy.github.io/clare)

<details>
<summary>Abstract</summary>

To teach robots complex manipulation tasks, it is now a common practice to fine-tune a pre-trained vision-language-action model (VLA) on task-specific data. However, since this recipe updates existing representations, it is unsuitable for long-term operation in the real world, where robots must continually adapt to new tasks and environments while retaining the knowledge they have already acquired. Existing continual learning methods for robotics commonly require storing previous data (exemplars...

</details>

---

### [VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory](https://arxiv.org/abs/2601.08665v1)

**Authors:** Shaoan Wang, Yuanfei Luo, Xingyu Chen, Aocheng Luo, Dongyue Li et al. (9 authors)

**Published:** 2026-01-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.08665v1) | [PDF](https://arxiv.org/pdf/2601.08665v1.pdf) | [Project Page](https://wsakobe.github.io/VLingNav-web/)

<details>
<summary>Abstract</summary>

VLA models have shown promising potential in embodied navigation by unifying perception and planning while inheriting the strong generalization abilities of large VLMs. However, most existing VLA models rely on reactive mappings directly from observations to actions, lacking the explicit reasoning capabilities and persistent memory required for complex, long-horizon navigation tasks. To address these challenges, we propose VLingNav, a VLA model for embodied navigation grounded in linguistic-driv...

</details>

---

### [LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model](https://arxiv.org/abs/2601.05248v1)

**Authors:** Zhuoyang Liu, Jiaming Liu, Hao Chen, Ziyu Guo, Chengkai Hou et al. (13 authors)

**Published:** 2026-01-08 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.05248v1) | [PDF](https://arxiv.org/pdf/2601.05248v1.pdf) | [Project Page](https://sites.google.com/view/last0)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently demonstrated strong generalization capabilities in robotic manipulation. Some existing VLA approaches attempt to improve action accuracy by explicitly generating linguistic reasoning traces or future visual observations before action execution. However, explicit reasoning typically incurs non-negligible inference latency, which constrains the temporal resolution required for robotic manipulation. Moreover, such reasoning is confined to the lingui...

</details>

---

### [CLAP: Contrastive Latent Action Pretraining for Learning Vision-Language-Action Models from Human Videos](https://arxiv.org/abs/2601.04061v1)

**Authors:** Chubin Zhang, Jianan Wang, Zifeng Gao, Yue Su, Tianru Dai et al. (8 authors)

**Published:** 2026-01-07 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.04061v1) | [PDF](https://arxiv.org/pdf/2601.04061v1.pdf) | [Project Page](https://lin-shan.com/CLAP/)

<details>
<summary>Abstract</summary>

Generalist Vision-Language-Action models are currently hindered by the scarcity of robotic data compared to the abundance of human video demonstrations. Existing Latent Action Models attempt to leverage video data but often suffer from visual entanglement, capturing noise rather than manipulation skills. To address this, we propose Contrastive Latent Action Pretraining (CLAP), a framework that aligns the visual latent space from videos with a proprioceptive latent space from robot trajectories. ...

</details>

---

### [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](https://arxiv.org/abs/2601.02456v1)

**Authors:** Junhao Cai, Zetao Cai, Jiafei Cao, Yilun Chen, Zeyu He et al. (42 authors)

**Published:** 2026-01-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.02456v1) | [PDF](https://arxiv.org/pdf/2601.02456v1.pdf) | [Project Page](https://internrobotics.github.io/internvla-a1.github.io/)

<details>
<summary>Abstract</summary>

Prevalent Vision-Language-Action (VLA) models are typically built upon Multimodal Large Language Models (MLLMs) and demonstrate exceptional proficiency in semantic understanding, but they inherently lack the capability to deduce physical world dynamics. Consequently, recent approaches have shifted toward World Models, typically formulated via video prediction; however, these methods often suffer from a lack of semantic grounding and exhibit brittleness when handling prediction errors. To synergi...

</details>

---

### [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding](https://arxiv.org/abs/2601.02295v1)

**Authors:** Chenyang Ma, Guangyu Yang, Kai Lu, Shitong Xu, Bill Byrne et al. (7 authors)

**Published:** 2026-01-05 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.02295v1) | [PDF](https://arxiv.org/pdf/2601.02295v1.pdf) | [Project Page](https://dannymcy.github.io/cyclevla/)

<details>
<summary>Abstract</summary>

Current work on robot failure detection and correction typically operate in a post hoc manner, analyzing errors and applying corrections only after failures occur. This work introduces CycleVLA, a system that equips Vision-Language-Action models (VLAs) with proactive self-correction, the capability to anticipate incipient failures and recover before they fully manifest during execution. CycleVLA achieves this by integrating a progress-aware VLA that flags critical subtask transition points where...

</details>

---

### [Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2601.01618v1)

**Authors:** Huajie Tan, Peterson Co, Yijie Xu, Shanyu Rong, Yuheng Ji et al. (12 authors)

**Published:** 2026-01-04 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.01618v1) | [PDF](https://arxiv.org/pdf/2601.01618v1.pdf) | [Project Page](https://action-sketcher.github.io)

<details>
<summary>Abstract</summary>

Long-horizon robotic manipulation is increasingly important for real-world deployment, requiring spatial disambiguation in complex layouts and temporal resilience under dynamic interaction. However, existing end-to-end and hierarchical Vision-Language-Action (VLA) policies often rely on text-only cues while keeping plan intent latent, which undermines referential grounding in cluttered or underspecified scenes, impedes effective task decomposition of long-horizon goals with close-loop interactio...

</details>

---

## Other Recent Papers

### [ReViP: Reducing False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance](https://arxiv.org/abs/2601.16667v1)

**Authors:** Zhuohao Li, Yinghao Li, Jian-Jian Jiang, Lang Zhou, Tianyu Zhang et al. (6 authors)

**Published:** 2026-01-23 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.16667v1) | [PDF](https://arxiv.org/pdf/2601.16667v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced robotic manipulation by combining vision, language, and proprioception to predict actions. However, previous methods fuse proprioceptive signals directly with VLM-encoded vision-language features, resulting in state-dominant bias and false completions despite visible execution failures. We attribute this to modality imbalance, where policies over-rely on internal state while underusing visual evidence. To address this, we present ReViP, a novel V...

</details>

---

### [IVRA: Improving Visual-Token Relations for Robot Action Policy with Training-Free Hint-Based Guidance](https://arxiv.org/abs/2601.16207v1)

**Authors:** Jongwoo Park, Kanchana Ranasinghe, Jinhyeok Jang, Cristina Mata, Yoo Sung Jang et al. (6 authors)

**Published:** 2026-01-22 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.16207v1) | [PDF](https://arxiv.org/pdf/2601.16207v1.pdf)

<details>
<summary>Abstract</summary>

Many Vision-Language-Action (VLA) models flatten image patches into a 1D token sequence, weakening the 2D spatial cues needed for precise manipulation. We introduce IVRA, a lightweight, training-free method that improves spatial understanding by exploiting affinity hints already available in the model's built-in vision encoder, without requiring any external encoder or retraining. IVRA selectively injects these affinity signals into a language-model layer in which instance-level features reside....

</details>

---

### [DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models](https://arxiv.org/abs/2601.16065v1)

**Authors:** Chenyang Li, Jieyuan Liu, Bin Li, Bo Gao, Yilin Yuan et al. (8 authors)

**Published:** 2026-01-22 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.16065v1) | [PDF](https://arxiv.org/pdf/2601.16065v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language Action (VLA) models have shown remarkable progress in robotic manipulation by leveraging the powerful perception abilities of Vision-Language Models (VLMs) to understand environments and directly output actions. However, by default, VLA models may overly attend to image tokens in the task-irrelevant region, which we describe as 'distracting tokens'. This behavior can disturb the model from the generation of the desired action tokens in each step, affecting the success rate of tas...

</details>

---

### [Off-Policy Actor-Critic with Sigmoid-Bounded Entropy for Real-World Robot Learning](https://arxiv.org/abs/2601.15761v1)

**Authors:** Xiefeng Wu, Mingyu Hu, Shu Zhang

**Published:** 2026-01-22 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.15761v1) | [PDF](https://arxiv.org/pdf/2601.15761v1.pdf)

<details>
<summary>Abstract</summary>

Deploying reinforcement learning in the real world remains challenging due to sample inefficiency, sparse rewards, and noisy visual observations. Prior work leverages demonstrations and human feedback to improve learning efficiency and robustness. However, offline-to-online methods need large datasets and can be unstable, while VLA-assisted RL relies on large-scale pretraining and fine-tuning. As a result, a low-cost real-world RL method with minimal data requirements has yet to emerge. We intro...

</details>

---

### [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163v1)

**Authors:** Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, Yen-Chen Lin, Yunhao Ge et al. (11 authors)

**Published:** 2026-01-22 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.16163v1) | [PDF](https://arxiv.org/pdf/2601.16163v1.pdf)

<details>
<summary>Abstract</summary>

Recent video generation models demonstrate remarkable ability to capture complex physical interactions and scene evolution over time. To leverage their spatiotemporal priors, robotics works have adapted video models for policy learning but introduce complexity by requiring multiple stages of post-training and new architectural components for action generation. In this work, we introduce Cosmos Policy, a simple approach for adapting a large pretrained video model (Cosmos-Predict2) into an effecti...

</details>

---

### [CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation](https://arxiv.org/abs/2601.15541v1)

**Authors:** Heng Zhang, Wei-Hsing Huang, Qiyi Tong, Gokhan Solak, Puze Liu et al. (8 authors)

**Published:** 2026-01-21 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.15541v1) | [PDF](https://arxiv.org/pdf/2601.15541v1.pdf)

<details>
<summary>Abstract</summary>

We propose a CompliantVLA-adaptor that augments the state-of-the-art Vision-Language-Action (VLA) models with vision-language model (VLM)-informed context-aware variable impedance control (VIC) to improve the safety and effectiveness of contact-rich robotic manipulation tasks. Existing VLA systems (e.g., RDT, Pi0, OpenVLA-oft) typically output position, but lack force-aware adaptation, leading to unsafe or failed interactions in physical tasks involving contact, compliance, or uncertainty. In th...

</details>

---

### [BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries](https://arxiv.org/abs/2601.15197v2)

**Authors:** Shijie Lian, Bin Yu, Xiaopeng Lin, Laurence T. Yang, Zhaolong Shen et al. (9 authors)

**Published:** 2026-01-21 | **Categories:** cs.AI, cs.CL, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.15197v2) | [PDF](https://arxiv.org/pdf/2601.15197v2.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown promise in robot manipulation but often struggle to generalize to new instructions or complex multi-task scenarios. We identify a critical pathology in current training paradigms where goal-driven data collection creates a dataset bias. In such datasets, language instructions are highly predictable from visual observations alone, causing the conditional mutual information between instructions and actions to vanish, a phenomenon we term Information C...

</details>

---

### [TIDAL: Temporally Interleaved Diffusion and Action Loop for High-Frequency VLA Control](https://arxiv.org/abs/2601.14945v1)

**Authors:** Yuteng Sun, Haoran Wang, Ruofei Bai, Zhengguo Li, Jun Li et al. (8 authors)

**Published:** 2026-01-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.14945v1) | [PDF](https://arxiv.org/pdf/2601.14945v1.pdf)

<details>
<summary>Abstract</summary>

Large-scale Vision-Language-Action (VLA) models offer semantic generalization but suffer from high inference latency, limiting them to low-frequency batch-and-execute paradigm. This frequency mismatch creates an execution blind spot, causing failures in dynamic environments where targets move during the open-loop execution window. We propose TIDAL (Temporally Interleaved Diffusion and Action Loop), a hierarchical framework that decouples semantic reasoning from high-frequency actuation. TIDAL op...

</details>

---

### [A Brain-inspired Embodied Intelligence for Fluid and Fast Reflexive Robotics Control](https://arxiv.org/abs/2601.14628v1)

**Authors:** Weiyu Guo, He Zhang, Pengteng Li, Tiefu Cai, Ziyang Chen et al. (10 authors)

**Published:** 2026-01-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.14628v1) | [PDF](https://arxiv.org/pdf/2601.14628v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in embodied intelligence have leveraged massive scaling of data and model parameters to master natural-language command following and multi-task control. In contrast, biological systems demonstrate an innate ability to acquire skills rapidly from sparse experience. Crucially, current robotic policies struggle to replicate the dynamic stability, reflexive responsiveness, and temporal memory inherent in biological motion. Here we present Neuromorphic Vision-Language-Action (NeuroVL...

</details>

---

### [FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation](https://arxiv.org/abs/2601.13976v2)

**Authors:** Jing Zuo, Lingzhou Mu, Fan Jiang, Chengcheng Ma, Mu Xu et al. (6 authors)

**Published:** 2026-01-20 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.13976v2) | [PDF](https://arxiv.org/pdf/2601.13976v2.pdf)

<details>
<summary>Abstract</summary>

Achieving human-level performance in Vision-and-Language Navigation (VLN) requires an embodied agent to jointly understand multimodal instructions and visual-spatial context while reasoning over long action sequences. Recent works, such as NavCoT and NavGPT-2, demonstrate the potential of Chain-of-Thought (CoT) reasoning for improving interpretability and long-horizon planning. Moreover, multimodal extensions like OctoNav-R1 and CoT-VLA further validate CoT as a promising pathway toward human-li...

</details>

---

### [DroneVLA: VLA based Aerial Manipulation](https://arxiv.org/abs/2601.13809v2)

**Authors:** Fawad Mehboob, Monijesu James, Amir Habel, Jeffrin Sam, Miguel Altamirano Cabrera et al. (6 authors)

**Published:** 2026-01-20 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.13809v2) | [PDF](https://arxiv.org/pdf/2601.13809v2.pdf)

<details>
<summary>Abstract</summary>

As aerial platforms evolve from passive observers to active manipulators, the challenge shifts toward designing intuitive interfaces that allow non-expert users to command these systems naturally. This work introduces a novel concept of autonomous aerial manipulation system capable of interpreting high-level natural language commands to retrieve objects and deliver them to a human user. The system is intended to integrate a MediaPipe based on Grounding DINO and a Vision-Language-Action (VLA) mod...

</details>

---

### [SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2601.14323v1)

**Authors:** Bingxin Xu, Yuzhang Shang, Binghui Wang, Emilio Ferrara

**Published:** 2026-01-20 | **Categories:** cs.CR, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.14323v1) | [PDF](https://arxiv.org/pdf/2601.14323v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly deployed in safety-critical robotic applications, yet their security vulnerabilities remain underexplored. We identify a fundamental security flaw in modern VLA systems: the combination of action chunking and delta pose representations creates an intra-chunk visual open-loop. This mechanism forces the robot to execute K-step action sequences, allowing per-step perturbations to accumulate through integration. We propose SILENTDRIFT, a stealthy ...

</details>

---

### [Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993v1)

**Authors:** Hao Luo, Ye Wang, Wanpeng Zhang, Sipeng Zheng, Ziheng Xi et al. (12 authors)

**Published:** 2026-01-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.12993v1) | [PDF](https://arxiv.org/pdf/2601.12993v1.pdf)

<details>
<summary>Abstract</summary>

We introduce Being-H0.5, a foundational Vision-Language-Action (VLA) model designed for robust cross-embodiment generalization across diverse robotic platforms. While existing VLAs often struggle with morphological heterogeneity and data scarcity, we propose a human-centric learning paradigm that treats human interaction traces as a universal "mother tongue" for physical interaction. To support this, we present UniHand-2.0, the largest embodied pre-training recipe to date, comprising over 35,000...

</details>

---

### [Listen, Look, Drive: Coupling Audio Instructions for User-aware VLA-based Autonomous Driving](https://arxiv.org/abs/2601.12142v1)

**Authors:** Ziang Guo, Feng Yang, Xuefeng Zhang, Jiaqi Guo, Kun Zhao et al. (8 authors)

**Published:** 2026-01-17 | **Categories:** eess.AS, cs.MM, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.12142v1) | [PDF](https://arxiv.org/pdf/2601.12142v1.pdf)

<details>
<summary>Abstract</summary>

Vision Language Action (VLA) models promise an open-vocabulary interface that can translate perceptual ambiguity into semantically grounded driving decisions, yet they still treat language as a static prior fixed at inference time. As a result, the model must infer continuously shifting objectives from pixels alone, yielding delayed or overly conservative maneuvers. We argue that effective VLAs for autonomous driving need an online channel in which users can influence driving with specific inten...

</details>

---

### [Generative Scenario Rollouts for End-to-End Autonomous Driving](https://arxiv.org/abs/2601.11475v1)

**Authors:** Rajeev Yasarla, Deepti Hegde, Shizhong Han, Hsin-Pai Cheng, Yunxiao Shi et al. (13 authors)

**Published:** 2026-01-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.11475v1) | [PDF](https://arxiv.org/pdf/2601.11475v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are emerging as highly effective planning models for end-to-end autonomous driving systems. However, current works mostly rely on imitation learning from sparse trajectory annotations and under-utilize their potential as generative models. We propose Generative Scenario Rollouts (GeRo), a plug-and-play framework for VLA models that jointly performs planning and generation of language-grounded future traffic scenes through an autoregressive rollout strategy. Fi...

</details>

---

### [The Great March 100: 100 Detail-oriented Tasks for Evaluating Embodied AI Agents](https://arxiv.org/abs/2601.11421v1)

**Authors:** Ziyu Wang, Chenyuan Liu, Yushun Xiang, Runhao Zhang, Qingbo Hao et al. (19 authors)

**Published:** 2026-01-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.11421v1) | [PDF](https://arxiv.org/pdf/2601.11421v1.pdf)

<details>
<summary>Abstract</summary>

Recently, with the rapid development of robot learning and imitation learning, numerous datasets and methods have emerged. However, these datasets and their task designs often lack systematic consideration and principles. This raises important questions: Do the current datasets and task designs truly advance the capabilities of robotic agents? Do evaluations on a few common tasks accurately reflect the differentiated performance of various methods proposed by different teams and evaluated on dif...

</details>

---

### [ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models](https://arxiv.org/abs/2601.11404v1)

**Authors:** Linqing Zhong, Yi Liu, Yifei Wei, Ziyu Xiong, Maoqing Yao et al. (7 authors)

**Published:** 2026-01-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.11404v1) | [PDF](https://arxiv.org/pdf/2601.11404v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as essential generalist robot policies for diverse manipulation tasks, conventionally relying on directly translating multimodal inputs into actions via Vision-Language Model (VLM) embeddings. Recent advancements have introduced explicit intermediary reasoning, such as sub-task prediction (language) or goal image synthesis (vision), to guide action generation. However, these intermediate reasoning are often indirect and inherently limited in their...

</details>

---

### [Evaluating Self-Correcting Vision Agents Through Quantitative and Qualitative Metrics](https://arxiv.org/abs/2601.11637v1)

**Authors:** Aradhya Dixit

**Published:** 2026-01-14 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.11637v1) | [PDF](https://arxiv.org/pdf/2601.11637v1.pdf)

<details>
<summary>Abstract</summary>

Recent progress in multimodal foundation models has enabled Vision-Language Agents (VLAs) to decompose complex visual tasks into executable tool-based plans. While recent benchmarks have begun to evaluate iterative self-correction, its quantitative limits and dominant reasoning bottlenecks remain poorly characterized. This work introduces a Diagnostic Micro-Benchmark. Our analysis decouples Task Success Rate (TSR = 62 percent) from Correction Success Rate (CSR = 25 to 33 percent), revealing that...

</details>

---

### [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://arxiv.org/abs/2601.08325v1)

**Authors:** Zhenyang Liu, Yongchong Gu, Yikai Wang, Xiangyang Xue, Yanwei Fu

**Published:** 2026-01-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.08325v1) | [PDF](https://arxiv.org/pdf/2601.08325v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in robot manipulation have leveraged pre-trained vision-language models (VLMs) and explored integrating 3D spatial signals into these models for effective action prediction, giving rise to the promising vision-language-action (VLA) paradigm. However, most existing approaches overlook the importance of active perception: they typically rely on static, wrist-mounted cameras that provide an end-effector-centric viewpoint. As a result, these models are unable to adaptively select opt...

</details>

---

### [Motion Focus Recognition in Fast-Moving Egocentric Video](https://arxiv.org/abs/2601.07154v1)

**Authors:** Daniel Hong, James Tribble, Hao Wang, Chaoyi Zhou, Ashish Bastola et al. (7 authors)

**Published:** 2026-01-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.07154v1) | [PDF](https://arxiv.org/pdf/2601.07154v1.pdf)

<details>
<summary>Abstract</summary>

From Vision-Language-Action (VLA) systems to robotics, existing egocentric datasets primarily focus on action recognition tasks, while largely overlooking the inherent role of motion analysis in sports and other fast-movement scenarios. To bridge this gap, we propose a real-time motion focus recognition method that estimates the subject's locomotion intention from any egocentric video. Our approach leverages the foundation model for camera pose estimation and introduces system-level optimization...

</details>

---

### [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2601.07060v1)

**Authors:** Yuanzhe Liu, Jingyuan Zhu, Yuchen Mo, Gen Li, Xu Cao et al. (12 authors)

**Published:** 2026-01-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.07060v1) | [PDF](https://arxiv.org/pdf/2601.07060v1.pdf)

<details>
<summary>Abstract</summary>

Recent advancements in vision-language-action (VLA) models have shown promise in robotic manipulation, yet they continue to struggle with long-horizon, multi-step tasks. Existing methods lack internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask, leading to critical execution errors such as repeated actions, missed steps, and premature termination. To address these challenges, we introduce PALM, a VLA framework that structures policy le...

</details>

---

### [On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning](https://arxiv.org/abs/2601.06748v2)

**Authors:** Changyu Liu, Yiyang Liu, Taowen Wang, Qiao Zhuang, James Chenhao Liang et al. (10 authors)

**Published:** 2026-01-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.06748v2) | [PDF](https://arxiv.org/pdf/2601.06748v2.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models have recently emerged as a powerful paradigm for general-purpose robot learning, enabling agents to map visual observations and natural-language instructions into executable robotic actions. Though popular, they are primarily trained via supervised fine-tuning or training-time reinforcement learning, requiring explicit fine-tuning phases, human interventions, or controlled data collection. Consequently, existing methods remain unsuitable for challenging simulated- o...

</details>

---

### [CulinaryCut-VLAP: A Vision-Language-Action-Physics Framework for Food Cutting via a Force-Aware Material Point Method](https://arxiv.org/abs/2601.06451v1)

**Authors:** Hyunseo Koh, Chang-Yong Song, Youngjae Choi, Misa Viveiros, David Hyde et al. (6 authors)

**Published:** 2026-01-10 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.06451v1) | [PDF](https://arxiv.org/pdf/2601.06451v1.pdf)

<details>
<summary>Abstract</summary>

Food cutting is a highly practical yet underexplored application at the intersection of vision and robotic manipulation. The task remains challenging because interactions between the knife and deformable materials are highly nonlinear and often entail large deformations, frequent contact, and topological change, which in turn hinder stable and safe large-scale data collection. To address these challenges, we propose a unified framework that couples a vision-language-action (VLA) dataset with a p...

</details>

---

### [SparseOccVLA: Bridging Occupancy and Vision-Language Models via Sparse Queries for Unified 4D Scene Understanding and Planning](https://arxiv.org/abs/2601.06474v2)

**Authors:** Chenxu Dang, Jie Wang, Guang Li, Zhiwen Hou, Zihan You et al. (9 authors)

**Published:** 2026-01-10 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.06474v2) | [PDF](https://arxiv.org/pdf/2601.06474v2.pdf)

<details>
<summary>Abstract</summary>

In autonomous driving, Vision Language Models (VLMs) excel at high-level reasoning , whereas semantic occupancy provides fine-grained details. Despite significant progress in individual fields, there is still no method that can effectively integrate both paradigms. Conventional VLMs struggle with token explosion and limited spatiotemporal reasoning, while semantic occupancy provides a unified, explicit spatial representation but is too dense to integrate efficiently with VLMs. To address these c...

</details>

---

### [LatentVLA: Efficient Vision-Language Models for Autonomous Driving via Latent Action Prediction](https://arxiv.org/abs/2601.05611v1)

**Authors:** Chengen Xie, Bin Sun, Tianyu Li, Junjie Wu, Zhihui Hao et al. (7 authors)

**Published:** 2026-01-09 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.05611v1) | [PDF](https://arxiv.org/pdf/2601.05611v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving models trained on largescale datasets perform well in common scenarios but struggle with rare, long-tail situations due to limited scenario diversity. Recent Vision-Language-Action (VLA) models leverage broad knowledge from pre-trained visionlanguage models to address this limitation, yet face critical challenges: (1) numerical imprecision in trajectory prediction due to discrete tokenization, (2) heavy reliance on language annotations that introduce linguistic bias...

</details>

---

### [RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation](https://arxiv.org/abs/2601.05241v1)

**Authors:** Boyang Wang, Haoran Zhang, Shujie Zhang, Jinkun Hao, Mingda Jia et al. (11 authors)

**Published:** 2026-01-08 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.05241v1) | [PDF](https://arxiv.org/pdf/2601.05241v1.pdf)

<details>
<summary>Abstract</summary>

The diversity, quantity, and quality of manipulation data are critical for training effective robot policies. However, due to hardware and physical setup constraints, collecting large-scale real-world manipulation data remains difficult to scale across diverse environments. Recent work uses text-prompt conditioned image diffusion models to augment manipulation data by altering the backgrounds and tabletop objects in the visual observations. However, these approaches often overlook the practical ...

</details>

---

### [Stable Language Guidance for Vision-Language-Action Models](https://arxiv.org/abs/2601.04052v1)

**Authors:** Zhihao Zhan, Yuhao Chen, Jiaying Zhou, Qinhan Lv, Hao Liu et al. (8 authors)

**Published:** 2026-01-07 | **Categories:** cs.RO, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2601.04052v1) | [PDF](https://arxiv.org/pdf/2601.04052v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated impressive capabilities in generalized robotic control; however, they remain notoriously brittle to linguistic perturbations. We identify a critical ``modality collapse'' phenomenon where strong visual priors overwhelm sparse linguistic signals, causing agents to overfit to specific instruction phrasings while ignoring the underlying semantic intent. To address this, we propose \textbf{Residual Semantic Steering (RSS)}, a probabilistic framew...

</details>

---

### [State Backdoor: Towards Stealthy Real-world Poisoning Attack on Vision-Language-Action Model in State Space](https://arxiv.org/abs/2601.04266v1)

**Authors:** Ji Guo, Wenbo Jiang, Yansong Lin, Yijing Liu, Ruichen Zhang et al. (10 authors)

**Published:** 2026-01-07 | **Categories:** cs.CR, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2601.04266v1) | [PDF](https://arxiv.org/pdf/2601.04266v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are widely deployed in safety-critical embodied AI applications such as robotics. However, their complex multimodal interactions also expose new security vulnerabilities. In this paper, we investigate a backdoor threat in VLA models, where malicious inputs cause targeted misbehavior while preserving performance on clean data. Existing backdoor methods predominantly rely on inserting visible triggers into visual modality, which suffer from poor robustness and l...

</details>

---

### [A Vision-Language-Action Model with Visual Prompt for OFF-Road Autonomous Driving](https://arxiv.org/abs/2601.03519v2)

**Authors:** Liangdong Zhang, Yiming Nie, Haoyang Li, Fanjie Kong, Baobao Zhang et al. (9 authors)

**Published:** 2026-01-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.03519v2) | [PDF](https://arxiv.org/pdf/2601.03519v2.pdf)

<details>
<summary>Abstract</summary>

Efficient trajectory planning in off-road terrains presents a formidable challenge for autonomous vehicles, often necessitating complex multi-step pipelines. However, traditional approaches exhibit limited adaptability in dynamic environments. To address these limitations, this paper proposes OFF-EMMA, a novel end-to-end multimodal framework designed to overcome the deficiencies of insufficient spatial perception and unstable reasoning in visual-language-action (VLA) models for off-road autonomo...

</details>

---

### [I2E: From Image Pixels to Actionable Interactive Environments for Text-Guided Image Editing](https://arxiv.org/abs/2601.03741v1)

**Authors:** Jinghan Yu, Junhao Xiao, Chenyu Zhu, Jiaming Li, Jia Li et al. (12 authors)

**Published:** 2026-01-07 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.03741v1) | [PDF](https://arxiv.org/pdf/2601.03741v1.pdf)

<details>
<summary>Abstract</summary>

Existing text-guided image editing methods primarily rely on end-to-end pixel-level inpainting paradigm. Despite its success in simple scenarios, this paradigm still significantly struggles with compositional editing tasks that require precise local control and complex multi-object spatial reasoning. This paradigm is severely limited by 1) the implicit coupling of planning and execution, 2) the lack of object-level control granularity, and 3) the reliance on unstructured, pixel-centric modeling....

</details>

---

### [Limited Linguistic Diversity in Embodied AI Datasets](https://arxiv.org/abs/2601.03136v1)

**Authors:** Selma Wanna, Agnes Luhtaru, Jonathan Salfity, Ryan Barron, Juston Moore et al. (7 authors)

**Published:** 2026-01-06 | **Categories:** cs.CL, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.03136v1) | [PDF](https://arxiv.org/pdf/2601.03136v1.pdf)

<details>
<summary>Abstract</summary>

Language plays a critical role in Vision-Language-Action (VLA) models, yet the linguistic characteristics of the datasets used to train and evaluate these systems remain poorly documented. In this work, we present a systematic dataset audit of several widely used VLA corpora, aiming to characterize what kinds of instructions these datasets actually contain and how much linguistic variety they provide. We quantify instruction language along complementary dimensions-including lexical variety, dupl...

</details>

---

### [SOP: A Scalable Online Post-Training System for Vision-Language-Action Models](https://arxiv.org/abs/2601.03044v1)

**Authors:** Mingjie Pan, Siyuan Feng, Qinglin Zhang, Xinchen Li, Jianheng Song et al. (12 authors)

**Published:** 2026-01-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.03044v1) | [PDF](https://arxiv.org/pdf/2601.03044v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models achieve strong generalization through large-scale pre-training, but real-world deployment requires expert-level task proficiency in addition to broad generality. Existing post-training approaches for VLA models are typically offline, single-robot, or task-specific, limiting effective on-policy adaptation and scalable learning from real-world interaction. We introduce a Scalable Online Post-training (SOP) system that enables online, distributed, multi-task post...

</details>

---

### [VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models](https://arxiv.org/abs/2601.03309v1)

**Authors:** Jianke Zhang, Xiaoyu Chen, Qiuyue Wang, Mingsheng Li, Yanjiang Guo et al. (10 authors)

**Published:** 2026-01-06 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.03309v1) | [PDF](https://arxiv.org/pdf/2601.03309v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models, which integrate pretrained large Vision-Language Models (VLM) into their policy backbone, are gaining significant attention for their promising generalization capabilities. This paper revisits a fundamental yet seldom systematically studied question: how VLM choice and competence translate to downstream VLA policies performance? We introduce VLM4VLA, a minimal adaptation pipeline that converts general-purpose VLMs into VLA policies using only a small set of n...

</details>

---

### [Value Vision-Language-Action Planning & Search](https://arxiv.org/abs/2601.00969v1)

**Authors:** Ali Salamatian,  Ke,  Ren, Kieran Pattison, Cyrus Neary

**Published:** 2026-01-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.00969v1) | [PDF](https://arxiv.org/pdf/2601.00969v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as powerful generalist policies for robotic manipulation, yet they remain fundamentally limited by their reliance on behavior cloning, leading to brittleness under distribution shift. While augmenting pretrained models with test-time search algorithms like Monte Carlo Tree Search (MCTS) can mitigate these failures, existing formulations rely solely on the VLA prior for guidance, lacking a grounded estimate of expected future return. Consequently, ...

</details>

---

### [Dichotomous Diffusion Policy Optimization](https://arxiv.org/abs/2601.00898v1)

**Authors:** Ruiming Liang, Yinan Zheng, Kexin Zheng, Tianyi Tan, Jianxiong Li et al. (12 authors)

**Published:** 2025-12-31 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.00898v1) | [PDF](https://arxiv.org/pdf/2601.00898v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion-based policies have gained growing popularity in solving a wide range of decision-making tasks due to their superior expressiveness and controllable generation during inference. However, effectively training large diffusion policies using reinforcement learning (RL) remains challenging. Existing methods either suffer from unstable training due to directly maximizing value objectives, or face computational issues due to relying on crude Gaussian likelihood approximation, which requires ...

</details>

---

### [VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots](https://arxiv.org/abs/2512.24673v1)

**Authors:** Yongsheng Zhao, Lei Zhao, Baoping Cheng, Gongxin Yao, Xuanzhang Wen et al. (6 authors)

**Published:** 2025-12-31 | **Categories:** cs.RO, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2512.24673v1) | [PDF](https://arxiv.org/pdf/2512.24673v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved remarkable breakthroughs in robotics, with the action chunk playing a dominant role in these advances. Given the real-time and continuous nature of robotic motion control, the strategies for fusing a queue of successive action chunks have a profound impact on the overall performance of VLA models. Existing methods suffer from jitter, stalling, or even pauses in robotic action execution, which not only limits the achievable execution speed but als...

</details>

---

### [RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset for Generalizable Embodied Intelligence](https://arxiv.org/abs/2512.24653v2)

**Authors:** Chengkai Hou, Kun Wu, Jiaming Liu, Zhengping Che, Di Wu et al. (33 authors)

**Published:** 2025-12-31 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2512.24653v2) | [PDF](https://arxiv.org/pdf/2512.24653v2.pdf)

<details>
<summary>Abstract</summary>

While data-driven imitation learning has revolutionized robotic manipulation, current approaches remain constrained by the scarcity of large-scale, diverse real-world demonstrations. Consequently, the ability of existing models to generalize across long-horizon bimanual tasks and mobile manipulation in unstructured environments remains limited. To bridge this gap, we present RoboMIND 2.0, a comprehensive real-world dataset comprising over 310K dual-arm manipulation trajectories collected across ...

</details>

---
