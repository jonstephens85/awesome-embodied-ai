# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-13 22:56 UTC

**Papers found:** 19

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

### [PriorZero: Bridging Language Priors and World Models for Decision Making](https://arxiv.org/abs/2605.12289v1)

**Authors:** Junyu Xiong, Yuan Pu, Jia Tang, Yazhe Niu

**Published:** 2026-05-12 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.12289v1) | [PDF](https://arxiv.org/pdf/2605.12289v1.pdf) | [GitHub](https://github.com/opendilab/LightZero)

<details>
<summary>Abstract</summary>

Leveraging the rich world knowledge of Large Language Models (LLMs) to enhance Reinforcement Learning (RL) agents offers a promising path toward general intelligence. However, a fundamental prior-dynamics mismatch hinders existing approaches: static LLM knowledge cannot directly adapt to the complex transition dynamics of long-horizon tasks. Using LLM priors as fixed policies limits exploration diversity, as the prior is blind to environment-specific dynamics; while end-to-end fine-tuning suffer...

</details>

---

### [Closing the Motion Execution Gap: From Semantic Motion Task Constraints to Kinematic Control](https://arxiv.org/abs/2605.12053v1)

**Authors:** Simon Stelter, Vanessa Hassouna, Malte Huerkamp, Michael Beetz

**Published:** 2026-05-12 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.12053v1) | [PDF](https://arxiv.org/pdf/2605.12053v1.pdf) | [GitHub](https://github.com/cram2/cognitive_robot_abstract_machine)

<details>
<summary>Abstract</summary>

This paper addresses the Motion Execution Gap, the disconnect between high-level symbolic task descriptions using semantic constraints and executable robot motions. Motion Statecharts are introduced as an executable symbolic representation for complex motions. They allow the arbitrary arrangement of motion constraints, monitors or nested statecharts in parallel and sequence. World-centric motion specification and generalization across embodiments are enabled through the use of a unified differen...

</details>

---

### [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858v1)

**Authors:** Lingdong Kong, Ao Liang, Tianyi Yan, Hongsi Liu, Wesley Yang et al. (23 authors)

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10858v1) | [PDF](https://arxiv.org/pdf/2605.10858v1.pdf) | [Project Page](at) | [GitHub](https://github.com/worldbench/WorldLens)

<details>
<summary>Abstract</summary>

Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally. Some generate photorealistic textures but violate basic physics; others maintain geometric consistency but fail when subjected to closed-loop planning. This disconnect exposes a critical gap: the field evaluates how real generated worlds appear, but rarely whether they behave realistically. We introduce WorldLens, a unified benchmark that measures world-model fidelity across th...

</details>

---

### [PhyGround: Benchmarking Physical Reasoning in Generative World Models](https://arxiv.org/abs/2605.10806v1)

**Authors:** Juyi Lin, Arash Akbari, Yumei He, Lin Zhao, Haichao Zhang et al. (16 authors)

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.10806v1) | [PDF](https://arxiv.org/pdf/2605.10806v1.pdf) | [Project Page](https://phyground.github.io/)

<details>
<summary>Abstract</summary>

Generative world models are increasingly used for video generation, where learned simulators are expected to capture the physical rules that govern real-world dynamics. However, evaluating whether generated videos actually follow these rules remains challenging. Existing physics-focused video benchmarks have made important progress, but they still face three key challenges, including the coarse evaluation frameworks that hide law-specific failures, response biases and fatigue that undermine the ...

</details>

---

### [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564v1)

**Authors:** Lingjun Zhang, Changjie Wu, Linzhe Shi, Jiangyang Li, Jiaxin Liu et al. (9 authors)

**Published:** 2026-05-11 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10564v1) | [PDF](https://arxiv.org/pdf/2605.10564v1.pdf) | [GitHub](https://github.com/hotdogcheesewhite/DeepSight)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions. However, the reasoning mechanisms employed in most methods are direct adaptations from general domains, lacking in-depth exploration tailored to autonomous driving scenarios, particularly within visual reasoning modules. In this paper, we propose a driving world model that perfor...

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

### [Why Conclusions Diverge from the Same Observations: Formalizing World-Model Non-Identifiability via an Inference](https://arxiv.org/abs/2605.12255v1)

**Authors:** Toru Takahashi

**Published:** 2026-05-12 | **Categories:** cs.AI, cs.CY, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.12255v1) | [PDF](https://arxiv.org/pdf/2605.12255v1.pdf)

<details>
<summary>Abstract</summary>

When people share the same documents and observations yet reach different conclusions, the disagreement often shifts into a judgment that the other party is cognitively defective, irrational, or acting in bad faith. This paper argues that such divergence is better described as a form of non-identifiability inherent in inference and learning, rather than as a defect of the other party. We organize the phenomenon into two levels: (i) $θ$-level non-identifiability, where conclusions diverge under t...

</details>

---

### [Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics](https://arxiv.org/abs/2605.12178v1)

**Authors:** Jishnu Sethumadhavan Nair, Patrice Bechard, Rishabh Maheshwary, Surajit Dasgupta, Sravan Ramachandran et al. (17 authors)

**Published:** 2026-05-12 | **Categories:** cs.AI, cs.CL, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.12178v1) | [PDF](https://arxiv.org/pdf/2605.12178v1.pdf)

<details>
<summary>Abstract</summary>

World models enable agents to anticipate the effects of their actions by internalizing environment dynamics. In enterprise systems, however, these dynamics are often defined by tenant-specific business logic that varies across deployments and evolves over time, making models trained on historical transitions brittle under deployment shift. We ask a question the world-models literature has not addressed: when the rules can be read at inference time, does an agent still need to learn them? We argu...

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

### [HorizonDrive: Self-Corrective Autoregressive World Model for Long-horizon Driving Simulation](https://arxiv.org/abs/2605.11596v1)

**Authors:** Conglang Zhang, Yifan Zhan, Qingjie Wang, Zhanpeng Ouyang, Yu Li et al. (13 authors)

**Published:** 2026-05-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.11596v1) | [PDF](https://arxiv.org/pdf/2605.11596v1.pdf)

<details>
<summary>Abstract</summary>

Closed-loop driving simulation requires real-time interaction beyond short offline clips, pushing current driving world models toward autoregressive (AR) rollout. Existing AR distillation approaches typically rely on frame sinks or student-side degradation training. The former transfers poorly to driving due to fast ego-motion and rapid scene changes, while the latter remains bounded by the teacher's single-pass output length and thus provides only a limited supervision horizon. A natural questi...

</details>

---

### [The DAWN of World-Action Interactive Models](https://arxiv.org/abs/2605.11550v1)

**Authors:** Hongbo Lu, Liang Yao, Chenghao He, Haoyu Wang, Xiang Gu et al. (9 authors)

**Published:** 2026-05-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.11550v1) | [PDF](https://arxiv.org/pdf/2605.11550v1.pdf)

<details>
<summary>Abstract</summary>

A plausible scene evolution depends on the maneuver being considered, while a good maneuver depends on how the scene may evolve. Existing World Action Models (WAMs) largely miss this reciprocity, treating world prediction and action generation as either isolated parallel branches or rigid predict-then-plan pipelines. We formalize this perspective as World-Action Interactive Models (WAIMs), and instantiate it in autonomous driving with \textbf{DAWN} (\textbf{D}enoising \textbf{A}ctions and \textb...

</details>

---

### [3D-Belief: Embodied Belief Inference via Generative 3D World Modeling](https://arxiv.org/abs/2605.11367v1)

**Authors:** Yifan Yin, Zehao Wen, Jieneng Chen, Zehan Zheng, Nanru Dai et al. (13 authors)

**Published:** 2026-05-12 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.11367v1) | [PDF](https://arxiv.org/pdf/2605.11367v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in visual generative models have highlighted the promise of learning generative world models. However, most existing approaches frame world modeling as novel-view synthesis or future-frame prediction, emphasizing visual realism rather than the structured uncertainty required by embodied agents acting under partial observability. In this work, we propose a different perspective: world modeling as embodied belief inference in 3D space. From this view, a world model should not merel...

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

### [Position: Life-Logging Video Streams Make the Privacy-Utility Trade-off Inevitable](https://arxiv.org/abs/2605.10404v1)

**Authors:** Tianyuan Zou, Liang Yue, Yang Liu, Ya-Qin Zhang, Sijie Cheng

**Published:** 2026-05-11 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.10404v1) | [PDF](https://arxiv.org/pdf/2605.10404v1.pdf)

<details>
<summary>Abstract</summary>

With the growing prevalence of always-on hardware such as smart glasses, body cameras, and home security systems, life-logging visual sensing is becoming inevitable, forming the backbone of persistent, always-on AI systems. Meanwhile, recent advances in proactive agents and world models signal a fundamental shift from episodic, prompt-driven tools to next-generation AI systems that continuously perceive and react to the physical world. Although life-logging video streams can substantially improv...

</details>

---

### [How Mobile World Model Guides GUI Agents?](https://arxiv.org/abs/2605.10347v1)

**Authors:** Weikai Xu, Kun Huang, Yunren Feng, Jiaxing Li, Yuhan Chen et al. (13 authors)

**Published:** 2026-05-11 | **Categories:** cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.10347v1) | [PDF](https://arxiv.org/pdf/2605.10347v1.pdf)

<details>
<summary>Abstract</summary>

Recent advances in vision-language models have enabled mobile GUI agents to perceive visual interfaces and execute user instructions, but reliable prediction of action consequences remains critical for long-horizon and high-risk interactions. Existing mobile world models provide either text-based or image-based future states, yet it remains unclear which representation is useful, whether generated rollouts can replace real environments, and how test-time guidance helps agents of different streng...

</details>

---

### [Data-Asymmetric Latent Imagination and Reranking for 3D Robotic Imitation Learning](https://arxiv.org/abs/2605.10166v1)

**Authors:** Lianghao Luo, Xizhou Bu, Ruyan Liu, Qingqiu Huang, Chufeng Tang et al. (8 authors)

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.10166v1) | [PDF](https://arxiv.org/pdf/2605.10166v1.pdf)

<details>
<summary>Abstract</summary>

Robotic imitation learning typically assumes access to optimal demonstrations, yet real-world data collection often yields suboptimal, exploratory, or even failed trajectories. Discarding such data wastes valuable information about environment dynamics and failure modes, which can instead be leveraged to improve decision-making. While 3D policies reduce reliance on high-quality demonstrations through strong spatial generalization, they still require large-scale data to achieve high task success....

</details>

---

### [Network-Efficient World Model Token Streaming](https://arxiv.org/abs/2605.09886v1)

**Authors:** Shatadal Mishra, Ahmadreza Moradipari, Nejib Ammar

**Published:** 2026-05-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.09886v1) | [PDF](https://arxiv.org/pdf/2605.09886v1.pdf)

<details>
<summary>Abstract</summary>

Generative driving world models rely on compact latent state representations that must be efficiently transmitted and synchronized across distributed compute and connected vehicles. We study network-efficient streaming of a discrete world model state, where a stride-16 VQ-U-Net tokenizer (codebook size 8,192) maps each 288x512 frame to an 18x32 grid of token IDs (576 tokens/frame), equivalent to 936 bytes/frame under fixed-length coding. We consider a keyframe--delta protocol under strict per-me...

</details>

---
