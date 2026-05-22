# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-22 22:49 UTC

**Papers found:** 12

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Efficient Agentic Reasoning Through Self-Regulated Simulative Planning](https://arxiv.org/abs/2605.22138v1)

**Authors:** Mingkai Deng, Jinyu Hou, Lara Sá Neves, Varad Pimpalkhute, Taylor W. Killian et al. (7 authors)

**Published:** 2026-05-21 | **Categories:** cs.AI, cs.CL, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.22138v1) | [PDF](https://arxiv.org/pdf/2605.22138v1.pdf) | [GitHub](https://github.com/sailing-lab/sr2am)

<details>
<summary>Abstract</summary>

How should an agent decide when and how to plan? A dominant approach builds agents as reactive policies with adaptive computation (e.g., chain-of-thought), trained end-to-end expecting planning to emerge implicitly. Without control over the presence, structure, or horizon of planning, these systems dramatically increase reasoning length, yielding inefficient token use without reliable accuracy gains. We argue efficient agentic reasoning benefits from decomposing decision-making into three system...

</details>

---

### [Q-ARVD: Quantizing Autoregressive Video Diffusion Models](https://arxiv.org/abs/2605.21072v1)

**Authors:** Siao Tang, Xinyin Ma, Gongfan Fang, Xingyi Yang, Xinchao Wang

**Published:** 2026-05-20 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.21072v1) | [PDF](https://arxiv.org/pdf/2605.21072v1.pdf) | [GitHub](https://github.com/tsa18/Q-ARVD)

<details>
<summary>Abstract</summary>

Autoregressive video diffusion models (ARVDs) have emerged as a promising architecture for streaming video generation, paving the way for real-time interactive video generation and world modeling. Despite their potential, the substantial inference cost of ARVDs remains a major obstacle to practical deployment, making model quantization a natural direction for improving efficiency. However, quantization for ARVDs remains largely unexplored. Our empirical analysis shows that directly applying exis...

</details>

---

## Other Recent Papers

### [Steins;Gate Drive: Semantic Safety Arbitration over Structured Futures for Latency-Decoupled LLM Planning](https://arxiv.org/abs/2605.22456v1)

**Authors:** Anjie Qiu, Hans D. Schotten

**Published:** 2026-05-21 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.22456v1) | [PDF](https://arxiv.org/pdf/2605.22456v1.pdf)

<details>
<summary>Abstract</summary>

Cloud-hosted LLM driver agents provide useful semantic judgments, but their inference latency exceeds stepwise vehicle-control windows. Learned world models predict futures, but they usually keep future generation and action selection inside large coupled loops. We present SteinsGateDrive, a latency-decoupled planner-runtime architecture in which the worldline metaphor from the eponymous story names one plausible consequence of an intervention: the LLM selects counterfactual driving futures befo...

</details>

---

### [Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts](https://arxiv.org/abs/2605.22446v1)

**Authors:** Zhen Sun, Yongjian Guo, Haoran Sun, Luqiao Wang, Wei Lu et al. (9 authors)

**Published:** 2026-05-21 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.22446v1) | [PDF](https://arxiv.org/pdf/2605.22446v1.pdf)

<details>
<summary>Abstract</summary>

While large vision-language-action (VLA) models and generative world models (WM) have advanced long-horizon embodied intelligence, their practical deployment remains challenged by uncertainty in learning-based action generation. Low-quality actions may cause physical failures during execution or lead to misleading world-model rollouts with redundant rendering costs. To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity ass...

</details>

---

### [Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics](https://arxiv.org/abs/2605.22164v1)

**Authors:** Liangyu Li, Shengzhi Wang, Qingwen Liu

**Published:** 2026-05-21 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.22164v1) | [PDF](https://arxiv.org/pdf/2605.22164v1.pdf)

<details>
<summary>Abstract</summary>

Latent world models can contain the state needed for control, yet their terminal-cost interface can expose the planner to the wrong decision-relevant information. In common latent MPC, candidate sequences are ranked by Euclidean distance between predicted terminal and goal latent states; this assumes that raw latent distance weights reachability-relevant variables correctly. We propose trajectory reachability metrics (TRM), a post-hoc terminal-ranking method for fixed latent world models. TRM tr...

</details>

---

### [LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model](https://arxiv.org/abs/2605.22089v1)

**Authors:** Xiaodong Mei, Diankun Zhang, Hongwei Xie, Guang Chen, Hangjun Ye et al. (6 authors)

**Published:** 2026-05-21 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.22089v1) | [PDF](https://arxiv.org/pdf/2605.22089v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a promising framework for end-to-end autonomous driving. However, existing VLAs typically rely on sparse action supervision, which underutilizes their powerful scene understanding and reasoning capabilities. Recent attempts to incorporate dense visual supervision via world modeling often overemphasize pixel-level image reconstruction, neglecting semantically meaningful scene representation learning. In this work, we propose LVDrive, a Latent Vi...

</details>

---

### [ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data](https://arxiv.org/abs/2605.21963v1)

**Authors:** Jiangyuan Wang, Xuyong Chen, Junwei He, Xu Xu, Shasha Xie et al. (6 authors)

**Published:** 2026-05-21 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.21963v1) | [PDF](https://arxiv.org/pdf/2605.21963v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon clinical simulation -- predicting how a patient's physiology evolves over years under specified interventions -- is central to chronic-disease care, yet existing electronic health record (EHR) models are predominantly discriminative, and general-purpose large language models drift under repeated interventions. We propose the \textbf{ChronoMedicalWorld Model (CMWM)}, an action-conditioned latent world-model framework for learning patient trajectories from longitudinal care data. CMWM...

</details>

---

### [stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation](https://arxiv.org/abs/2605.21800v1)

**Authors:** Lucas Maes, Quentin Le Lidec, Luiz Facury, Nassim Massaudi, Ayush Chaurasia et al. (12 authors)

**Published:** 2026-05-20 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.21800v1) | [PDF](https://arxiv.org/pdf/2605.21800v1.pdf)

<details>
<summary>Abstract</summary>

World models are central to building agents that can reason, plan, and generalize beyond their training data. However, research on world models is currently fragmented, with disparate codebases, data pipelines, and evaluation protocols hindering reproducibility and fair comparison. Current practice is further limited by three key bottlenecks: fragile one-off codebases, slow video data loading, and the lack of standardized generalization benchmarks. We present stable-worldmodel (swm), an open-sou...

</details>

---

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
