# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-21 22:57 UTC

**Papers found:** 13

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Q-ARVD: Quantizing Autoregressive Video Diffusion Models](https://arxiv.org/abs/2605.21072v1)

**Authors:** Siao Tang, Xinyin Ma, Gongfan Fang, Xingyi Yang, Xinchao Wang

**Published:** 2026-05-20 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.21072v1) | [PDF](https://arxiv.org/pdf/2605.21072v1.pdf) | [GitHub](https://github.com/tsa18/Q-ARVD)

<details>
<summary>Abstract</summary>

Autoregressive video diffusion models (ARVDs) have emerged as a promising architecture for streaming video generation, paving the way for real-time interactive video generation and world modeling. Despite their potential, the substantial inference cost of ARVDs remains a major obstacle to practical deployment, making model quantization a natural direction for improving efficiency. However, quantization for ARVDs remains largely unexplored. Our empirical analysis shows that directly applying exis...

</details>

---

### [RoHIL: Robust Human-in-the-Loop Robotic Reinforcement Learning Against Illumination Variations](https://arxiv.org/abs/2605.19924v1)

**Authors:** Shuoqin Zhang, Yixin Xiong, Xiru Gao, Kai Liu, Ke Wang et al. (7 authors)

**Published:** 2026-05-19 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.19924v1) | [PDF](https://arxiv.org/pdf/2605.19924v1.pdf) | [Project Page](https://anonymous4365.github.io/RoHIL/)

<details>
<summary>Abstract</summary>

Human-in-the-loop reinforcement learning systems achieve near-perfect success on the workstation where they are trained, but collapse when the same robot is moved to a workstation a few meters away due to shifts in the visual input distribution caused by new lamp positions and window light. Re-collecting demonstrations and re-running HIL on every workstation is incompatible with deployment, and naively fine-tuning on shifted-light data triggers catastrophic forgetting of the source workstation. ...

</details>

---

## Other Recent Papers

### [Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/2605.21139v1)

**Authors:** Yang Wu, Qiang Meng, Zhaojiang Liu, Youquan Liu, Jian Yang et al. (6 authors)

**Published:** 2026-05-20 | **Categories:** cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.21139v1) | [PDF](https://arxiv.org/pdf/2605.21139v1.pdf)

<details>
<summary>Abstract</summary>

Current end-to-end autonomous driving models are fundamentally constrained by the behavioral cloning ceiling of imitation learning. While reinforcement learning offers a path to smarter autonomy, it demands two missing pieces of infrastructure: (1) a cognitive foundation that understands traffic semantics and driving intent, and (2) a foresighted physical environment that can anticipate the consequences of candidate actions. To this end, we propose CoPhy, a CognitivePhysical reinforcement learni...

</details>

---

### [Anomaly-Informed Confidence Calibration for Vision-Based Safety Prediction](https://arxiv.org/abs/2605.21109v1)

**Authors:** Zhenjiang Mao, Jiawen Wu, Gabriel Wagner, Zhongzheng Zhang, Ivan Ruchkin

**Published:** 2026-05-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.21109v1) | [PDF](https://arxiv.org/pdf/2605.21109v1.pdf)

<details>
<summary>Abstract</summary>

Reliable confidence estimates are important for safely deploying vision-based controllers in autonomous racing, where safety predictions must be derived from camera images, yet modern predictors become dangerously overconfident under test-time distribution shifts. We identify a critical perception-dynamics gap in existing anomaly signals: widely used scores, such as autoencoder reconstruction error, capture visual corruptions but miss dynamics anomalies (e.g., actuation bias, latency), where ima...

</details>

---

### [Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation](https://arxiv.org/abs/2605.20811v1)

**Authors:** Jingyang He, Guangrun Li, Jieyu Zhang, Chengkai Hou, Zhengping Che et al. (6 authors)

**Published:** 2026-05-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.20811v1) | [PDF](https://arxiv.org/pdf/2605.20811v1.pdf)

<details>
<summary>Abstract</summary>

Robotic imitation learning is often treated as reproducing demonstrated actions, but actions are inherently embodiment-specific. When demonstrations come from humans or robots with different morphology, kinematics, or action spaces, this action-centric view requires shared action spaces, heuristic retargeting, or large-scale multi-embodiment co-training. We instead view demonstrations as implicit specifications of future goals: the target agent should infer what state the demonstrator is trying ...

</details>

---

### [GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation](https://arxiv.org/abs/2605.20752v1)

**Authors:** Zijian Zhang, Yuqing Jiang, Qian Cheng, Si Liu, Ding Zhao et al. (8 authors)

**Published:** 2026-05-20 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.20752v1) | [PDF](https://arxiv.org/pdf/2605.20752v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have advanced language-conditioned robotic manipulation by transferring semantic priors from pretrained vision-language models to action generation. Yet, standard action-imitation training often provides limited explicit supervision for 3D geometry, dense visual structure, and short-horizon environment evolution, which are critical for physically precise manipulation. We introduce \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in that tu...

</details>

---

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
