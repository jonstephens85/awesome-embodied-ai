# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-09 22:33 UTC

**Papers found:** 6

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

### [Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning](https://arxiv.org/abs/2605.05544v1)

**Authors:** Nandiraju Gireesh, Yuanliang Ju, He Wang

**Published:** 2026-05-07 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.05544v1) | [PDF](https://arxiv.org/pdf/2605.05544v1.pdf)

<details>
<summary>Abstract</summary>

Offline-to-online reinforcement learning with action chunking eliminates multi-step off-policy bias and enables temporally coherent exploration, but all existing methods use a fixed chunk size across every state. This is suboptimal: near contact events the agent needs short chunks for reactive control, while during free-space motion long chunks provide better credit assignment. The natural solution is to train critics for several chunk sizes and select the best one at each state, but naive compa...

</details>

---
