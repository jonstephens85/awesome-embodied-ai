# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-29 17:14 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking](https://arxiv.org/abs/2607.24008v1)

**Authors:** Hai Jiang, Yixian Zou, Binbin Liang, Boqian Liu, Fanman Meng et al. (6 authors)

**Published:** 2026-07-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.24008v1) | [PDF](https://arxiv.org/pdf/2607.24008v1.pdf) | [Project Page](https://jianghaiscu.github.io/FutureRTC_proj/)

<details>
<summary>Abstract</summary>

Real-time deployment of Vision-Language-Action (VLA) policies necessitates asynchronous execution, wherein subsequent action chunks are computed concurrently with the execution of the current chunk, leading to prediction-execution misalignment and manifesting as inter-chunk discontinuities. Existing methods either superficially smooth chunk boundaries, require costly policy optimization, or exclusively forward-predict proprioceptive states yet neglect critical visual observations. In this paper,...

</details>

---

### [Data Pyramid for Embodied Manipulation](https://arxiv.org/abs/2607.24744v1)

**Authors:** Yifan Ye, Yankai Fu, Yaoxu Lv, Bohan Hou, Jun Cen et al. (29 authors)

**Published:** 2026-07-27 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.24744v1) | [PDF](https://arxiv.org/pdf/2607.24744v1.pdf) | [Project Page](at) | [GitHub](https://github.com/worldbench/awesome-embodied-data-pyramid)

<details>
<summary>Abstract</summary>

Multimodal foundation models learned to see and to speak by consuming the whole internet. Embodied agents admit no such shortcut, since they require data that couple observations with physical states and actions. These signals can be provided, to varying degrees, by multiple data sources. In this work, we organize the embodied data ecosystem as a "pyramid" spanning five complementary sources: real-robot data, UMI-style data, egocentric and exocentric data, simulation data, and general vision-lan...

</details>

---

### [DeVA: Decoupled Video-Action Model with physical guidance for robot policy learning](https://arxiv.org/abs/2607.24159v1)

**Authors:** Mengqi Zhang, Sahil Khose, Simar Kareer, Yuchen Song, Unnat Jain et al. (6 authors)

**Published:** 2026-07-27 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.24159v1) | [PDF](https://arxiv.org/pdf/2607.24159v1.pdf) | [Project Page](with)

<details>
<summary>Abstract</summary>

Generalizable robot manipulation requires policies that can anticipate how visual scenes evolve while executing language instructions. While recent Vision-Language-Action models benefit from large-scale pretraining, their predominantly static pretraining objectives provide limited supervision for physical dynamics and temporal causality, leaving control-relevant knowledge to be learned from downstream robot demonstrations. Video generative models offer a promising foundation by encoding rich spa...

</details>

---

## Other Recent Papers

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

### [τ: Learning Touch-Augmented Vision-Language-Action Models from Future Visual Supervision](https://arxiv.org/abs/2607.24485v1)

**Authors:** Ning Cheng, Jinan Xu, Wanlin Li, Yangzhi Chen, Jing Gao et al. (8 authors)

**Published:** 2026-07-27 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2607.24485v1) | [PDF](https://arxiv.org/pdf/2607.24485v1.pdf)

<details>
<summary>Abstract</summary>

Learning the informative tactile representation while effectively adapting it to pretrained Vision-Language-Action (VLA) models remains challenging at both the data and modeling levels. At the data level, limited task-specific demonstrations constrain representation quality, whereas large-scale pretraining incurs substantial costs. At the modeling level, existing methods either focus on instantaneous contact states or model temporal interaction dynamics using 6D wrench sequences, leaving high-di...

</details>

---

### [A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference](https://arxiv.org/abs/2607.24148v1)

**Authors:** Zhuoran Song, Haozhe Jiang, Chunyu Qi, Minnan Pei, Gang Li et al. (7 authors)

**Published:** 2026-07-27 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.24148v1) | [PDF](https://arxiv.org/pdf/2607.24148v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong potential for embodied AI, yet their high inference latency on GPUs limits real-time deployment. Existing accelerators, such as Dadu-Corki, improve efficiency but treat VLA models as full-precision workloads, leaving substantial redundancy in both memory and computation underexploited. In this paper, we propose VQVLA, an algorithm-hardware co-design framework that accelerates VLA inference by exploiting weight similarity and execution ...

</details>

---
