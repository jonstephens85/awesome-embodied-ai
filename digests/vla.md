# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-02-27 16:40 UTC

**Papers found:** 9

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation](https://arxiv.org/abs/2602.22896v1)

**Authors:** Zebin Yang, Yijiahao Qi, Tong Xie, Bo Yu, Shaoshan Liu et al. (6 authors)

**Published:** 2026-02-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.22896v1) | [PDF](https://arxiv.org/pdf/2602.22896v1.pdf) | [GitHub](https://github.com/PKU-SEC-Lab/DYSL_VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown remarkable success in robotic tasks like manipulation by fusing a language model's reasoning with a vision model's 3D understanding. However, their high computational cost remains a major obstacle for real-world applications that require real-time performance. We observe that the actions within a task have varying levels of importance: critical steps demand high precision, while less important ones can tolerate more variance. Leveraging this insight...

</details>

---

### [World Guidance: World Modeling in Condition Space for Action Generation](https://arxiv.org/abs/2602.22010v1)

**Authors:** Yue Su, Sijin Chen, Haixin Shi, Mingyu Liu, Zhengshen Zhang et al. (10 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.22010v1) | [PDF](https://arxiv.org/pdf/2602.22010v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Leveraging future observation modeling to facilitate action generation presents a promising avenue for enhancing the capabilities of Vision-Language-Action (VLA) models. However, existing approaches struggle to strike a balance between maintaining efficient, predictable future representations and preserving sufficient fine-grained information to guide precise action generation. To address this limitation, we propose WoG (World Guidance), a framework that maps future observations into compact con...

</details>

---

### [Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633v1)

**Authors:** Chenyv Liu, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li et al. (7 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.21633v1) | [PDF](https://arxiv.org/pdf/2602.21633v1.pdf) | [GitHub](https://github.com/Kisaragi0/SC-VLA)

<details>
<summary>Abstract</summary>

Standard vision-language-action (VLA) models rely on fitting statistical data priors, limiting their robust understanding of underlying physical dynamics. Reinforcement learning enhances physical grounding through exploration yet typically relies on external reward signals that remain isolated from the agent's internal states. World action models have emerged as a promising paradigm that integrates imagination and control to enable predictive planning. However, they rely on implicit context mode...

</details>

---

### [LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies](https://arxiv.org/abs/2602.21531v1)

**Authors:** Yue Yang, Shuo Cheng, Yu Fang, Homanga Bharadhwaj, Mingyu Ding et al. (7 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2602.21531v1) | [PDF](https://arxiv.org/pdf/2602.21531v1.pdf) | [Project Page](https://yy-gx.github.io/LiLo-VLA/)

<details>
<summary>Abstract</summary>

General-purpose robots must master long-horizon manipulation, defined as tasks involving multiple kinematic structure changes (e.g., attaching or detaching objects) in unstructured environments. While Vision-Language-Action (VLA) models offer the potential to master diverse atomic skills, they struggle with the combinatorial complexity of sequencing them and are prone to cascading failures due to environmental sensitivity. To address these challenges, we propose LiLo-VLA (Linked Local VLA), a mo...

</details>

---

## Other Recent Papers

### [Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline](https://arxiv.org/abs/2602.22663v1)

**Authors:** Wenxuan Song, Jiayi Chen, Xiaoquan Sun, Huashuo Lei, Yikai Qin et al. (15 authors)

**Published:** 2026-02-26 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.22663v1) | [PDF](https://arxiv.org/pdf/2602.22663v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have emerged as a generalist robotic agent. However, existing VLAs are hindered by excessive parameter scales, prohibitive pre-training requirements, and limited applicability to diverse embodiments. To improve the practicality of VLAs, we propose a comprehensive benchmark and an improved baseline. First, we propose CEBench, a new benchmark spanning diverse embodiments in both simulation and the real world with consideration of domain randomization. We collect...

</details>

---

### [Metamorphic Testing of Vision-Language Action-Enabled Robots](https://arxiv.org/abs/2602.22579v1)

**Authors:** Pablo Valle, Sergio Segura, Shaukat Ali, Aitor Arrieta

**Published:** 2026-02-26 | **Categories:** cs.RO, cs.SE

**Links:** [arXiv](https://arxiv.org/abs/2602.22579v1) | [PDF](https://arxiv.org/pdf/2602.22579v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are multimodal robotic task controllers that, given an instruction and visual inputs, produce a sequence of low-level control actions (or motor commands) enabling a robot to execute the requested task in the physical environment. These systems face the test oracle problem from multiple perspectives. On the one hand, a test oracle must be defined for each instruction prompt, which is a complex and non-generalizable approach. On the other hand, current state-of-...

</details>

---

### [SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation](https://arxiv.org/abs/2602.22514v1)

**Authors:** Xinyu Tan, Ningwei Bai, Harry Gardener, Zhengyang Zhong, Luoyu Zhang et al. (9 authors)

**Published:** 2026-02-26 | **Categories:** cs.RO, cs.AI, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2602.22514v1) | [PDF](https://arxiv.org/pdf/2602.22514v1.pdf)

<details>
<summary>Abstract</summary>

We present, to our knowledge, the first sign language-driven Vision-Language-Action (VLA) framework for intuitive and inclusive human-robot interaction. Unlike conventional approaches that rely on gloss annotations as intermediate supervision, the proposed system adopts a gloss-free paradigm and directly maps visual sign gestures to semantic instructions. This design reduces annotation cost and avoids the information loss introduced by gloss representations, enabling more natural and scalable mu...

</details>

---

### [Are Foundation Models the Route to Full-Stack Transfer in Robotics?](https://arxiv.org/abs/2602.22001v1)

**Authors:** Freek Stulp, Samuel Bustamante, João Silvério, Alin Albu-Schäffer, Jeannette Bohg et al. (6 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.22001v1) | [PDF](https://arxiv.org/pdf/2602.22001v1.pdf)

<details>
<summary>Abstract</summary>

In humans and robots alike, transfer learning occurs at different levels of abstraction, from high-level linguistic transfer to low-level transfer of motor skills. In this article, we provide an overview of the impact that foundation models and transformer networks have had on these different levels, bringing robots closer than ever to "full-stack transfer". Considering LLMs, VLMs and VLAs from a robotic transfer learning perspective allows us to highlight recurring concepts for transfer, beyond...

</details>

---

### [Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild](https://arxiv.org/abs/2602.21736v1)

**Authors:** Hao Luo, Ye Wang, Wanpeng Zhang, Haoqi Yuan, Yicheng Feng et al. (8 authors)

**Published:** 2026-02-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2602.21736v1) | [PDF](https://arxiv.org/pdf/2602.21736v1.pdf)

<details>
<summary>Abstract</summary>

Despite progress, Vision-Language-Action models (VLAs) are limited by a scarcity of large-scale, diverse robot data. While human manipulation videos offer a rich alternative, existing methods are forced to choose between small, precisely-labeled datasets and vast in-the-wild footage with unreliable hand tracking labels. We present JALA, a pretraining framework that learns Jointly-Aligned Latent Actions. JALA bypasses full visual dynamic reconstruction, instead learns a predictive action embeddin...

</details>

---
