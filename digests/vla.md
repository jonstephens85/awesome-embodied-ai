# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-07-28 22:50 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

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

### [A Few Words Go a Long Way: Language Guided Robot Policy Synthesis](https://arxiv.org/abs/2607.23784v1)

**Authors:** Daphne Chen, Archit Ritesh Jain, Eric Goossen, Emma Romig, Michael Murray et al. (7 authors)

**Published:** 2026-07-26 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.23784v1) | [PDF](https://arxiv.org/pdf/2607.23784v1.pdf) | [Project Page](https://robo-architect.github.io/)

<details>
<summary>Abstract</summary>

While vision-language-action models have demonstrated impressive zero-shot manipulation capabilities, they remain fundamentally black box policies that are difficult to interpret, adapt, or correct when they inevitably fail. In this work, we propose ARCHITECT, a framework that treats robot policy acquisition as an interactive program synthesis task. ARCHITECT leverages the reasoning capabilities of LLM coding agents to synthesize modular robot programs that utilize a suite of perception and cont...

</details>

---

### [LabRobFail: A Benchmark for Robotic Failure Analysis in Chemical Self-driving Laboratories](https://arxiv.org/abs/2607.23704v1)

**Authors:** Haobo Wang, Baoli Sun, Anqi Zou, Dongsheng Huang, Zelin Lv et al. (11 authors)

**Published:** 2026-07-26 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2607.23704v1) | [PDF](https://arxiv.org/pdf/2607.23704v1.pdf) | [GitHub](https://github.com/Su-ISE-2001/SciRobo)

<details>
<summary>Abstract</summary>

The deployment of embodied agents in self-driving laboratories could accelerate scientific discovery, yet their reliability is constrained by the irreversible and safety-critical nature of chemical experiments. Progress is further hindered by scarce failure data and the lack of fine-grained evaluation protocols. To address these challenges, we introduce LabRobFail, a failure-centric framework for learning and evaluating robotic failure analysis in chemical laboratories. LabRobFail-Sim injects co...

</details>

---

## Other Recent Papers

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

### [MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents](https://arxiv.org/abs/2607.23870v1)

**Authors:** Belal S. Alsinglawi, Weizheng Wang, Junyi Wu, Yi Jiang, Lianhai Lin et al. (7 authors)

**Published:** 2026-07-26 | **Categories:** cs.MA, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2607.23870v1) | [PDF](https://arxiv.org/pdf/2607.23870v1.pdf)

<details>
<summary>Abstract</summary>

Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language. Existing UAV and multimodal benchmarks evaluate perception, navigation, collaboration, and reasoning, but few assess whether physical evidence, protocol constraints, and action risk remain coupled during critical decisions. We introduce MulRobBench, an offline, protocol-conditi...

</details>

---
