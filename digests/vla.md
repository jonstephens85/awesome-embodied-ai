# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-15 22:43 UTC

**Papers found:** 15

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/abs/2605.14712v1)

**Authors:** Shijie Lian, Bin Yu, Xiaopeng Lin, Zhaolong Shen, Laurence Tianruo Yang et al. (11 authors)

**Published:** 2026-05-14 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.14712v1) | [PDF](https://arxiv.org/pdf/2605.14712v1.pdf) | [GitHub](https://github.com/ZGC-EmbodyAI/IntentVLA)

<details>
<summary>Abstract</summary>

Robot imitation data are often multimodal: similar visual-language observations may be followed by different action chunks because human demonstrators act with different short-horizon intents, task phases, or recent context. Existing frame-conditioned VLA policies infer each chunk from the current observation and instruction alone, so under partial observability they may resample different intents across adjacent replanning steps, leading to inter-chunk conflict and unstable execution. We introd...

</details>

---

### [VGGT-$Ω$](https://arxiv.org/abs/2605.15195v1)

**Authors:** Jianyuan Wang, Minghao Chen, Shangzhan Zhang, Nikita Karaev, Johannes Schönberger et al. (10 authors)

**Published:** 2026-05-14 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.15195v1) | [PDF](https://arxiv.org/pdf/2605.15195v1.pdf) | [Project Page](http://vggt-omega.github.io/)

<details>
<summary>Abstract</summary>

Recent feed-forward reconstruction models, such as VGGT, have proven competitive with traditional optimization-based reconstructors while also providing geometry-aware features useful for other tasks. Here, we show that the quality of these models scales predictably with model and data size. We do so by introducing VGGT-$Ω$, which substantially improves reconstruction accuracy, efficiency, and capabilities for both static and dynamic scenes. To enable training this model at an unprecedented scal...

</details>

---

### [FrameSkip: Learning from Fewer but More Informative Frames in VLA Training](https://arxiv.org/abs/2605.13757v1)

**Authors:** Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei et al. (11 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.13757v1) | [PDF](https://arxiv.org/pdf/2605.13757v1.pdf) | [GitHub](https://github.com/ZGC-EmbodyAI/FrameSkip)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) policies are commonly trained from dense robot demonstration trajectories, often collected through teleoperation, by sampling every recorded frame as if it provided equally useful supervision. We argue that this convention creates a temporal supervision imbalance: long low-change segments dominate the training stream, while manipulation-critical transitions such as alignment, contact, grasping, and release appear only sparsely. We introduce FrameSkip, a data-layer fr...

</details>

---

### [Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models](https://arxiv.org/abs/2605.13632v1)

**Authors:** Yiran Ling, Qing Lian, Jinghang Li, Qing Jiang, Tianming Zhang et al. (9 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.13632v1) | [PDF](https://arxiv.org/pdf/2605.13632v1.pdf) | [Project Page](https://signalispupupu.github.io/GTA-VLA_ProjPage/)

<details>
<summary>Abstract</summary>

In this paper, we propose GTA-VLA(Guide, Think, Act), an interactive Vision-Language-Action (VLA) framework that enables spatially steerable embodied reasoning by allowing users to guide robot policies with explicit visual cues. Existing VLA models learn a direct "Sense-to-Act" mapping from multimodal observations to robot actions. While effective within the training distribution, such tightly coupled policies are brittle under out-of-domain (OOD) shifts and difficult to correct when failures oc...

</details>

---

### [What Limits Vision-and-Language Navigation ?](https://arxiv.org/abs/2605.13328v1)

**Authors:** Yunheng Wang, Yuetong Fang, Taowen Wang, Lusong Li, Kun Liu et al. (12 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.13328v1) | [PDF](https://arxiv.org/pdf/2605.13328v1.pdf) | [Project Page](https://yunheng-wang.github.io/stereonav-public.github.io)

<details>
<summary>Abstract</summary>

Vision-and-Language Navigation (VLN) is a cornerstone of embodied intelligence. However, current agents often suffer from significant performance degradation when transitioning from simulation to real-world deployment, primarily due to perceptual instability (e.g., lighting variations and motion blur) and under-specified instructions. While existing methods attempt to bridge this gap by scaling up model size and training data, we argue that the bottleneck lies in the lack of robust spatial groun...

</details>

---

## Other Recent Papers

### [Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction](https://arxiv.org/abs/2605.15157v1)

**Authors:** Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin et al. (8 authors)

**Published:** 2026-05-14 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.15157v1) | [PDF](https://arxiv.org/pdf/2605.15157v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are prone to compounding errors in dexterous manipulation, where high-dimensional action spaces and contact-rich dynamics amplify small policy deviations over long horizons. While Interactive Imitation Learning (IIL) can refine policies through human takeover data, applying it to high-degree-of-freedom (DoF) robotic hands remains challenging due to a command mismatch between human teleoperation and policy execution at the takeover moment, which causes abrupt r...

</details>

---

### [Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model](https://arxiv.org/abs/2605.14950v1)

**Authors:** Tao Lin, Yuxin Du, Jiting Liu, Nuobei Zhu, Yunhe Li et al. (17 authors)

**Published:** 2026-05-14 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.14950v1) | [PDF](https://arxiv.org/pdf/2605.14950v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models have emerged as a promising paradigm for robotic manipulation by unifying perception, language grounding, and action generation. However, they often struggle in scenarios requiring precise spatial understanding, as current VLA models primarily rely on 2D visual representations that lack depth information and detailed spatial relationships. While recent approaches incorporate explicit 3D inputs such as depth maps or point clouds to address this issue, they often incr...

</details>

---

### [MAPLE: Latent Multi-Agent Play for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.14201v1)

**Authors:** Rajeev Yasarla, Deepti Hegde, Hsin-Pai Cheng, Shizhong Han, Yunxiao Shi et al. (12 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.14201v1) | [PDF](https://arxiv.org/pdf/2605.14201v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are effective as end-to-end motion planners, but can be brittle when evaluated in closed-loop settings due to being trained under traditional imitation learning framework. Existing closed-loop supervision approaches lack scalability and fail to completely model a reactive environment. We propose MAPLE, a novel framework for reactive, multi-agent rollout of a dynamic driving scenario in the latent space of the VLA model. The ego vehicle and nearby traffic agent...

</details>

---

### [Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs](https://arxiv.org/abs/2605.13778v1)

**Authors:** Jiahui Niu, Kefan Gu, Yucheng Zhao, Shengwen Liang, Tiancai Wang et al. (8 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.13778v1) | [PDF](https://arxiv.org/pdf/2605.13778v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion-based vision-language-action models (dVLAs) are promising for embodied intelligence but are fundamentally limited in real-time deployment by the high latency of full inference. We propose Realtime-VLA FLASH, a speculative inference framework that eliminates most full inference calls during replanning by introducing a lightweight draft model with parallel verification via the main model's Action Expert and a phase-aware fallback mechanism that reverts to the full inference pipeline when...

</details>

---

### [AttenA+: Rectifying Action Inequality in Robotic Foundation Models](https://arxiv.org/abs/2605.13548v1)

**Authors:** Daojie Peng, Fulong Ma, Jiahang Cao, Qiang Zhang, Xupeng Xie et al. (10 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2605.13548v1) | [PDF](https://arxiv.org/pdf/2605.13548v1.pdf)

<details>
<summary>Abstract</summary>

Existing robotic foundation models, while powerful, are predicated on an implicit assumption of temporal homogeneity: treating all actions as equally informative during optimization. This "flat" training paradigm, inherited from language modeling, remains indifferent to the underlying physical hierarchy of manipulation. In reality, robot trajectories are fundamentally heterogeneous, where low-velocity segments often dictate task success through precision-demanding interactions, while high-veloci...

</details>

---

### [RotVLA: Rotational Latent Action for Vision-Language-Action Model](https://arxiv.org/abs/2605.13403v1)

**Authors:** Qiwei Li, Xicheng Gong, Xinghang Li, Peiyan Li, Quanyun Zhou et al. (8 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.13403v1) | [PDF](https://arxiv.org/pdf/2605.13403v1.pdf)

<details>
<summary>Abstract</summary>

Latent Action Models (LAMs) have emerged as an effective paradigm for handling heterogeneous datasets during Vision-Language-Action (VLA) model pretraining, offering a unified action space across embodiments. However, existing LAMs often rely on discrete quantization encode and decode pipelines, which can lead to trivial frame reconstruction behavior, limited representational capacity, and a lack of physically meaningful structure. We introduce RotVLA, a VLA framework built on a continuous rotat...

</details>

---

### [BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning](https://arxiv.org/abs/2605.13382v1)

**Authors:** Ruiheng Wang, Shuanghao Bai, Haoran Zhang, Badong Chen, Xiangyu Xu

**Published:** 2026-05-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.13382v1) | [PDF](https://arxiv.org/pdf/2605.13382v1.pdf)

<details>
<summary>Abstract</summary>

While autoregressive (AR) Vision-Language-Action (VLA) models have demonstrated formidable reasoning capabilities in robotic tasks, their sequential decoding process often incurs high inference latency and may amplify error accumulation during long-horizon execution. Discrete Diffusion Language Models (dLLMs) provide a promising alternative through parallel token refinement, but their practical deployment in robotics remains limited by repeated denoising function evaluations (NFEs) and the diffi...

</details>

---

### [D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models](https://arxiv.org/abs/2605.13276v2)

**Authors:** Yucheng Guo, Yongjian Guo, Zhong Guan, Wen Huang, Haoran Sun et al. (12 authors)

**Published:** 2026-05-13 | **Categories:** cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.13276v2) | [PDF](https://arxiv.org/pdf/2605.13276v2.pdf)

<details>
<summary>Abstract</summary>

The rapid evolution of Embodied AI has enabled Vision-Language-Action (VLA) models to excel in multimodal perception and task execution. However, applying Reinforcement Learning (RL) to these massive models in large-scale distributed environments faces severe systemic bottlenecks, primarily due to the resource conflict between high-fidelity physical simulation and the intensive VRAM/bandwidth demands of deep learning. This conflict often leaves overall throughput constrained by execution-phase i...

</details>

---

### [Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models](https://arxiv.org/abs/2605.13119v1)

**Authors:** Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding et al. (8 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.13119v1) | [PDF](https://arxiv.org/pdf/2605.13119v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are effective robot action executors, but they remain limited on long-horizon tasks due to the dual burden of extended closed-loop planning and diverse physical operations. We therefore propose VLAs-as-Tools, a strategy that distributes this burden across a high-level vision language model (VLM) agent for temporal reasoning and a family of specialized VLA tools for diverse local physical operations. The VLM handles scene analysis, global planning, and recovery...

</details>

---

### [What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models](https://arxiv.org/abs/2605.13105v1)

**Authors:** Yuanfang Peng, Jingjing Fu, Chuheng Zhang, Li Zhao, Jiang Bian et al. (9 authors)

**Published:** 2026-05-13 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.13105v1) | [PDF](https://arxiv.org/pdf/2605.13105v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) fine-tuning has shown promise for Vision-Language-Action (VLA) models in robotic manipulation, but deployment-time visual shifts pose practical challenges. A key difficulty is that standard task rewards supervise task success, but offer limited guidance on whether a visual change is task-irrelevant or changes the behavior required for manipulation. We propose PAIR-VLA (Paired Action Invariance & Sensitivity for Visually Robust VLA), an RL fine-tuning framework to addr...

</details>

---
