# World Models

Papers on world models for robotics, video prediction, and simulation.

**Last updated:** 2026-01-31 22:13 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998v1)

**Authors:** Lin Li, Qihang Zhang, Yiming Luo, Shuai Yang, Ruilin Wang et al. (12 authors)

**Published:** 2026-01-29 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.21998v1) | [PDF](https://arxiv.org/pdf/2601.21998v1.pdf) | [Project Page](https://technology.robbyant.com/lingbot-va) | [GitHub](https://github.com/robbyant/lingbot-va)

<details>
<summary>Abstract</summary>

This work highlights that video world modeling, alongside vision-language pre-training, establishes a fresh and independent foundation for robot learning. Intuitively, video world models provide the ability to imagine the near future by understanding the causality between actions and visual dynamics. Inspired by this, we introduce LingBot-VA, an autoregressive diffusion framework that learns frame prediction and policy execution simultaneously. Our model features three carefully crafted designs:...

</details>

---

### [WorldBench: Disambiguating Physics for Diagnostic Evaluation of World Models](https://arxiv.org/abs/2601.21282v1)

**Authors:** Rishi Upadhyay, Howard Zhang, Jim Solomon, Ayush Agrawal, Pranay Boreddy et al. (10 authors)

**Published:** 2026-01-29 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.21282v1) | [PDF](https://arxiv.org/pdf/2601.21282v1.pdf) | [Project Page](https://world-bench.github.io/)

<details>
<summary>Abstract</summary>

Recent advances in generative foundational models, often termed "world models," have propelled interest in applying them to critical tasks like robotic planning and autonomous system training. For reliable deployment, these models must exhibit high physical fidelity, accurately simulating real-world dynamics. Existing physics-based video benchmarks, however, suffer from entanglement, where a single test simultaneously evaluates multiple physical laws and concepts, fundamentally limiting their di...

</details>

---

## Other Recent Papers

### [DynaWeb: Model-Based Reinforcement Learning of Web Agents](https://arxiv.org/abs/2601.22149v1)

**Authors:** Hang Ding, Peidong Liu, Junqiao Wang, Ziwei Ji, Meng Cao et al. (10 authors)

**Published:** 2026-01-29 | **Categories:** cs.CL, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2601.22149v1) | [PDF](https://arxiv.org/pdf/2601.22149v1.pdf)

<details>
<summary>Abstract</summary>

The development of autonomous web agents, powered by Large Language Models (LLMs) and reinforcement learning (RL), represents a significant step towards general-purpose AI assistants. However, training these agents is severely hampered by the challenges of interacting with the live internet, which is inefficient, costly, and fraught with risks. Model-based reinforcement learning (MBRL) offers a promising solution by learning a world model of the environment to enable simulated interaction. This ...

</details>

---

### [World of Workflows: a Benchmark for Bringing World Models to Enterprise Systems](https://arxiv.org/abs/2601.22130v1)

**Authors:** Lakshya Gupta, Litao Li, Yizhe Liu, Sriram Ganapathi Subramanian, Kaheer Suleman et al. (8 authors)

**Published:** 2026-01-29 | **Categories:** cs.AI, cs.SE

**Links:** [arXiv](https://arxiv.org/abs/2601.22130v1) | [PDF](https://arxiv.org/pdf/2601.22130v1.pdf)

<details>
<summary>Abstract</summary>

Frontier large language models (LLMs) excel as autonomous agents in many domains, yet they remain untested in complex enterprise systems where hidden workflows create cascading effects across interconnected databases. Existing enterprise benchmarks evaluate surface-level agentic task completion similar to general consumer benchmarks, ignoring true challenges in enterprises, such as limited observability, large database state, and hidden workflows with cascading side effects. We introduce World o...

</details>

---

### [The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR](https://arxiv.org/abs/2601.22128v1)

**Authors:** Irsyad Adam, Zekai Chen, David Laprade, Shaun Porwal, David Laub et al. (8 authors)

**Published:** 2026-01-29 | **Categories:** cs.AI, cs.CE, q-bio.QM

**Links:** [arXiv](https://arxiv.org/abs/2601.22128v1) | [PDF](https://arxiv.org/pdf/2601.22128v1.pdf)

<details>
<summary>Abstract</summary>

Large language models (LLMs) trained with next-word-prediction have achieved success as clinical foundation models. Representations from these language backbones yield strong linear probe performance across biomedical tasks, suggesting that patient semantics emerge from next-token prediction at scale. However, this paradigm treats patients as a document to be summarized rather than a dynamical system to be simulated; a patient's trajectory emerges from their state evolving under interventions an...

</details>

---

### [Learning Transient Convective Heat Transfer with Geometry Aware World Models](https://arxiv.org/abs/2601.22086v1)

**Authors:** Onur T. Doganay, Alexander Klawonn, Martin Eigel, Hanno Gottschalk

**Published:** 2026-01-29 | **Categories:** physics.flu-dyn, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.22086v1) | [PDF](https://arxiv.org/pdf/2601.22086v1.pdf)

<details>
<summary>Abstract</summary>

Partial differential equation (PDE) simulations are fundamental to engineering and physics but are often computationally prohibitive for real-time applications. While generative AI offers a promising avenue for surrogate modeling, standard video generation architectures lack the specific control and data compatibility required for physical simulations. This paper introduces a geometry aware world model architecture, derived from a video generation architecture (LongVideoGAN), designed to learn t...

</details>

---

### [Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving](https://arxiv.org/abs/2601.22032v1)

**Authors:** Linhan Wang, Zichong Yang, Chen Bai, Guoxiang Zhang, Xiaotong Liu et al. (9 authors)

**Published:** 2026-01-29 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2601.22032v1) | [PDF](https://arxiv.org/pdf/2601.22032v1.pdf)

<details>
<summary>Abstract</summary>

End-to-end autonomous driving increasingly leverages self-supervised video pretraining to learn transferable planning representations. However, pretraining video world models for scene understanding has so far brought only limited improvements. This limitation is compounded by the inherent ambiguity of driving: each scene typically provides only a single human trajectory, making it difficult to learn multimodal behaviors. In this work, we propose Drive-JEPA, a framework that integrates Video Joi...

</details>

---

### [Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control](https://arxiv.org/abs/2601.21363v1)

**Authors:** Weidong Huang, Zhehan Li, Hangxin Liu, Biao Hou, Yao Su et al. (6 authors)

**Published:** 2026-01-29 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2601.21363v1) | [PDF](https://arxiv.org/pdf/2601.21363v1.pdf)

<details>
<summary>Abstract</summary>

Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on...

</details>

---
