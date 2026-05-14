# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-14 17:49 UTC

**Papers found:** 29

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [FrameSkip: Learning from Fewer but More Informative Frames in VLA Training](https://arxiv.org/abs/2605.13757v1)

**Authors:** Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei et al. (11 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.13757v1) | [PDF](https://arxiv.org/pdf/2605.13757v1.pdf) | [GitHub](https://github.com/ZGC-EmbodyAI/FrameSkip)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies are commonly trained from dense robot demonstration trajectories, often collected through teleoperation, by sampling every recorded frame as if it provided equally useful supervision. We argue that this convention creates a temporal supervision imbalance: long low-change segments dominate the training stream, while manipulation-critical transitions such as alignment, contact, grasping, and release appear only sparsely. We introduce FrameSkip, a data-layer fr...

</details>

---

### [Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models](https://arxiv.org/abs/2605.13632v1)

**Authors:** Yiran Ling, Qing Lian, Jinghang Li, Qing Jiang, Tianming Zhang et al. (9 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.13632v1) | [PDF](https://arxiv.org/pdf/2605.13632v1.pdf) | [Project Page](https://signalispupupu.github.io/GTA-VLA_ProjPage/)

<details>
<summary>Abstract</summary>

In this paper, we propose GTA-VLA(Guide, Think, Act), an interactive Vision-Language-Action (VLA) framework that enables spatially steerable embodied reasoning by allowing users to guide robot policies with explicit visual cues. Existing VLA models learn a direct "Sense-to-Act" mapping from multimodal observations to robot actions. While effective within the training distribution, such tightly coupled policies are brittle under out-of-domain (OOD) shifts and difficult to correct when failures oc...

</details>

---

### [What Limits Vision-and-Language Navigation ?](https://arxiv.org/abs/2605.13328v1)

**Authors:** Yunheng Wang, Yuetong Fang, Taowen Wang, Lusong Li, Kun Liu et al. (12 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.13328v1) | [PDF](https://arxiv.org/pdf/2605.13328v1.pdf) | [Project Page](https://yunheng-wang.github.io/stereonav-public.github.io)

<details>
<summary>Abstract</summary>

Vision-and-Language Navigation (VLN) is a cornerstone of embodied intelligence. However, current agents often suffer from significant performance degradation when transitioning from simulation to real-world deployment, primarily due to perceptual instability (e.g., lighting variations and motion blur) and under-specified instructions. While existing methods attempt to bridge this gap by scaling up model size and training data, we argue that the bottleneck lies in the lack of robust spatial groun...

</details>

---

### [Driving Intents Amplify Planning-Oriented Reinforcement Learning](https://arxiv.org/abs/2605.12625v1)

**Authors:** Hengtong Lu, Victor Shea-Jay Huang, Chengmin Yang, Pengfei Jing, Jifeng Dai et al. (7 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.12625v1) | [PDF](https://arxiv.org/pdf/2605.12625v1.pdf) | [Project Page](https://mind-omni.github.io/)

<details>
<summary>Abstract</summary>

Continuous-action policies trained on a single demonstrated trajectory per scene suffer from mode collapse: samples cluster around the demonstrated maneuver and the policy cannot represent semantically distinct alternatives. Under preference-based evaluation, this caps best-of-N performance -- even oracle selection cannot recover what the sampling distribution does not contain. We introduce DIAL, a two-stage Driving-Intent-Amplified reinforcement Learning framework for preference-aligned continu...

</details>

---

### [MindVLA-U1: VLA Beats VA with Unified Streaming Architecture for Autonomous Driving](https://arxiv.org/abs/2605.12624v1)

**Authors:** Yuzhou Huang, Benjin Zhu, Hengtong Lu, Victor Shea-Jay Huang, Haiming Zhang et al. (9 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.12624v1) | [PDF](https://arxiv.org/pdf/2605.12624v1.pdf) | [Project Page](https://mind-omni.github.io/)

<details>
<summary>Abstract</summary>

Autonomous driving has progressed from modular pipelines toward end-to-end unification, and Vision-Language-Action (VLA) models are a natural extension of this journey beyond Vision-to-Action (VA). In practice, driving VLAs have often trailed VA on planning quality, suggesting that the difficulty is not simply model scale but the interface through which semantic reasoning, temporal context, and continuous control are combined. We argue that this gap reflects how VLA has been built -- as isolated...

</details>

---

### [Action Emergence from Streaming Intent](https://arxiv.org/abs/2605.12622v1)

**Authors:** Pengfei Jing, Victor Shea-Jay Huang, Hengtong Lu, Jifeng Dai, Xie Yan et al. (6 authors)

**Published:** 2026-05-12 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.12622v1) | [PDF](https://arxiv.org/pdf/2605.12622v1.pdf) | [Project Page](https://mind-omni.github.io/)

<details>
<summary>Abstract</summary>

We formalize action emergence as a target capability for end-to-end autonomous driving: the ability to generate physically feasible, semantically appropriate, and safety-compliant actions in arbitrary, long-tail traffic scenes through scene-conditioned reasoning rather than retrieval or interpolation of learned scene-action mappings. We show that previous paradigms cannot deliver action emergence: autoregressive trajectory decoders collapse the inherently multimodal future into a single averaged...

</details>

---

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

## Other Recent Papers

### [Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs](https://arxiv.org/abs/2605.13778v1)

**Authors:** Jiahui Niu, Kefan Gu, Yucheng Zhao, Shengwen Liang, Tiancai Wang et al. (8 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.13778v1) | [PDF](https://arxiv.org/pdf/2605.13778v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion-based vision-language-action models (dVLAs) are promising for embodied intelligence but are fundamentally limited in real-time deployment by the high latency of full inference. We propose Realtime-VLA FLASH, a speculative inference framework that eliminates most full inference calls during replanning by introducing a lightweight draft model with parallel verification via the main model's Action Expert and a phase-aware fallback mechanism that reverts to the full inference pipeline when...

</details>

---

### [AttenA+: Rectifying Action Inequality in Robotic Foundation Models](https://arxiv.org/abs/2605.13548v1)

**Authors:** Daojie Peng, Fulong Ma, Jiahang Cao, Qiang Zhang, Xupeng Xie et al. (10 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.13548v1) | [PDF](https://arxiv.org/pdf/2605.13548v1.pdf)

<details>
<summary>Abstract</summary>

Existing robotic foundation models, while powerful, are predicated on an implicit assumption of temporal homogeneity: treating all actions as equally informative during optimization. This "flat" training paradigm, inherited from language modeling, remains indifferent to the underlying physical hierarchy of manipulation. In reality, robot trajectories are fundamentally heterogeneous, where low-velocity segments often dictate task success through precision-demanding interactions, while high-veloci...

</details>

---

### [RotVLA: Rotational Latent Action for Vision-Language-Action Model](https://arxiv.org/abs/2605.13403v1)

**Authors:** Qiwei Li, Xicheng Gong, Xinghang Li, Peiyan Li, Quanyun Zhou et al. (8 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.13403v1) | [PDF](https://arxiv.org/pdf/2605.13403v1.pdf)

<details>
<summary>Abstract</summary>

Latent Action Models (LAMs) have emerged as an effective paradigm for handling heterogeneous datasets during Vision-Language-Action (VLA) model pretraining, offering a unified action space across embodiments. However, existing LAMs often rely on discrete quantization encode and decode pipelines, which can lead to trivial frame reconstruction behavior, limited representational capacity, and a lack of physically meaningful structure. We introduce RotVLA, a VLA framework built on a continuous rotat...

</details>

---

### [BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning](https://arxiv.org/abs/2605.13382v1)

**Authors:** Ruiheng Wang, Shuanghao Bai, Haoran Zhang, Badong Chen, Xiangyu Xu

**Published:** 2026-05-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.13382v1) | [PDF](https://arxiv.org/pdf/2605.13382v1.pdf)

<details>
<summary>Abstract</summary>

While autoregressive (AR) Vision-Language-Action (VLA) models have demonstrated formidable reasoning capabilities in robotic tasks, their sequential decoding process often incurs high inference latency and may amplify error accumulation during long-horizon execution. Discrete Diffusion Language Models (dLLMs) provide a promising alternative through parallel token refinement, but their practical deployment in robotics remains limited by repeated denoising function evaluations (NFEs) and the diffi...

</details>

---

### [D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models](https://arxiv.org/abs/2605.13276v1)

**Authors:** Yucheng Guo, Yongjian Guo, Zhong Guan, Wen Huang, Haoran Sun et al. (12 authors)

**Published:** 2026-05-13 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.13276v1) | [PDF](https://arxiv.org/pdf/2605.13276v1.pdf)

<details>
<summary>Abstract</summary>

The rapid evolution of Embodied AI has enabled Vision-Language-Action (VLA) models to excel in multimodal perception and task execution. However, applying Reinforcement Learning (RL) to these massive models in large-scale distributed environments faces severe systemic bottlenecks, primarily due to the resource conflict between high-fidelity physical simulation and the intensive VRAM/bandwidth demands of deep learning. This conflict often leaves overall throughput constrained by execution-phase i...

</details>

---

### [Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models](https://arxiv.org/abs/2605.13119v1)

**Authors:** Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding et al. (8 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.13119v1) | [PDF](https://arxiv.org/pdf/2605.13119v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are effective robot action executors, but they remain limited on long-horizon tasks due to the dual burden of extended closed-loop planning and diverse physical operations. We therefore propose VLAs-as-Tools, a strategy that distributes this burden across a high-level vision language model (VLM) agent for temporal reasoning and a family of specialized VLA tools for diverse local physical operations. The VLM handles scene analysis, global planning, and recovery...

</details>

---

### [What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models](https://arxiv.org/abs/2605.13105v1)

**Authors:** Yuanfang Peng, Jingjing Fu, Chuheng Zhang, Li Zhao, Jiang Bian et al. (9 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.13105v1) | [PDF](https://arxiv.org/pdf/2605.13105v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) fine-tuning has shown promise for Vision-Language-Action (VLA) models in robotic manipulation, but deployment-time visual shifts pose practical challenges. A key difficulty is that standard task rewards supervise task success, but offer limited guidance on whether a visual change is task-irrelevant or changes the behavior required for manipulation. We propose PAIR-VLA (Paired Action Invariance & Sensitivity for Visually Robust VLA), an RL fine-tuning framework to addr...

</details>

---

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
