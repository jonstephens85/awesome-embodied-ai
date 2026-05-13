# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-13 22:56 UTC

**Papers found:** 32

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://arxiv.org/abs/2605.12500v1)

**Authors:** Haiwen Diao, Penghao Wu, Hanming Deng, Jiahao Wang, Shihao Bai et al. (58 authors)

**Published:** 2026-05-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.12500v1) | [PDF](https://arxiv.org/pdf/2605.12500v1.pdf) | [GitHub](https://github.com/OpenSenseNova/SenseNova-U1)

<details>
<summary>Abstract</summary>

Recent large vision-language models (VLMs) remain fundamentally constrained by a persistent dichotomy: understanding and generation are treated as distinct problems, leading to fragmented architectures, cascaded pipelines, and misaligned representation spaces. We argue that this divide is not merely an engineering artifact, but a structural limitation that hinders the emergence of native multimodal intelligence. Hence, we introduce SenseNova-U1, a native unified multimodal paradigm built upon NE...

</details>

---

### [GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization](https://arxiv.org/abs/2605.12369v1)

**Authors:** Xiaosong Jia, Bowen Yang, Zuhao Ge, Xian Nie, Yuchen Zhou et al. (20 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.12369v1) | [PDF](https://arxiv.org/pdf/2605.12369v1.pdf) | [Project Page](https://guidedvla.github.io/project_page/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models aim for general robot learning by aligning action as a modality within powerful Vision-Language Models (VLMs). Existing VLAs rely on end-to-end supervision to implicitly enable the action decoding process to learn task-relevant features. However, without explicit guidance, these models often overfit to spurious correlations, such as visual shortcuts or environmental noise, limiting their generalization. In this paper, we introduce GuidedVLA, a framework design...

</details>

---

### [TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning](https://arxiv.org/abs/2605.12236v1)

**Authors:** Matthew M. Hong, Jesse Zhang, Anusha Nagabandi, Abhishek Gupta

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.12236v1) | [PDF](https://arxiv.org/pdf/2605.12236v1.pdf) | [Project Page](https://weirdlabuw.github.io/tmrl/)

<details>
<summary>Abstract</summary>

Fine-tuning pre-trained robot policies with reinforcement learning (RL) often inherits the bottlenecks introduced by pre-training with behavioral cloning (BC), which produces narrow action distributions that lack the coverage necessary for downstream exploration. We present a unified framework that enables the exploration necessary to enable efficient robot policy finetuning by bridging BC pre-training and RL fine-tuning. Our pre-training method, Context-Smoothed Pre-training (CSP), injects forw...

</details>

---

### [Learning Action Manifold with Multi-view Latent Priors for Robotic Manipulation](https://arxiv.org/abs/2605.11832v1)

**Authors:** Junjin Xiao, Dongyang Li, Yandan Yang, Shuang Zeng, Tong Lin et al. (12 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.11832v1) | [PDF](https://arxiv.org/pdf/2605.11832v1.pdf) | [Project Page](https://junjxiao.github.io/Multi-view-VLA.github.io/)

<details>
<summary>Abstract</summary>

This paper tackles spatial perception and manipulation challenges in Vision-Language-Action (VLA) models. To address depth ambiguity from monocular input, we leverage a pre-trained multi-view diffusion model to synthesize latent novel views and propose a Geometry-Guided Gated Transformer (G3T) that aligns multi-view features under 3D geometric guidance while adaptively filtering occlusion noise. To improve action learning efficiency, we introduce Action Manifold Learning (AML), which directly pr...

</details>

---

### [See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model](https://arxiv.org/abs/2605.11817v1)

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du et al. (7 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.11817v1) | [PDF](https://arxiv.org/pdf/2605.11817v1.pdf) | [GitHub](https://github.com/Fediory/Grid-Sampler)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment. Existing token pruning methods suffer from a fundamental trade-off: aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation. This forces a compromise, limiting the achievable compression rate and thus the potential speedup. We argue that breaking this t...

</details>

---

### [DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies](https://arxiv.org/abs/2605.11750v1)

**Authors:** Xianzhe Fan, Yuxiang Lu, Shenyuan Gao, Xiaoyang Wu, Ruihua Han et al. (7 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.11750v1) | [PDF](https://arxiv.org/pdf/2605.11750v1.pdf) | [GitHub](https://github.com/XianzheFan/DreamAvoid)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are often brittle in fine-grained manipulation, where minor action errors during the critical phases can rapidly escalate into irrecoverable failures. Since existing VLA models rely predominantly on successful demonstrations for training, they lack an explicit awareness of failure during these critical phases. To address this, we propose DreamAvoid, a critical-phase test-time dreaming framework that enables VLA models to anticipate and avoid failures. We also ...

</details>

---

### [PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2605.10925v1)

**Authors:** Xinyu Guo, Bin Xie, Wei Chai, Xianchi Deng, Tiancai Wang et al. (7 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10925v1) | [PDF](https://arxiv.org/pdf/2605.10925v1.pdf) | [Project Page](https://priorvla.github.io/)

<details>
<summary>Abstract</summary>

Large-scale pretraining has made Vision-Language-Action (VLA) models promising foundations for generalist robot manipulation, yet adapting them to downstream tasks remains necessary. However, the common practice of full fine-tuning treats pretraining as initialization and can shift broad priors toward narrow training-distribution patterns. We propose PriorVLA, a novel framework that preserves pretrained priors and learns to leverage them for effective adaptation. PriorVLA keeps a frozen Prior Ex...

</details>

---

### [RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark](https://arxiv.org/abs/2605.10921v1)

**Authors:** Huashuo Lei, Wenxuan Song, Huarui Zhang, Jieyuan Pei, Jiayi Chen et al. (13 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10921v1) | [PDF](https://arxiv.org/pdf/2605.10921v1.pdf) | [Project Page](https://robomemarena.github.io)

<details>
<summary>Abstract</summary>

Memory is a critical component of robotic intelligence, as robots must rely on past observations and actions to accomplish long-horizon tasks in partially observable environments. However, existing robotic memory benchmarks still lack multimodal annotations for memory formation, provide limited task coverage and structural complexity, and remain restricted to simulation without real-world evaluation. We address this gap with RoboMemArena, a large-scale benchmark of 26 tasks, with average traject...

</details>

---

### [CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving](https://arxiv.org/abs/2605.10426v1)

**Authors:** Minqing Huang, Yujiao Xiang, Zihan Liang, Jiajie Huang, Jingqi Wang et al. (10 authors)

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.10426v1) | [PDF](https://arxiv.org/pdf/2605.10426v1.pdf) | [GitHub](https://github.com/potatochip1211/CoWorld-VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving. However, existing reasoning mechanisms still struggle to provide planning-oriented intermediate representations: textual Chain-of-Thought (CoT) fails to preserve continuous spatiotemporal structure, while latent world reasoning remains difficult to use as a direct condition for action generation. In this paper, we propose CoWorld-VLA, a multi-expert world reasoning framework for autonomous...

</details>

---

## Other Recent Papers

### [Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334v1)

**Authors:** Yucen Wang, Rui Yu, Fengming Zhang, Junjie Lu, Xinyao Qin et al. (8 authors)

**Published:** 2026-05-12 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.12334v1) | [PDF](https://arxiv.org/pdf/2605.12334v1.pdf)

<details>
<summary>Abstract</summary>

Post-training Vision-Language-Action (VLA) models via reinforcement learning (RL) in learned world models has emerged as an effective strategy to adapt to new tasks without costly real-world interactions. However, while using imagined trajectories reduces the sample complexity of policy training, existing methods still heavily rely on task-specific data to fine-tune both the world and reward models, fundamentally limiting their scalability to unseen tasks. To overcome this, we argue that world a...

</details>

---

### [Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete](https://arxiv.org/abs/2605.12160v1)

**Authors:** Joonha Park, Jiseung Jeong, Taesik Gong

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.12160v1) | [PDF](https://arxiv.org/pdf/2605.12160v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies are typically evaluated as if the user had finished typing or speaking before the robot begins acting. In real deployment, however, users take several seconds to enter a request, leaving the policy idle for a substantial fraction of the interaction. We introduce Premover, a lightweight module that converts this idle window into useful precomputation. Premover keeps the VLA backbone frozen and attaches two small projection heads, one for image patches, one fo...

</details>

---

### [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090v1)

**Authors:** Siyin Wang, Junhao Shi, Zhaoyang Fu, Xinzhe He, Feihong Liu et al. (14 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.CL, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.12090v1) | [PDF](https://arxiv.org/pdf/2605.12090v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved strong semantic generalization for embodied policy learning, yet they learn reactive observation-to-action mappings without explicitly modeling how the physical world evolves under intervention. A growing body of work addresses this limitation by integrating world models, predictive models of environment dynamics, into the action generation pipeline. We term this emerging paradigm World Action Models (WAMs): embodied foundation models that unify ...

</details>

---

### [Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models](https://arxiv.org/abs/2605.11809v1)

**Authors:** Huoren Yang, Jianchao Zhao, Hu Yusong, Qiguan Ou, Yuyang Gao et al. (10 authors)

**Published:** 2026-05-12 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.11809v1) | [PDF](https://arxiv.org/pdf/2605.11809v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced rapidly with stronger backbones, broader pre-training, and larger demonstration datasets, yet their action heads remain largely homogeneous: most directly predict action commands in a fixed world coordinate frame. We propose \textbf{MCF-Proto}, a lightweight action head that equips VLA policies with a Motion-Centric Action Frame (MCF) and a prototype-based action parameterization. At each step, the policy predicts a rotation $R_t \in SO(3)$, comp...

</details>

---

### [OOM-Free Alpamayo via CPU-GPU Memory Swapping for Vision-Language-Action Models](https://arxiv.org/abs/2605.11678v1)

**Authors:** Seungwoo Roh, Huiyeong Kim, Jong-Chan Kim

**Published:** 2026-05-12 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.11678v1) | [PDF](https://arxiv.org/pdf/2605.11678v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end Vision-Language-Action (VLA) models for autonomous driving unify perception, reasoning, and control in a single neural network, achieving strong driving performance but requiring 20-60GB of GPU memory-far exceeding the 12-16GB available on commodity GPUs. We present a framework, which enables memory-efficient VLA inference on VRAM-constrained GPUs through system-level optimization alone, without model modification. Our work proceeds in three stages: (1) Sequential Demand Layering redu...

</details>

---

### [Dynamic Execution Commitment of Vision-Language-Action Models](https://arxiv.org/abs/2605.11567v1)

**Authors:** Feng Chen, Xianghui Wang, Yuxuan Chen, Boying Li, Yefei He et al. (7 authors)

**Published:** 2026-05-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.11567v1) | [PDF](https://arxiv.org/pdf/2605.11567v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models predominantly adopt action chunking, i.e., predicting and committing to a short horizon of consecutive low-level actions in a single forward pass, to amortize the inference cost of large-scale backbones and reduce per-step latency. However, committing these multi-step predictions to real-world execution requires balancing success rate against inference efficiency, a decision typically governed by fixed execution horizons tuned per task. Such heuristics ignore ...

</details>

---

### [RIO: Flexible Real-Time Robot I/O for Cross-Embodiment Robot Learning](https://arxiv.org/abs/2605.11564v1)

**Authors:** Pablo Ortega-Kral, Eliot Xing, Arthur Bucker, Vernon Luk, Junseo Kim et al. (16 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.11564v1) | [PDF](https://arxiv.org/pdf/2605.11564v1.pdf)

<details>
<summary>Abstract</summary>

Despite recent efforts to collect multi-task, multi-embodiment datasets, to design recipes for training Vision-Language-Action models (VLAs), and to showcase these models on different robot platforms, generalist cross-embodiment robot capabilities remains a largely elusive ideal. Progress is limited by fragmented infrastructure: most robot code is highly specific to the exact setup the user decided on, which adds major overhead when attempting to reuse, recycle, or share artifacts between users....

</details>

---

### [Overcoming Dynamics-Blindness: Training-Free Pace-and-Path Correction for VLA Models](https://arxiv.org/abs/2605.11459v1)

**Authors:** Yanyan Zhang, Chaoda Song, Vikash Singh, Xinpeng Li, Kai Ye et al. (9 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.11459v1) | [PDF](https://arxiv.org/pdf/2605.11459v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models achieve remarkable flexibility and generalization beyond classical control paradigms. However, most prevailing VLAs are trained under a single-frame observation paradigm, which leaves them structurally blind to temporal dynamics. Consequently, these models degrade severely in non-stationary scenarios, even when trained or finetuned on dynamic datasets. Existing approaches either require expensive retraining or suffer from latency bottlenecks and poor temporal ...

</details>

---

### [SafeManip: A Property-Driven Benchmark for Temporal Safety Evaluation in Robotic Manipulation](https://arxiv.org/abs/2605.12386v1)

**Authors:** Chengyue Huang, Khang Vo Huynh, Sebastian Elbaum, Zsolt Kira, Lu Feng

**Published:** 2026-05-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.12386v1) | [PDF](https://arxiv.org/pdf/2605.12386v1.pdf)

<details>
<summary>Abstract</summary>

Robotic manipulation is typically evaluated by task success, but successful completion does not guarantee safe execution. Many safety failures are temporal: a robot may touch a clean surface after contamination or release an object before it is fully inside an enclosure. We introduce SafeManip, a property-driven benchmark to explicitly evaluate temporal safety properties in robotic manipulation, moving beyond prior evaluations that largely focus on task completion or per-state constraint violati...

</details>

---

### [Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation](https://arxiv.org/abs/2605.11479v1)

**Authors:** Hao Wang, Joshua Bowden, Colton Crosby, Somil Bansal

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.11479v1) | [PDF](https://arxiv.org/pdf/2605.11479v1.pdf)

<details>
<summary>Abstract</summary>

Policy evaluation is a fundamental component of the development and deployment pipeline for robotic policies. In modern manipulation systems, this problem is particularly challenging: rewards are often sparse, task progression of evaluation rollouts are often non-monotonic as the policies exhibit recovery behaviors, and evaluation rollouts are necessarily of finite length. This finite length introduces truncation bias, breaking the infinite-horizon assumptions underlying standard methods relying...

</details>

---

### [Variational Linear Attention: Stable Associative Memory for Long-Context Transformers](https://arxiv.org/abs/2605.11196v1)

**Authors:** Vishal Pandey, Gopal Singh

**Published:** 2026-05-11 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.11196v1) | [PDF](https://arxiv.org/pdf/2605.11196v1.pdf)

<details>
<summary>Abstract</summary>

Linear attention reduces the quadratic cost of softmax attention to $\mathcal{O}(T)$, but its memory state grows as $\mathcal{O}(T)$ in Frobenius norm, causing progressive interference between stored associations. We introduce \textbf{Variational Linear Attention} (VLA), which reframes the memory update as an online regularised least-squares problem with an adaptive penalty matrix maintained via the Sherman-Morrison rank-1 formula. We prove that normalising the write direction to unit length giv...

</details>

---

### [RankQ: Offline-to-Online Reinforcement Learning via Self-Supervised Action Ranking](https://arxiv.org/abs/2605.11151v1)

**Authors:** Andrew Choi, Wei Xu

**Published:** 2026-05-11 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.11151v1) | [PDF](https://arxiv.org/pdf/2605.11151v1.pdf)

<details>
<summary>Abstract</summary>

Offline-to-online reinforcement learning (RL) improves sample efficiency by leveraging pre-collected datasets prior to online interaction. A key challenge, however, is learning an accurate critic in large state--action spaces with limited dataset coverage. To mitigate harmful updates from value overestimation, prior methods impose pessimism by down-weighting out-of-distribution (OOD) actions relative to dataset actions. While effective, this essentially acts as a behavior cloning anchor and can ...

</details>

---

### [SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection](https://arxiv.org/abs/2605.11114v1)

**Authors:** Tianchonghui Fang, Yuan Zhuang, Fei Miao

**Published:** 2026-05-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.11114v1) | [PDF](https://arxiv.org/pdf/2605.11114v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) and imitation-learning policies trained via community toolchains on low-cost hardware frequently fail when deployed outside the training environment. Existing evaluations, including the original ACT and SmolVLA benchmarks, demonstrate high success rates under controlled, fixed backgrounds, yet community practitioners report near-zero transfer to new environments. We present SEVO (Semantic-Enhanced Virtual Observation), a data-centric approach that improves cross-envi...

</details>

---

### [HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models](https://arxiv.org/abs/2605.10942v1)

**Authors:** Qiuxuan Feng, Jiale Yu, Jiaming Liu, Yueru Jia, Zhuangzhe Wu et al. (11 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10942v1) | [PDF](https://arxiv.org/pdf/2605.10942v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) have emerged as a promising paradigm for robot control by modeling physical dynamics. Current WAMs generally follow two paradigms: the "Imagine-then-Execute" approach, which uses video prediction to infer actions via inverse dynamics, and the "Joint Modeling" approach, which jointly models actions and video representations. Based on systematic experiments, we observe a fundamental trade-off between these paradigms: the former explicitly leverages world models for gener...

</details>

---

### [CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models](https://arxiv.org/abs/2605.10903v1)

**Authors:** Wenxuan Song, Han Zhao, Fuhao Li, Ziyang Zhou, Xi Wang et al. (10 authors)

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10903v1) | [PDF](https://arxiv.org/pdf/2605.10903v1.pdf)

<details>
<summary>Abstract</summary>

This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Some advanced finetuning methods with auxiliary training objectives can improve performance and reduce the number of convergence steps. However, they typically incur significant computational overhead due to the additional losses from auxiliary objectives. To simultaneously achieve the enhan...

</details>

---

### [Unified Noise Steering for Efficient Human-Guided VLA Adaptation](https://arxiv.org/abs/2605.10821v1)

**Authors:** Junjie Lu, Xinyao Qin, Yuhua Jiang, Kaixin Wang, Chuheng Zhang et al. (9 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10821v1) | [PDF](https://arxiv.org/pdf/2605.10821v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion-based vision-language-action (VLA) models have emerged as strong priors for robotic manipulation, yet adapting them to real-world distributions remains challenging. In particular, on-robot reinforcement learning (RL) is expensive and time-consuming, so effective adaptation depends on efficient policy improvement within a limited budget of real-world interactions. Noise-space RL lowers the cost by keeping the pretrained VLA fixed as a denoising generator while updating only a lightweigh...

</details>

---

### [ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models](https://arxiv.org/abs/2605.10819v1)

**Authors:** Zuojin Tang, Haoyun Liu, Xinyuan Chang, Changjie Wu, Dongjie Huo et al. (14 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.10819v1) | [PDF](https://arxiv.org/pdf/2605.10819v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models remain constrained by the scarcity of action-labeled robot data, whereas action-free videos provide abundant evidence of how the physical world changes. Latent action models offer a promising way to extract such priors from videos, but reconstruction-trained latent codes are not necessarily suitable for policy generation: they may predict future observations while lacking the structure needed to be reused or generated coherently with robot actions. We introduc...

</details>

---

### [VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models](https://arxiv.org/abs/2605.10485v1)

**Authors:** Hao Wang, Xiaobao Wei, Jingyang He, Chengyu Bai, Chun-Kai Fan et al. (13 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10485v1) | [PDF](https://arxiv.org/pdf/2605.10485v1.pdf)

<details>
<summary>Abstract</summary>

Precise spatial reasoning is fundamental to robotic manipulation, yet the visual backbones of current vision-language-action (VLA) models are predominantly pretrained on 2D image data without explicit 3D geometric supervision, resulting in representations that lack accurate spatial awareness. Existing implicit spatial grounding methods partially address this by aligning VLA features with those of 3D-aware foundation models, but they rely on empirical layer search and perform alignment on LLM-lev...

</details>

---

### [Temporal Sampling Frequency Matters: A Capacity-Aware Study of End-to-End Driving Trajectory Prediction](https://arxiv.org/abs/2605.10388v1)

**Authors:** Yumao Liu, Tao Liu, Xiangyu Li, Jiaxiang Li, Ke Ma

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10388v1) | [PDF](https://arxiv.org/pdf/2605.10388v1.pdf)

<details>
<summary>Abstract</summary>

End to end (E2E) autonomous driving trajectory prediction is often trained with camera frames sampled at the highest available temporal frequency, assuming that denser sampling improves performance. We question this assumption by treating temporal sampling frequency as an explicit training set design variable. Starting from high frequency E2E driving datasets, we construct frequency sweep training sets by temporally subsampling camera frames along each trajectory. For each model dataset pair, we...

</details>

---

### [Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs](https://arxiv.org/abs/2605.10094v2)

**Authors:** Jianchao Zhao, Huoren Yang, Yusong Hu, Yuyang Gao, Qiguan Ou et al. (9 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.10094v2) | [PDF](https://arxiv.org/pdf/2605.10094v2.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models show strong potential for general-purpose robotic manipulation, yet their closed-loop reliability often degrades under local deployment conditions. Existing evaluations typically treat test episodes as independent zero-shot trials. However, real robots often operate repeatedly in the same or slowly changing environments, where successful executions provide environment-verified evidence of reliable behavior patterns. We study this persistent-deployment setting,...

</details>

---

### [StereoPolicy: Improving Robotic Manipulation Policies via Stereo Perception](https://arxiv.org/abs/2605.09989v1)

**Authors:** Evans Han, Yunfan Jiang, Yingke Wang, Haoyue Xiao, Huang Huang et al. (9 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.09989v1) | [PDF](https://arxiv.org/pdf/2605.09989v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in robot imitation learning have yielded powerful visuomotor policies capable of manipulating a wide variety of objects directly from monocular visual inputs. However, monocular observations inherently lack reliable depth cues and spatial awareness, which are critical for precise manipulation in cluttered or geometrically complex scenes. To address this limitation, we introduce StereoPolicy, a new visuomotor policy learning framework that directly leverages synchronized stereo im...

</details>

---

### [LoopVLA: Learning Sufficiency in Recurrent Refinement for Vision-Language-Action Models](https://arxiv.org/abs/2605.09948v1)

**Authors:** Boyang Shen, Kaixiang Yang, Hao Wang, Qiuyu Yu, Qiang Xie et al. (7 authors)

**Published:** 2026-05-11 | **Categories:** cs.AI, cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.09948v1) | [PDF](https://arxiv.org/pdf/2605.09948v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models typically treat the deepest representation of a vision-language backbone as universally optimal for action prediction. However, robotic manipulation is composed of many frequent closed-loop spatial adjustments, for which excessive abstraction may waste computation and weaken low-level geometric cues essential for precise control. Existing early-exit strategies attempt to reduce computation by stopping at predefined layers or applying heuristic rules su...

</details>

---

### [Do Vision-Language-Models show human-like logical problem-solving capability in point and click puzzle games?](https://arxiv.org/abs/2605.11223v1)

**Authors:** Dominik Helfenstein, Marco Menner, Maximilian Triebel

**Published:** 2026-05-11 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.11223v1) | [PDF](https://arxiv.org/pdf/2605.11223v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language(-Action) Models (VLMs) are increasingly applied to interactive environments, yet existing benchmarks often overlook the complex physical reasoning required for point-and-click puzzle games. This paper introduces Vision-Language Against The Incredible Machine (VLATIM), a benchmark designed to evaluate human-like logical problem-solving capabilities within the classic physics puzzle game The Incredible Machine 2 (TIM). Unlike existing benchmarks, VLATIM specifically targets the cri...

</details>

---
