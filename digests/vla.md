# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-20 17:26 UTC

**Papers found:** 10

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models](https://arxiv.org/abs/2606.19784v1)

**Authors:** Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, Long Dinh, Minh Duc Nguyen et al. (11 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.19784v1) | [PDF](https://arxiv.org/pdf/2606.19784v1.pdf) | [Project Page](https://equivla.github.io/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for generalist robot manipulation, yet they lack geometric inductive biases: policies trained at specific orientations require substantially more data to generalize across rotational configurations. We present \textsc{EquiVLA}, the first general framework for end-to-end $\mathrm{SO}(2)$-equivariant VLA models, applicable to any architecture coupling a frozen vision-language backbone with a flow-matching Diffusion Transformer...

</details>

---

## Other Recent Papers

### [MemoryWAM: Efficient World Action Modeling with Persistent Memory](https://arxiv.org/abs/2606.20562v1)

**Authors:** Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li et al. (11 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.20562v1) | [PDF](https://arxiv.org/pdf/2606.20562v1.pdf)

<details>
<summary>Abstract</summary>

Robust robotic manipulation in the real world requires not only an understanding of the current observation, but also memory and dynamics modeling. World action models (WAMs) possess these capabilities by jointly modeling visual foresight and actions conditioned on both current and historical observations, making them a promising paradigm for robotic manipulation. However, existing WAMs face a fundamental trade-off: methods with efficient inference typically condition only on a bounded window of...

</details>

---

### [Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems](https://arxiv.org/abs/2606.20285v1)

**Authors:** Yandong Wang, Jiaqian Yu, Xiongfeng Peng, Lu Xu, Yamin Mao et al. (11 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.20285v1) | [PDF](https://arxiv.org/pdf/2606.20285v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models show strong capabilities in single and dual-arm robotic manipulation. Prior works show coordinated bimanual behaviors can emerge from end-to-end learning, leveraging large vision-language backbones with continuous action prediction. However, as bimanual tasks become tightly coupled and execution constraints become critical, implicit coordination alone is insufficient to ensure reliable, interpretable, and stable behavior. In this work, we propose Co-VLA, a coo...

</details>

---

### [Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving](https://arxiv.org/abs/2606.20274v1)

**Authors:** Shihao Ji, HongXi Li, Zihui Song, Mingyu Li

**Published:** 2026-06-18 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.20274v1) | [PDF](https://arxiv.org/pdf/2606.20274v1.pdf)

<details>
<summary>Abstract</summary>

Scaling end-to-end autonomous driving to complex, open-world environments requires perceptual models that generalize to anomalous scenarios and planners that produce kinematically valid trajectories. Existing paradigms face a distinct dichotomy between representational efficiency and generalization capacity. Dense models (e.g., occupancy networks), while geometrically robust, incur critical computational bottlenecks and struggle with high-level semantic reasoning. Conversely, sparse, query-based...

</details>

---

### [Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think](https://arxiv.org/abs/2606.20246v1)

**Authors:** Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller et al. (20 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.20246v1) | [PDF](https://arxiv.org/pdf/2606.20246v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have revolutionized robotic manipulation, yet their multi-billion parameter architectures impose prohibitive computational burdens during downstream fine-tuning and real-time inference. In this work, we reveal a highly non-trivial architectural characteristic of these continuous control foundation policies (e.g., pi_0, GR00T-N1.5): despite being trained on diverse physical trajectories, they exhibit severe layer-wise...

</details>

---

### [Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation](https://arxiv.org/abs/2606.20118v1)

**Authors:** Jonghoon Lee, Seong Hyeon Park, Byungwoo Jeon, Minha Lee, Jinwoo Shin

**Published:** 2026-06-18 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.20118v1) | [PDF](https://arxiv.org/pdf/2606.20118v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies have shown strong potential for general-purpose manipulation, yet they often fail on novel, out-of-distribution objects whose appearance or geometry deviates from the training distribution. The standard remedy is to collect multi-view teleoperation data for every failure case, but this scales poorly in both cost and time. We introduce Pose6DAug, a failure-driven data augmentation framework that turns a policy's own successful episodes into targeted demonstra...

</details>

---

### [EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/abs/2606.20092v1)

**Authors:** Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, Sitong Mao, Junyi Dong et al. (13 authors)

**Published:** 2026-06-18 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.20092v1) | [PDF](https://arxiv.org/pdf/2606.20092v1.pdf)

<details>
<summary>Abstract</summary>

Memory remains a critical bottleneck for long-horizon robotic manipulation, as standard Vision-Language-Action (VLA) policies often fail when task-relevant cues become occluded or unobservable over time. While existing memory-augmented methods utilize historical context, they either suffer from severe information bottlenecks, incur high latency via decoupled dual systems, or rely on unselective buffers that accumulate massive visual redundancies. To address these limitations, we introduce EventV...

</details>

---

### [Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory](https://arxiv.org/abs/2606.19998v1)

**Authors:** Jinghan Yang, Yunchao Zhang, Wang Yuan, Haolun Wan, Jiaming Zhang et al. (7 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.19998v1) | [PDF](https://arxiv.org/pdf/2606.19998v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet they remain black boxes whose physical interactions can cause irreversible harm, making generalizable and interpretable failure detection essential. We observe that successful and failed rollouts carry systematically different information-theoretic signatures. Building on this, we formalize VLA control as a closed-loop information pipeline and derive the Triple Information-theoretic (Tri-Info) signals that ca...

</details>

---

### [Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation](https://arxiv.org/abs/2606.20458v1)

**Authors:** Zhenghao "Mark'' Peng, Honglin He, Quanyi Li, Yukai Ma, Bolei Zhou

**Published:** 2026-06-18 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.20458v1) | [PDF](https://arxiv.org/pdf/2606.20458v1.pdf)

<details>
<summary>Abstract</summary>

Learning-based planners for sidewalk navigation can generate diverse candidate trajectories in real time, yet their scoring functions often fail to select the best trajectory in challenging situations, outputting trajectories that make the mobile robot drive onto grass, toward pedestrians, or in the wrong direction, even when better candidates exist in the same set. We call this the trajectory scoring gap: in real-world sidewalk navigation, the gap between an anchor-based planner's top choice an...

</details>

---

### [Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation](https://arxiv.org/abs/2606.20135v1)

**Authors:** Jianing Guo, Fangzheng Chen, Zihao Mao, Wong Lik Hang Kenny, Zhenhong Wu et al. (15 authors)

**Published:** 2026-06-18 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.20135v1) | [PDF](https://arxiv.org/pdf/2606.20135v1.pdf)

<details>
<summary>Abstract</summary>

Flow matching has emerged as a standard paradigm for robotic manipulation owing to its strong expressive power for modelling complex, multimodal action distributions, alongside similar approaches like diffusion policy. However, existing methods rely on discretized action chunks, making them brittle to demonstrations collected at heterogeneous control frequencies and prone to temporally inconsistent actions that degrade control stability. In this paper, we propose Frequency-Aware Flow Matching (F...

</details>

---
