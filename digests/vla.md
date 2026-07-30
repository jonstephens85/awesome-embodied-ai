# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-30 22:55 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](https://arxiv.org/abs/2607.27205v1)

**Authors:** Hengyi Xie, Chenfei Yao, Xianjin Wu, Xuanyang Xi, Yiping Tang et al. (10 authors)

**Published:** 2026-07-29 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.27205v1) | [PDF](https://arxiv.org/pdf/2607.27205v1.pdf) | [GitHub](https://github.com/H-EmbodVis/TurboVLA)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we introduce TurboVLA, a new VLA paradigm that reformulates the conventional $V \to L \to A$ pathway as a direct $V + L \to A$ mapping. Instead of ...

</details>

---

### [CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model](https://arxiv.org/abs/2607.25487v1)

**Authors:** Minhyeok Lee, Chiyoung Kim, Chanhoe Gu, Seongrok Kim, Sanghyuk Roy Choi et al. (8 authors)

**Published:** 2026-07-28 | **Categories:** cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.25487v1) | [PDF](https://arxiv.org/pdf/2607.25487v1.pdf) | [GitHub](https://github.com/BrainJellyPie/CoTinyVLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models translate natural-language commands into robot action sequences, but leading systems on the LIBERO-Plus robustness benchmark use three- to seven-billion-parameter backbones whose memory demands can exceed embedded robotic budgets. We present CoTinyVLA, a 0.9B-parameter action model on a Qwen3.5-0.8B backbone that obtains that robustness by structuring supervision instead of enlarging the model. Three components target different axes of the problem: dual-view t...

</details>

---

### [HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone](https://arxiv.org/abs/2607.25895v1)

**Authors:** Simple AI,  :, Yuteng Wei, Jinming Ma, Jiawei Wang et al. (19 authors)

**Published:** 2026-07-28 | **Categories:** cs.RO, cs.CV, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2607.25895v1) | [PDF](https://arxiv.org/pdf/2607.25895v1.pdf) | [Project Page](https://cloud.simpleai.tech/simple-world-lab/hifi-umi/)

<details>
<summary>Abstract</summary>

Learning deployable manipulation policies is bottlenecked by the scarcity of data that is both high-fidelity and scalable. Real-robot teleoperation is accurate but costly to scale; robot-free UMI capture scales readily, and current practice uses the resulting data mainly for pre-training, adding a small real-robot "anchor" at post-training. We ask whether raising the fidelity of robot-free UMI data, rather than shrinking the real-robot fraction, can remove that anchor. We present HiFi-UMI, a por...

</details>

---

## Other Recent Papers

### [DLAM: Distributional Latent Actions with Temporal Constraints](https://arxiv.org/abs/2607.27138v1)

**Authors:** Zuojin Tang, Feifan Luo, Haoyun Liu, Botai Yuan, Dekang Qi et al. (13 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.27138v1) | [PDF](https://arxiv.org/pdf/2607.27138v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models remain constrained by scarce action-labeled robot data, whereas action-free videos offer abundant observations of physical change. Latent action models can extract such priors, but reconstruction-trained codes may predict future observations without the structure required for joint generation with robot actions. Existing structured methods add temporal constraints but retain deterministic transition points, so residual errors in locally inferred transitions ma...

</details>

---

### [RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models](https://arxiv.org/abs/2607.26991v1)

**Authors:** Derek Ming Siang Tan, Shailesh Shailesh, Srikrishna Iyer, William Wei Jie Teo, Yuanliang Ju et al. (7 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26991v1) | [PDF](https://arxiv.org/pdf/2607.26991v1.pdf)

<details>
<summary>Abstract</summary>

Despite the impressive visuomotor capabilities enabled by Vision-Language-Action (VLA) models, their performance often degrades on challenging and out-of-domain tasks. Recent test-time steering and scaling methods improve performance without extensive data collection and retraining, but action samples often remain concentrated around similar behaviors and therefore inherit correlated failure modes. Moreover, existing methods apply the same intervention strategy at every timestep, regardless of w...

</details>

---

### [Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA](https://arxiv.org/abs/2607.26807v1)

**Authors:** Tianhang Yang, Yanze Zheng, Junjie Wang, Wei-Bin Kou, Ruotong Li et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26807v1) | [PDF](https://arxiv.org/pdf/2607.26807v1.pdf)

<details>
<summary>Abstract</summary>

While MoE augments VLA via expert specialization, router suffers from ineffective expert routing owing to the kinematic heterogeneity of actions across manipulation tasks and, even worse, the unavailability of the kinematic signals at inference time. In this work, we first observe that most semantically distinct manipulation tasks reduce to multiple kinematic archetypes. Motivated by this finding, we propose Kinematics-supervised explicit routing (KinRT), a new paradigm that shifts from implicit...

</details>

---

### [CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2607.26789v1)

**Authors:** Yushan Liu, Peibo Sun, Xintao Chao, Zhenyang Yang, Yifan Xie et al. (11 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26789v1) | [PDF](https://arxiv.org/pdf/2607.26789v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks, issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate the error: commit-time policy confidence cannot react to a deviation that occurs after dispatch, and observation-only anomaly scores l...

</details>

---

### [Explicit Kinematic Guidance from Analytic Concepts for Vision-Language-Action Models](https://arxiv.org/abs/2607.26513v1)

**Authors:** Mingyang Sun, Jiude Wei, Xiujian Liang, Qichen He, Donglin Wang et al. (7 authors)

**Published:** 2026-07-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.26513v1) | [PDF](https://arxiv.org/pdf/2607.26513v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) models rely mainly on 2D inputs, neglecting the rich object structural information and commonsense knowledge inherent in the 3D physical world. This deficiency restricts their spatial awareness and adaptability for complex, high-precision manipulation. To bridge this crucial gap, we construct a Concept Expert module for VLA to build executable Analytic Concepts that represent objects as explicit, programmatic blueprints. Our mechanism operates in two synergis...

</details>

---

### [CG-World: A Large-Scale World-State Dataset and Protocol for World Models](https://arxiv.org/abs/2607.26452v1)

**Authors:** Yiming Cai, Fangjie Yu, Meiqing Yu, Ziyue Shi, Pengfei Yuan et al. (6 authors)

**Published:** 2026-07-29 | **Categories:** cs.AI, cs.CV, cs.GR

**Links:** [arXiv](https://arxiv.org/abs/2607.26452v1) | [PDF](https://arxiv.org/pdf/2607.26452v1.pdf)

<details>
<summary>Abstract</summary>

World models must learn the joint dynamics of states, actions, events, and observations, yet existing video, robotics, and simulation datasets usually capture only part of this structure. We introduce CG-World, a large-scale world-state dataset and protocol derived from industrial computer graphics production pipelines. CG-World explicitly records intermediate states, including multimodal semantics, spatial structure, skeletal and controller states, motion curves, camera and lighting parameters,...

</details>

---

### [SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2607.25912v1)

**Authors:** Zonghe Liu, Shanyuan Jie, Xiaoquan Sun, Chen Cao, Zetian Xu et al. (7 authors)

**Published:** 2026-07-28 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.25912v1) | [PDF](https://arxiv.org/pdf/2607.25912v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong potential for general robot manipulation, but most existing models rely on 2D visual-language backbones and lack fine-grained 3D understanding of target objects, especially under occlusion, pose variation, scale changes, and precise spatial interaction. We propose an object-centric 3D representation alignment framework built upon $π_0$, using SAM3D as a frozen 3D teacher to provide target-object 3D priors during training. Specifically, we loc...

</details>

---

### [A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models](https://arxiv.org/abs/2607.25516v1)

**Authors:** Haoyu Zhang, Yuwei Wu, Jin Chen, Gao Zhi, Zhenxin Diao et al. (9 authors)

**Published:** 2026-07-28 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.25516v1) | [PDF](https://arxiv.org/pdf/2607.25516v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models predict sequential actions to execute tasks specified by language instructions, conditioned on visual observations and proprioceptive states. However, how to fuse modalities in VLA models remains an open problem, since robot manipulation involves dynamic phases, such as long-distance movements and close-range interactions, in which the importance of visual observations may vary over time. In this paper, we propose an infer-diagnose-refine (IDR) framework, a mo...

</details>

---
