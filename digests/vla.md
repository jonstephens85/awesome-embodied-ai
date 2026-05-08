# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-08 22:46 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts](https://arxiv.org/abs/2605.06175v1)

**Authors:** Yuhua Jiang, Junjie Lu, Xinyao Qin, Xiaoyu Chen, Kaixin Wang et al. (7 authors)

**Published:** 2026-05-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.06175v1) | [PDF](https://arxiv.org/pdf/2605.06175v1.pdf) | [GitHub](https://github.com/YuhuaJiang2002/VLA-GSE)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models inherit rich visual-semantic priors from pre-trained vision-language backbones, but adapting them to robotic control remains challenging. Full fine-tuning (FFT) is prone to overfitting on downstream robotic data and catastrophic forgetting of pretrained vision-language capabilities. Parameter-efficient fine-tuning (PEFT) better preserves pre-trained knowledge, yet existing PEFT methods still struggle to adapt effectively to robot control tasks. To address this...

</details>

---

### [ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation](https://arxiv.org/abs/2605.05126v1)

**Authors:** Wei Li, Jizhihui Liu, Li Yixing, Junwen Tong, Rui Shao et al. (6 authors)

**Published:** 2026-05-06 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.05126v1) | [PDF](https://arxiv.org/pdf/2605.05126v1.pdf) | [GitHub](https://github.com/iLearn-Lab/CVPR26-ConsisVLA-4D)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions, but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often rely on additional sensors, introducing substantial computational overhead; 2) visual reasoning is typically limited to future-frame prediction, lacking alignment with the instruction-grounded scene and thus compromising spatiotemporal consistency. To address these challenges, we propose Con...

</details>

---

### [From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models](https://arxiv.org/abs/2605.04678v1)

**Authors:** Yihan Lin, Haoyang Li, Yang Li, Haitao Shen, Yihan Zhao et al. (7 authors)

**Published:** 2026-05-06 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.04678v1) | [PDF](https://arxiv.org/pdf/2605.04678v1.pdf) | [GitHub](https://github.com/RUCKBReasoning/From_Pixels_to_Tokens)

<details>
<summary>Abstract</summary>

Latent actions serve as an intermediate representation that enables consistent modeling of vision-language-action (VLA) models across heterogeneous datasets. However, approaches to supervising VLAs with latent actions are fragmented and lack a systematic comparison. This work structures the study of latent action supervision from two perspectives: (i) regularizing the trajectory via image-based latent actions, and (ii) unifying the target space with action-based latent actions. Under a unified V...

</details>

---

### [CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies](https://arxiv.org/abs/2605.04470v1)

**Authors:** Keyu Chen, Nanfei Ye, Yida Wang, Wenchao Sun, Danqi Zhao et al. (7 authors)

**Published:** 2026-05-06 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.04470v1) | [PDF](https://arxiv.org/pdf/2605.04470v1.pdf) | [Project Page](https://currychen77.github.io/CRAFT)

<details>
<summary>Abstract</summary>

Open-loop imitation learning has advanced modern autonomous driving policy architectures, but closed-loop deployment remains vulnerable to policy-induced distribution shift. Existing post-training paradigms exhibit fundamental trade-offs: closed-loop RL fine-tuning provides grounded feedback from executed actions but is constrained by the sparsity of informative events, whereas counterfactual fine-tuning provides dense supervision over candidate futures but inherits bias from imperfect future es...

</details>

---

## Other Recent Papers

### [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/abs/2605.06481v1)

**Authors:** Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang et al. (10 authors)

**Published:** 2026-05-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.06481v1) | [PDF](https://arxiv.org/pdf/2605.06481v1.pdf)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) enhance Vision-Language-Action policies by jointly predicting scene evolution and robot actions, but existing methods usually represent the predicted world as holistic images, video tokens, or global latents. These representations are difficult for an action decoder to address when an instruction refers to a particular object, especially under scene shifts where object identity is entangled with context. We propose OA-WAM, an Object-Addressable World Action Model for r...

</details>

---

### [Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation](https://arxiv.org/abs/2605.06311v1)

**Authors:** Yixin Zhu, Zixiong Wang, Jian Yang, Jin Xie, Jingyi Yu et al. (7 authors)

**Published:** 2026-05-07 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.06311v1) | [PDF](https://arxiv.org/pdf/2605.06311v1.pdf)

<details>
<summary>Abstract</summary>

Reliable simulation evaluation of robot manipulation policies serves as a high-fidelity proxy for real-world performance. Although existing benchmarks cover a wide range of task categories, they lack visual realism, creating a large domain gap between simulation and reality. This undermines the reliability of simulation-based evaluation in predicting real-world performance. To mitigate the sim-to-real visual gap, we conduct a systematic analysis to isolate the effects of lighting and material. O...

</details>

---

### [MobileEgo Anywhere: Open Infrastructure for long horizon egocentric data on commodity hardware](https://arxiv.org/abs/2605.05945v1)

**Authors:** Senthil Palanisamy, Abhishek Anand, Satpal Singh Rathor, Pratyush Patnaik, Shubhanshu Khatana

**Published:** 2026-05-07 | **Categories:** cs.CV, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.05945v1) | [PDF](https://arxiv.org/pdf/2605.05945v1.pdf)

<details>
<summary>Abstract</summary>

The recent advancement of Vision Language Action (VLA) models has driven a critical demand for large scale egocentric datasets. However, existing datasets are often limited by short episode durations, typically spanning only a few minutes, which fails to capture the long horizon temporal dependencies necessary for complex robotic task execution. To bridge this gap, we present MobileEgo Anywhere, a framework designed to facilitate the collection of robust, hour plus egocentric trajectories using ...

</details>

---

### [TriRelVLA: Triadic Relational Structure for Generalizable Embodied Manipulation](https://arxiv.org/abs/2605.05714v1)

**Authors:** Hanyu Zhou, Chuanhao Ma, Gim Hee Lee

**Published:** 2026-05-07 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.05714v1) | [PDF](https://arxiv.org/pdf/2605.05714v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models perform well on training-seen robotic tasks but struggle to generalize to unseen scenes and objects. A key limitation lies in their implicit visual representations, which entangle object appearance, background, and scene layout. This makes policies sensitive to visual variations. Prior work improves transferability through structured intermediate representations that objectify visual content. However, these representations mainly capture scene semantics instea...

</details>

---
