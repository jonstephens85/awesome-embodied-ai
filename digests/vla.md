# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-03-18 22:24 UTC

**Papers found:** 16

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666v1)

**Authors:** Tianyuan Yuan, Zibin Dong, Yicheng Liu, Hang Zhao

**Published:** 2026-03-17 | **Categories:** cs.CV, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.16666v1) | [PDF](https://arxiv.org/pdf/2603.16666v1.pdf) | [Project Page](https://yuantianyuan01.github.io/FastWAM/)

<details>
<summary>Abstract</summary>

World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance. In this paper, we ask whether WAMs need explicit f...

</details>

---

### [Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation](https://arxiv.org/abs/2603.16086v1)

**Authors:** Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu, Hesheng Wang

**Published:** 2026-03-17 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.16086v1) | [PDF](https://arxiv.org/pdf/2603.16086v1.pdf) | [Project Page](are)

<details>
<summary>Abstract</summary>

While recent Vision-Language-Action (VLA) models have begun to incorporate audio, they typically treat sound as static pre-execution prompts or focus exclusively on human speech. This leaves a significant gap in real-time, sound-centric manipulation where fleeting environmental acoustics provide critical state verification during task execution. Consequently, key sounds are easily missed due to low-frequency updates or system latency. This problem is exacerbated by action chunking with open-loop...

</details>

---

### [Towards Generalizable Robotic Manipulation in Dynamic Environments](https://arxiv.org/abs/2603.15620v1)

**Authors:** Heng Fang, Shangru Li, Shuhan Wang, Xuanyang Xi, Dingkang Liang et al. (6 authors)

**Published:** 2026-03-16 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.15620v1) | [PDF](https://arxiv.org/pdf/2603.15620v1.pdf) | [GitHub](https://github.com/H-EmbodVis/DOMINO)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models excel in static manipulation but struggle in dynamic environments with moving targets. This performance gap primarily stems from a scarcity of dynamic manipulation datasets and the reliance of mainstream VLAs on single-frame observations, restricting their spatiotemporal reasoning capabilities. To address this, we introduce DOMINO, a large-scale dataset and benchmark for generalizable dynamic manipulation, featuring 35 tasks with hierarchical complexities, ove...

</details>

---

### [RoCo Challenge at AAAI 2026: Benchmarking Robotic Collaborative Manipulation for Assembly Towards Industrial Automation](https://arxiv.org/abs/2603.15469v1)

**Authors:** Haichao Liu, Yuheng Zhou, Zhenyu Wu, Ziheng Ji, Ziyu Shan et al. (17 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.15469v1) | [PDF](https://arxiv.org/pdf/2603.15469v1.pdf) | [Project Page](https://rocochallenge.github.io/RoCo2026/)

<details>
<summary>Abstract</summary>

Embodied Artificial Intelligence (EAI) is rapidly developing, gradually subverting previous autonomous systems' paradigms from isolated perception to integrated, continuous action. This transition is highly significant for industrial robotic manipulation, promising to free human workers from repetitive, dangerous daily labor. To benchmark and advance this capability, we introduce the Robotic Collaborative Assembly Assistance (RoCo) Challenge with a dataset towards simulation and real-world assem...

</details>

---

### [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](https://arxiv.org/abs/2603.15169v1)

**Authors:** Yang Li,  Zhaxizhuoma, Hongru Jiang, Junjie Xia, Hongquan Zhang et al. (14 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.15169v1) | [PDF](https://arxiv.org/pdf/2603.15169v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Embodied intelligence for contact-rich manipulation has predominantly relied on position control, while explicit awareness and regulation of interaction forces remain under-explored, limiting stability, precision, and robustness in real-world tasks. We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness. ForceVLA2 introduces force-based prompts into the VLM expert to construct force-aware task concep...

</details>

---

### [AutoMoT: A Unified Vision-Language-Action Model with Asynchronous Mixture-of-Transformers for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.14851v1)

**Authors:** Wenhui Huang, Songyan Zhang, Qihang Huang, Zhidong Wang, Zhiqi Mao et al. (9 authors)

**Published:** 2026-03-16 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.14851v1) | [PDF](https://arxiv.org/pdf/2603.14851v1.pdf) | [Project Page](https://automot-website.github.io/}{Project)

<details>
<summary>Abstract</summary>

Integrating vision-language models (VLMs) into end-to-end (E2E) autonomous driving (AD) systems has shown promise in improving scene understanding. However, existing integration strategies suffer from several limitations: they either struggle to resolve distribution misalignment between reasoning and action spaces, underexploit the general reasoning capabilities of pretrained VLMs, or incur substantial inference latency during action policy generation, which degrades driving performance. To addr...

</details>

---

## Other Recent Papers

### [Enabling Dynamic Tracking in Vision-Language-Action Models via Time-Discrete and Time-Continuous Velocity Feedforward](https://arxiv.org/abs/2603.16218v1)

**Authors:** Johannes Hechtl, Philipp Schmitt, Georg von Wichert, Wolfram Burgard

**Published:** 2026-03-17 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.16218v1) | [PDF](https://arxiv.org/pdf/2603.16218v1.pdf)

<details>
<summary>Abstract</summary>

While vision-language-action (VLA) models have shown great promise for robot manipulation, their deployment on rigid industrial robots remains challenging due to the inherent trade-off between compliance and responsiveness. Standard Behavior Cloning (BC) approaches predict discrete poses at low frequencies, omitting the velocity and acceleration feedforward terms typically used by low-level compliant controllers. This requires to rely on high stiffness for accurate tracking, thereby sacrificing ...

</details>

---

### [Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation](https://arxiv.org/abs/2603.16044v1)

**Authors:** Dongik Shin

**Published:** 2026-03-17 | **Categories:** cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.16044v1) | [PDF](https://arxiv.org/pdf/2603.16044v1.pdf)

<details>
<summary>Abstract</summary>

Generalization remains a core challenge in embodied AI, as robots must adapt to diverse environments. While OpenVLA represents the State-of-the-Art (SOTA) in Vision-Language-Action models by leveraging large-scale pre-training, its zero-shot performance can be limited when encountering completely new environments. This paper proposes a parameter-efficient fine-tuning strategy to enhance the linguistic generalization of OpenVLA by synthesizing a general instruction set for the Bridge Dataset V2. ...

</details>

---

### [Safety Case Patterns for VLA-based driving systems: Insights from SimLingo](https://arxiv.org/abs/2603.16013v1)

**Authors:** Gerhard Yu, Fuyuki Ishikawa, Oluwafemi Odu, Alvine Boaye Belle

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.SE

**Links:** [arXiv](https://arxiv.org/abs/2603.16013v1) | [PDF](https://arxiv.org/pdf/2603.16013v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA)-based driving systems represent a significant paradigm shift in autonomous driving since, by combining traffic scene understanding, linguistic interpretation, and action generation, these systems enable more flexible, adaptive, and instruction-responsive driving behaviors. However, despite their growing adoption and potential to support socially responsible autonomous driving while understanding high-level human instructions, VLA-based driving systems may exhibit new...

</details>

---

### [You've Got a Golden Ticket: Improving Generative Robot Policies With A Single Noise Vector](https://arxiv.org/abs/2603.15757v1)

**Authors:** Omkar Patil, Ondrej Biza, Thomas Weng, Karl Schmeckpeper, Wil Thomason et al. (10 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.15757v1) | [PDF](https://arxiv.org/pdf/2603.15757v1.pdf)

<details>
<summary>Abstract</summary>

What happens when a pretrained generative robot policy is provided a constant initial noise as input, rather than repeatedly sampling it from a Gaussian? We demonstrate that the performance of a pretrained, frozen diffusion or flow matching policy can be improved with respect to a downstream reward by swapping the sampling of initial noise from the prior distribution (typically isotropic Gaussian) with a well-chosen, constant initial noise input -- a golden ticket. We propose a search method to ...

</details>

---

### [Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models](https://arxiv.org/abs/2603.15618v2)

**Authors:** Yulin Luo, Hao Chen, Zhuangzhe Wu, Bowen Sui, Jiaming Liu et al. (13 authors)

**Published:** 2026-03-16 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2603.15618v2) | [PDF](https://arxiv.org/pdf/2603.15618v2.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for robotic manipulation, in which reliable action prediction critically depends on accurately interpreting and integrating visual observations conditioned on language instructions. Although recent works have sought to enhance the visual capabilities of VLA models, most approaches treat the LLM backbone as a black box, providing limited insight into how visual information is grounded into action generation. Therefo...

</details>

---

### [MA-VLCM: A Vision Language Critic Model for Value Estimation of Policies in Multi-Agent Team Settings](https://arxiv.org/abs/2603.15418v1)

**Authors:** Shahil Shaik, Aditya Parameshwaran, Anshul Nayak, Jonathon M. Smereka, Yue Wang

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.15418v1) | [PDF](https://arxiv.org/pdf/2603.15418v1.pdf)

<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) commonly relies on a centralized critic to estimate the value function. However, learning such a critic from scratch is highly sample-inefficient and often lacks generalization across environments. At the same time, large vision-language-action models (VLAs) trained on internet-scale data exhibit strong multimodal reasoning and zero-shot generalization capabilities, yet directly deploying them for robotic execution remains computationally prohibitive, pa...

</details>

---

### [HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing](https://arxiv.org/abs/2603.15257v1)

**Authors:** Konstantin Gubernatorov, Mikhail Sannikov, Ilya Mikhalchuk, Egor Kuznetsov, Makar Artemov et al. (10 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.15257v1) | [PDF](https://arxiv.org/pdf/2603.15257v1.pdf)

<details>
<summary>Abstract</summary>

Tactile sensing is a crucial capability for Vision-Language-Action (VLA) architectures, as it enables dexterous and safe manipulation in contact-rich tasks. However, reliance on dedicated tactile hardware increases cost and reduces reproducibility across robotic platforms. We argue that tactile-aware manipulation can be learned offline and deployed without direct haptic feedback at inference. To this end, we present HapticVLA, which proceeds in two tightly coupled stages: Safety-Aware Reward-Wei...

</details>

---

### [NavGSim: High-Fidelity Gaussian Splatting Simulator for Large-Scale Navigation](https://arxiv.org/abs/2603.15186v1)

**Authors:** Jiahang Liu, Yuanxing Duan, Jiazhao Zhang, Minghan Li, Shaoan Wang et al. (7 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.15186v1) | [PDF](https://arxiv.org/pdf/2603.15186v1.pdf)

<details>
<summary>Abstract</summary>

Simulating realistic environments for robots is widely recognized as a critical challenge in robot learning, particularly in terms of rendering and physical simulation. This challenge becomes even more pronounced in navigation tasks, where trajectories often extend across multiple rooms or entire floors. In this work, we present NavGSim, a Gaussian Splatting-based simulator designed to generate high-fidelity, large-scale navigation environments. Built upon a hierarchical 3D Gaussian Splatting fr...

</details>

---

### [AnoleVLA: Lightweight Vision-Language-Action Model with Deep State Space Models for Mobile Manipulation](https://arxiv.org/abs/2603.15046v1)

**Authors:** Yusuke Takagi, Motonari Kambara, Daichi Yashima, Koki Seno, Kento Tokura et al. (6 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2603.15046v1) | [PDF](https://arxiv.org/pdf/2603.15046v1.pdf)

<details>
<summary>Abstract</summary>

In this study, we address the problem of language-guided robotic manipulation, where a robot is required to manipulate a wide range of objects based on visual observations and natural language instructions. This task is essential for service robots that operate in human environments, and requires safety, efficiency, and task-level generality. Although Vision-Language-Action models (VLAs) have demonstrated strong performance for this task, their deployment in resource-constrained environments rem...

</details>

---

### [Learning from Mistakes: Post-Training for Driving VLA with Takeover Data](https://arxiv.org/abs/2603.14972v1)

**Authors:** Yinfeng Gao, Deqing Liu, Qichao Zhang, Yupeng Zheng, Haochen Tian et al. (10 authors)

**Published:** 2026-03-16 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2603.14972v1) | [PDF](https://arxiv.org/pdf/2603.14972v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision-Language-Action (VLA) paradigms in end-to-end autonomous driving rely on offline training from static datasets, leaving them vulnerable to distribution shift. Recent post-training methods use takeover data to mitigate this by augmenting the dataset with high-quality expert takeover samples, yet they suffer from two key limitations: supervision restricted to the period after the takeover moments leads to policies with limited safety margins, and passive preference optimization lack...

</details>

---
