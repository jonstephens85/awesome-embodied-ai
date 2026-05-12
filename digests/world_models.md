# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-05-12 22:51 UTC

**Papers found:** 17

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models](https://arxiv.org/abs/2605.09241v1)

**Authors:** Kai Zhao, Dongliang Nie, Yuchen Lin, Zhehan Luo, Yixiao Gu et al. (7 authors)

**Published:** 2026-05-10 | **Categories:** cs.LG, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.09241v1) | [PDF](https://arxiv.org/pdf/2605.09241v1.pdf) | [GitHub](https://github.com/intcomp/Sub-JEPA)

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be alleviated bysimply constraining latent embeddings with an isotropic Gaussian prior.However, latent repre...

</details>

---

## Other Recent Papers

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

### [Multi-Tier Labeling and Physics-Informed Learning for Orbital Anomaly Detection at Scale](https://arxiv.org/abs/2605.09790v1)

**Authors:** Yong Fu

**Published:** 2026-05-10 | **Categories:** cs.DC, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.09790v1) | [PDF](https://arxiv.org/pdf/2605.09790v1.pdf)

<details>
<summary>Abstract</summary>

Detecting orbital anomalies, such as maneuvers, atmospheric decay, and attitude upsets, across the rapidly growing population of low-Earth-orbit (LEO) satellites is a prerequisite for collision avoidance, decay forecasting, and conjunction screening. The bottleneck is not modeling capacity but labels: there is no public ground-truth corpus of orbital anomalies, manual review does not scale to approximately 10^4 active satellites, and pure rule-based detectors trade recall for precision so aggres...

</details>

---

### [DriveFuture: Future-Aware Latent World Models for Autonomous Driving](https://arxiv.org/abs/2605.09701v1)

**Authors:** Yufeng Hong, Xiaotian Zhou, Yingyan Li, Xiangpo Zhou, Lin Liu et al. (9 authors)

**Published:** 2026-05-10 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.09701v1) | [PDF](https://arxiv.org/pdf/2605.09701v1.pdf)

<details>
<summary>Abstract</summary>

Existing latent world models for autonomous driving have opened a promising path toward future-aware driving intelligence. However, they typically treat future latent states as prediction targets or auxiliary signals, rather than directly conditioning trajectory planning. This can entangle current and future features in latent space. In this work, we propose DriveFuture, a future-aware latent world modeling framework for autonomous driving that explicitly learns planning-oriented foresight by co...

</details>

---

### [Do multimodal models imagine electric sheep?](https://arxiv.org/abs/2605.09693v1)

**Authors:** Santhosh Kumar Ramakrishnan, Carl Vondrick, Raja Giryes, Philipp Krähenbühl, Vladlen Koltun

**Published:** 2026-05-10 | **Categories:** cs.CV, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.09693v1) | [PDF](https://arxiv.org/pdf/2605.09693v1.pdf)

<details>
<summary>Abstract</summary>

Yes. We find that large multimodal models develop mental imagery when solving spatial puzzles, and they do imagine sheep when solving sheep puzzles. We fine-tune a Qwen3.5 VLM to solve twelve diverse visual reasoning tasks -- including tangram, jigsaw, sokoban, 3D mental rotation, and rush hour -- that require understanding geometry, spatial relationships, and the consequences of actions. By supervising the model to predict the open-loop sequence of actions to solve a puzzle from an initial stat...

</details>

---

### [Absurd World: A Simple Yet Powerful Method to Absurdify the Real-world for Probing LLM Reasoning Capabilities](https://arxiv.org/abs/2605.09678v1)

**Authors:** Ryan Albright, Golam Md Muktadir, Zarif Ikram, S M Jubaer, Mehrab Hossain et al. (6 authors)

**Published:** 2026-05-10 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.09678v1) | [PDF](https://arxiv.org/pdf/2605.09678v1.pdf)

<details>
<summary>Abstract</summary>

While extremely powerful and versatile at various tasks, the thinking capabilities of large language models (LLMs) are often put under scrutiny as they sometimes fail to solve problems that humans can systematically solve. However, recent literature focuses on breaking LLM reasoning with increasingly complex problems, and whether an LLM is robust in simple logical reasoning remains underexplored. This paper proposes Absurd World, a benchmarking framework, to test LLMs against altered realism, wh...

</details>

---

### [Workspace Optimization: How to Train Your Agent](https://arxiv.org/abs/2605.09650v1)

**Authors:** Elad Sarafian, Gal Kaplun, Ron Banner, Daniel Soudry, Boris Ginsburg

**Published:** 2026-05-10 | **Categories:** cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.09650v1) | [PDF](https://arxiv.org/pdf/2605.09650v1.pdf)

<details>
<summary>Abstract</summary>

Modern agents built on frontier language models often cannot adapt their weights. What, then, remains trainable? We argue it is the agent's \emph{workspace}, the structured external substrate it reads, writes, and tests; we call its evolution workspace optimization. Workspace optimization targets hard multi-turn environments where a frontier model has strong priors but cannot solve the task in a single shot, so the agent must learn through interaction. We propose a principled way to evolve the w...

</details>

---

### [DeformMaster: An Interactive Physics-Neural World Model for Deformable Objects from Videos](https://arxiv.org/abs/2605.09586v1)

**Authors:** Can Li, Zhoujian Li, Ren Li, Jie Gu, Lei Lei et al. (7 authors)

**Published:** 2026-05-10 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.09586v1) | [PDF](https://arxiv.org/pdf/2605.09586v1.pdf)

<details>
<summary>Abstract</summary>

World models for deformable objects should recover not only geometry and appearance, but also underlying physical dynamics, interaction grounding, and material behavior. Learning such a model from real videos is challenging because deformable linear, planar, and volumetric objects evolve under high-dimensional deformation, noisy interactions, and complex material response. The model must therefore infer a physical state from visual observations, roll it forward under new interactions, and render...

</details>

---

### [FLAME: Adaptive Mixture-of-Experts for Continual Multimodal Multi-Task Learning](https://arxiv.org/abs/2605.09355v1)

**Authors:** Xing Han, Shravan Chaudhari, Tanvi Ranade, Rama Chellappa, Suchi Saria

**Published:** 2026-05-10 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.09355v1) | [PDF](https://arxiv.org/pdf/2605.09355v1.pdf)

<details>
<summary>Abstract</summary>

Real-world model deployment across multiple domains requires multimodal models to operate under two complementary regimes: (1) multi-task pretraining, tasks are co-available at design time where related tasks could borrow representational strength from one another, (2) continual adaptation, in which new tasks emerge after deployment with previously unseen modality combinations. However, neither regime alone suffices: the pretraining task set is never exhaustive, while bypassing joint training fo...

</details>

---
