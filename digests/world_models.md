# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-20 18:16 UTC

**Papers found:** 18

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [RoHIL: Robust Human-in-the-Loop Robotic Reinforcement Learning Against Illumination Variations](https://arxiv.org/abs/2605.19924v1)

**Authors:** Shuoqin Zhang, Yixin Xiong, Xiru Gao, Kai Liu, Ke Wang et al. (7 authors)

**Published:** 2026-05-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.19924v1) | [PDF](https://arxiv.org/pdf/2605.19924v1.pdf) | [Project Page](https://anonymous4365.github.io/RoHIL/)

<details>
<summary>Abstract</summary>

Human-in-the-loop reinforcement learning systems achieve near-perfect success on the workstation where they are trained, but collapse when the same robot is moved to a workstation a few meters away due to shifts in the visual input distribution caused by new lamp positions and window light. Re-collecting demonstrations and re-running HIL on every workstation is incompatible with deployment, and naively fine-tuning on shifted-light data triggers catastrophic forgetting of the source workstation. ...

</details>

---

### [PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis](https://arxiv.org/abs/2605.17916v2)

**Authors:** Jinrang Jia, Zhenjia Li, Yijiang Hu, Yifeng Shi

**Published:** 2026-05-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.17916v2) | [PDF](https://arxiv.org/pdf/2605.17916v2.pdf) | [Project Page](https://jjrcn.github.io/PanoWorld-project-home/)

<details>
<summary>Abstract</summary>

Generating a consistent whole-house VR tour from a floorplan and style reference requires both photorealistic panoramas and cross-view spatial coherence. Pure 2D generators produce appealing single panoramas but re-imagine geometry and materials when the viewpoint changes, whereas monolithic 3D generation becomes expensive and loses fine texture at multi-room scale. We introduce PanoWorld, a generative spatial world model that treats whole-house synthesis as autoregressive generation of node-bas...

</details>

---

## Other Recent Papers

### [World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks](https://arxiv.org/abs/2605.19957v1)

**Authors:** Zuyao Lin, Jianhui Zhang, Peidong Jia, Xiaoguang Zhao, Shanghang Zhang et al. (6 authors)

**Published:** 2026-05-19 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.19957v1) | [PDF](https://arxiv.org/pdf/2605.19957v1.pdf)

<details>
<summary>Abstract</summary>

World models are widely explored in embodied intelligence, yet they typically predict distinct evolutions of the world and the ego within a single stream, where the world captures persistent instruction-agnostic scene regularities and the ego captures robot-centric instruction-conditioned dynamics. This world-ego entanglement leads to a degradation in long-horizon embodied scenarios, particularly in hybrid tasks with interleaved navigation and manipulation behaviors. In this paper, we introduce ...

</details>

---

### [AffectVerse: Emotional World Models for Multimodal Affective Computing](https://arxiv.org/abs/2605.19950v1)

**Authors:** Bo Zhao, Fanghua Ye, Yixin Ji, Sicheng Zhao, Xiaojiang Peng et al. (6 authors)

**Published:** 2026-05-19 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.19950v1) | [PDF](https://arxiv.org/pdf/2605.19950v1.pdf)

<details>
<summary>Abstract</summary>

Humans infer emotions by integrating observed multimodal cues with expectations about how affective states may unfold. Existing multimodal large language models (MLLMs), however, often treat emotion recognition as static fusion over complete audiovisual-text inputs, leaving affective dynamics implicit. We propose AffectVerse, a Qwen2.5-Omni-based model equipped with an Emotion World Module (EWM), an action-free representation-level module for short-horizon latent affective prediction. \rev{EWM c...

</details>

---

### [HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models](https://arxiv.org/abs/2605.19631v1)

**Authors:** Hoonhee Cho, Giwon Lee, Jae-Young Kang, Hyemin Yang, Heejun Park et al. (6 authors)

**Published:** 2026-05-19 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.19631v1) | [PDF](https://arxiv.org/pdf/2605.19631v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving has emerged as a compelling alternative to traditional modular pipelines by directly mapping raw sensor data to driving actions. While recent approaches achieve strong performance on single-domain datasets, their performance degrades significantly when trained jointly across multiple heterogeneous domains. In practice, however, autonomous systems must operate across diverse environments with heterogeneous distributions, including different cities, sensor configurati...

</details>

---

### [FlyMirage: A Fully Automated Generation Pipeline for Diverse and Scalable UAV Flight Data via Generative World Model](https://arxiv.org/abs/2605.19600v1)

**Authors:** Jinhan Li, Xijie Huang, Zhaoqi Wang, Yijin Wang, Weiqi Ge et al. (10 authors)

**Published:** 2026-05-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.19600v1) | [PDF](https://arxiv.org/pdf/2605.19600v1.pdf)

<details>
<summary>Abstract</summary>

In the field of Vision-Language Navigation (VLN), aerial datasets remain limited in their ability to combine scale, diversity, and realism, often relying on either costly real-world scenes or visually limited simulations. To address these challenges, we introduce FlyMirage, a highly scalable and fully automated data generation pipeline for aerial VLN. Our approach leverages large language models (LLM) as an environment designer to promote scene diversity, paired with a generative world model tha...

</details>

---

### [HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models](https://arxiv.org/abs/2605.19341v1)

**Authors:** Emmy Liu, Varun Gangal, Michael Yu, Zhuofu Tao, Karan Singh et al. (7 authors)

**Published:** 2026-05-19 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.19341v1) | [PDF](https://arxiv.org/pdf/2605.19341v1.pdf)

<details>
<summary>Abstract</summary>

Hallucination remains a central failure mode of large language models, but existing benchmarks operationalize it inconsistently across summarization, question answering, retrieval-augmented generation, and agentic interaction. This fragmentation makes it unclear whether a mitigation that works in one setting reduces hallucinations across contexts. Current benchmarks either require human annotation and fixed references that may be memorized, or rely on observations in settings that are difficult ...

</details>

---

### [SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution](https://arxiv.org/abs/2605.19319v1)

**Authors:** Yiren Song, Yihan Wang, Xiyao Deng, Zhuoran Yan, Mike Zheng Shou

**Published:** 2026-05-19 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.19319v1) | [PDF](https://arxiv.org/pdf/2605.19319v1.pdf)

<details>
<summary>Abstract</summary>

Visual prediction has emerged as a promising paradigm for embodied control, where future observations are generated and then translated into actions. However, dense video generation is computationally expensive and often unnecessary for many manipulation tasks, whose progress can be summarized by a small number of task-relevant visual states. In this work, we study whether image editing models can serve as sparse visual world models for robot manipulation by predicting task-level future states w...

</details>

---

### [PhyWorld: Physics-Faithful World Model for Video Generation](https://arxiv.org/abs/2605.19242v1)

**Authors:** Pu Zhao, Juyi Lin, Timothy Rupprecht, Arash Akbari, Chence Yang et al. (13 authors)

**Published:** 2026-05-19 | **Categories:** cs.CV, cs.AI, cs.ET

**Links:** [arXiv](https://arxiv.org/abs/2605.19242v1) | [PDF](https://arxiv.org/pdf/2605.19242v1.pdf)

<details>
<summary>Abstract</summary>

World simulators can provide safe and scalable environments for training Physical AI systems before real-world deployment. Large video generation models are emerging as a promising basis for such simulators because they can generate diverse and realistic visual futures. However, using them as world simulators requires physically faithful video continuations, namely, generated videos that preserve the physical state implied by the conditioning input, and evolve in ways consistent with basic physi...

</details>

---

### [Actionable World Representation](https://arxiv.org/abs/2605.18743v1)

**Authors:** Kunqi Xu, Jitao Li, Jianglong Ye, Tianshu Tang, Isabella Liu et al. (7 authors)

**Published:** 2026-05-18 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.18743v1) | [PDF](https://arxiv.org/pdf/2605.18743v1.pdf)

<details>
<summary>Abstract</summary>

Inspired by the emergent behaviors in large language models that generalized human intelligence, the research community is pursuing similar emergent capabilities within world models, with a emphasis on modeling the physical world. Within the scope of physical world model, objects are the fundamental primitives that constitute physical reality. From humans to computers, nearly everything we interact with is an object. These objects are rarely static; they are actionable entities with varying stat...

</details>

---

### [Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction](https://arxiv.org/abs/2605.18729v1)

**Authors:** Nga Teng Chan, Yi Zhang, Yechi Liu, Renwen Cui, Fanhu Zeng et al. (12 authors)

**Published:** 2026-05-18 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.18729v1) | [PDF](https://arxiv.org/pdf/2605.18729v1.pdf)

<details>
<summary>Abstract</summary>

The ability to navigate and interact with complex environments is central to real-world embodied agents, yet navigation in unseen environments remains challenging due to "experiential amnesia," where existing trajectory-driven or reactive policies fail to synthesize generalizable strategies from past interactions. We propose Robo-Cortex, a self-evolving framework that enables robots to autonomously induce navigation heuristics and refine cognitive strategies through a continuous reflection-adapt...

</details>

---

### [Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models](https://arxiv.org/abs/2605.18601v1)

**Authors:** Shangwen Zhu, Qianyu Peng, Zhao Pu, Zhilei Shu, Xiangrui Ke et al. (14 authors)

**Published:** 2026-05-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.18601v1) | [PDF](https://arxiv.org/pdf/2605.18601v1.pdf)

<details>
<summary>Abstract</summary>

Modern interactive video world models have achieved impressive visual fidelity, yet lack fine-grained multi-entity control and cross-entity, cross-world generalization. We trace this gap to the action interface: standard control protocols (e.g. animation IDs, device inputs, scene-level captions) bind action semantics to specific entities or engines at design time. We propose natural language as the interface to unlock expressiveness that no prior interface can achieve, and we present Incantation...

</details>

---

### [Improved Baselines with Representation Autoencoders](https://arxiv.org/abs/2605.18324v1)

**Authors:** Jaskirat Singh, Boyang Zheng, Zongze Wu, Richard Zhang, Eli Shechtman et al. (6 authors)

**Published:** 2026-05-18 | **Categories:** cs.CV, cs.AI, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2605.18324v1) | [PDF](https://arxiv.org/pdf/2605.18324v1.pdf)

<details>
<summary>Abstract</summary>

Representation Autoencoders (RAE) replace traditional VAE with pretrained vision encoders. In this paper, we systematically investigate several design choices and find three insights which simplify and improve RAE. First, we study a generalized formulation where the representation is defined as sum of the last k encoder layers rather than solely the final layer. This simple change greatly improves reconstruction without encoder finetuning or specialized data (e.g., text, faces). Second, we study...

</details>

---

### [PH-Dreamer: A Physics-Driven World Model via Port-Hamiltonian Generative Dynamics](https://arxiv.org/abs/2605.18303v1)

**Authors:** Xueyu Luan, Chenwei Shi

**Published:** 2026-05-18 | **Categories:** cs.LG, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.18303v1) | [PDF](https://arxiv.org/pdf/2605.18303v1.pdf)

<details>
<summary>Abstract</summary>

World models built on recurrent state space architectures enable efficient latent imagination, yet remain physically unstructured, producing dynamics that violate conservation and dissipative principles. We introduce a unified Port-Hamiltonian framework that remedies this through three synergistic mechanisms. First, we embed implicit physical priors into recurrent transitions by modeling projected latent evolution as action controlled energy routing governed by flow and dissipation, biasing the ...

</details>

---

### [Scalable Environments Drive Generalizable Agents](https://arxiv.org/abs/2605.18181v1)

**Authors:** Jiayi Zhang, Fanqi Kong, Guibin Zhang, Maojia Song, Zhaoyang Yu et al. (10 authors)

**Published:** 2026-05-18 | **Categories:** cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.18181v1) | [PDF](https://arxiv.org/pdf/2605.18181v1.pdf)

<details>
<summary>Abstract</summary>

Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when unde...

</details>

---

### [Xiaomi EV World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving](https://arxiv.org/abs/2605.18137v2)

**Authors:** Lijun Zhou, Hongcheng Luo, Zhenxin Zhu, Cheng Chi, Mingfei Tu et al. (37 authors)

**Published:** 2026-05-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.18137v2) | [PDF](https://arxiv.org/pdf/2605.18137v2.pdf)

<details>
<summary>Abstract</summary>

This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high...

</details>

---

### [AdaptiveLoad: Towards Efficient Video Diffusion Transformer Training](https://arxiv.org/abs/2605.17923v1)

**Authors:** Yucheng Guo, Yongjian Guo, Zhong Guan, Haoran Sun, Wen Huang et al. (9 authors)

**Published:** 2026-05-18 | **Categories:** cs.DC, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.17923v1) | [PDF](https://arxiv.org/pdf/2605.17923v1.pdf)

<details>
<summary>Abstract</summary>

In video generation models, particularly world models, training large-scale video diffusion Transformers (such as DiT and MMDiT) poses significant computational challenges due to the extreme variance in sequence lengths within mixed-mode datasets. Existing bucket-based data loading strategies typically rely on "equal token length" constraints. This approach fails to account for the quadratic complexity of self-attention mechanisms, leading to severe load imbalance and underutilization of GPU res...

</details>

---

### [WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform](https://arxiv.org/abs/2605.17912v1)

**Authors:** Yu Shang, Yinzhou Tang, Yiding Ma, Zhuohang Li, Lei Jin et al. (25 authors)

**Published:** 2026-05-18 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.17912v1) | [PDF](https://arxiv.org/pdf/2605.17912v1.pdf)

<details>
<summary>Abstract</summary>

World models have emerged as a central paradigm for embodied intelligence, enabling agents to predict action-conditioned future and reason about environmental dynamics. However, existing embodied world model benchmarks are still largely confined to vision-only prediction, offline embodied applications, and simulator-based evaluation, making them insufficient for assessing increasingly comprehensive world models. In this work, we introduce WorldArena 2.0, an expanded benchmark that systematically...

</details>

---
