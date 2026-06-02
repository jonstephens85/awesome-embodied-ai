# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-02 23:27 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models](https://arxiv.org/abs/2606.02277v1)

**Authors:** Bin Yu, Yao Zhang, Haishan Liu, Shijie Lian, Yuliang Wei et al. (12 authors)

**Published:** 2026-06-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.02277v1) | [PDF](https://arxiv.org/pdf/2606.02277v1.pdf) | [GitHub](https://github.com/ZGC-EmbodyAI/RoboSemanticBench)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are built on the premise that semantic understanding from pretrained language or vision-language backbones should guide robot action prediction. Yet robot fine-tuning is optimized as imitation over task-specific action distributions, and many evaluations can be solved through visual or instruction-action shortcuts. We introduce RoboSemanticBench (RSB), an embodied benchmark for diagnosing semantic grounding in action prediction: whether post-trained VLA models...

</details>

---

### [LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World](https://arxiv.org/abs/2606.01458v1)

**Authors:** Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen et al. (7 authors)

**Published:** 2026-05-31 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.01458v1) | [PDF](https://arxiv.org/pdf/2606.01458v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Training vision-language-action (VLA) policies for humanoid loco-manipulation is constrained by the high cost and complexity of collecting human teleoperation demonstrations. VLA policies fine-tuned in simulators have, until now, failed to transfer effectively in humanoid loco-manipulation tasks. We present LEGS (Loco-manipulation via Embodied Gaussian Splatting), a hybrid simulator that composites a mesh foreground (robot, objects, props) over a photorealistic 3D Gaussian Splatting (3DGS) backg...

</details>

---

### [Make Your VLA More Robust Without More Data By Interleaving Motion Planning](https://arxiv.org/abs/2606.00985v1)

**Authors:** Dan BW Choe, Sundhar Vinodh Sangeetha, Samuel Coogan, Shreyas Kousik

**Published:** 2026-05-31 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.00985v1) | [PDF](https://arxiv.org/pdf/2606.00985v1.pdf) | [Project Page](https://mpvi.netlify.app/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown remarkable progress for mobile manipulation, but their performance on long-horizon tasks remains poor. These tasks are especially challenging because (1) progress toward high-level goals must be maintained across extended sequences of spatially distributed subtasks, and (2) early execution errors compound rapidly over the task horizon. These challenges persist despite finetuning on large human teleoperated mobile manipulation data, indicating that m...

</details>

---

### [Lagrangian Perturbation Diffusion Steering: Latent Reinforcement Learning for Generative Policies](https://arxiv.org/abs/2606.01151v1)

**Authors:** Hikmet Simsir, Ozgur S. Oguz

**Published:** 2026-05-31 | **Categories:** cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.01151v1) | [PDF](https://arxiv.org/pdf/2606.01151v1.pdf) | [Project Page](https://sites.google.com/view/lp-ds/home)

<details>
<summary>Abstract</summary>

Behavior cloning with high-capacity generative policies achieves strong imitation performance, but is often limited by demonstration coverage and distribution shift. Direct reinforcement learning fine-tuning can improve performance, but updating large action decoders is frequently unstable and sample inefficient. We propose Lagrangian Perturbation Diffusion Steering (LP-DS), a lightweight adaptation method that improves a frozen generative policy by learning a compact noise-space perturbation be...

</details>

---

## Other Recent Papers

### [Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](https://arxiv.org/abs/2606.02486v1)

**Authors:** Shahram Najam Syed, Arthur Jakobsson, Haoran Hao, Jeffrey Ichnowski

**Published:** 2026-06-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.02486v1) | [PDF](https://arxiv.org/pdf/2606.02486v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models generalize across static manipulation but fail when objects move during task execution. They map the current observation to an action and assume the scene is stationary between observation and execution, so at any non-trivial object speed the resulting latency exceeds the time available to grasp. We close this gap with AHEAD (Anticipatory Horizon Extrapolation with Adaptive Dynamics), a predict-then-act wrapper that augments a frozen VLA with a motion-aware la...

</details>

---

### [Towards Precise Intent-Aligned VLA Aerial Navigation via Expert-Guided GRPO](https://arxiv.org/abs/2606.02313v1)

**Authors:** Tianyang Chen, Wenjun Li, Xin zhou, Yuze Wu, Fei Gao

**Published:** 2026-06-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.02313v1) | [PDF](https://arxiv.org/pdf/2606.02313v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models offer a promising end-to-end paradigm for unmanned aerial vehicles (UAVs) to accomplish complex tasks specified by fine-grained instructions. However, standard supervised fine-tuning (SFT) suffers from data scarcity, limited generalization, and weak supervision for nuanced and complicated human intents. Reinforcement fine-tuning offers a natural way to mitigate these challenges and align policy behaviors with human intents through designable feedback, but appl...

</details>

---

### [FATE-VLA:Failue-aware test generation for vision-language-action models](https://arxiv.org/abs/2606.02307v1)

**Authors:** Arusa Kanwal, Pablo Valle, Shaukat Ali, Aitor Arrieta

**Published:** 2026-06-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.02307v1) | [PDF](https://arxiv.org/pdf/2606.02307v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are increasingly used as generalist robot policies, yet their evaluation still relies largely on static benchmarks that randomly sample task scenes. In high-dimensional embodied spaces, failures are sparse and clustered, so static benchmarking can underestimate robustness risks. We reframe VLA evaluation as an active failure-discovery problem and propose a failure-aware test-generation approach that combines diversity-driven exploration with surrogate models l...

</details>

---

### [WALL-WM: Carving World Action Modeling at the Event Joints](https://arxiv.org/abs/2606.01955v1)

**Authors:** Shalfun Li, Victor Yao, Charles Yang, Truth Qu, Regis Cheng et al. (31 authors)

**Published:** 2026-06-01 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.01955v1) | [PDF](https://arxiv.org/pdf/2606.01955v1.pdf)

<details>
<summary>Abstract</summary>

WALL-WM is a World Action Model that shifts video-action learning from chunk-centric optimization to event-grounded Vision-Language-Action pretraining, using semantically coherent action events as the atomic unit of learning. Existing WAMs commonly initialize from multimodal or video foundation models and then optimize fixed-length action chunks conditioned directly on the current observation and instruction. Although convenient, this chunk-centric formulation creates a fundamental granularity m...

</details>

---

### [Co-training with Ego-centric Video and Demonstration for Robot Navigation Task](https://arxiv.org/abs/2606.01951v1)

**Authors:** Shoya Kuno, Yumo Ouchi, Kanata Suzuki

**Published:** 2026-06-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.01951v1) | [PDF](https://arxiv.org/pdf/2606.01951v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are promising for diverse robotic tasks, but their performance heavily depends on large-scale high-quality training data, whose collection on real robots is costly and time-consuming. While prior work has explored augmenting manipulation datasets with egocentric human videos, applying such approaches to mobile robot navigation remains challenging due to viewpoint changes during locomotion. In this paper, we propose a framework that converts egocentric walking ...

</details>

---

### [The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space](https://arxiv.org/abs/2606.01847v1)

**Authors:** Bing-Cheng Chuang, I-Hsuan Chu, Bor-Jiun Lin, YuanFu Yang, Min Sun et al. (6 authors)

**Published:** 2026-06-01 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.01847v1) | [PDF](https://arxiv.org/pdf/2606.01847v1.pdf)

<details>
<summary>Abstract</summary>

Diffusion-based Vision-Language-Action policies achieve remarkable success in robotic manipulation, yet commit a fundamental geometric error we term the $\textbf{Euclidean Fallacy}$: representing SE(3) poses as flat $\mathbb{R}^{12}$ vectors. This approximation induces (1) manifold drift violating SO(3) constraints, (2) broken equivariance under coordinate transformations, and (3) non-geodesic trajectories with excessive kinematic cost. We introduce $\textbf{Lie Diffuser Actor (LDA)}$, a diffusi...

</details>

---

### [OneVLA: A Unified Framework for Embodied Tasks](https://arxiv.org/abs/2606.01241v1)

**Authors:** Lingfeng Zhang, Xiaoshuai Hao, Yingbo Tang, Lei Zhou, Shuyi Zhang et al. (13 authors)

**Published:** 2026-05-31 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.01241v1) | [PDF](https://arxiv.org/pdf/2606.01241v1.pdf)

<details>
<summary>Abstract</summary>

Navigation and manipulation are fundamental capabilities of embodied intelligence, enabling robots to interpret natural language commands and interact physically with their surroundings. However, current Vision-Language-Action (VLA) models remain constrained by task-specific architectures, specializing in either navigation or manipulation, which hinders the development of general-purpose robotic agents. To bridge this gap, we introduce OneVLA, a unified architecture that integrates these distinc...

</details>

---

### [ImagineUAV: Aerial Vision-Language Navigation via World-Action Modeling and Kinodynamic Planning](https://arxiv.org/abs/2606.01205v1)

**Authors:** Xuchen Liu, Jiawei Huang, Shihao Xia, Bingxi Liu, Jinqiang Cui et al. (6 authors)

**Published:** 2026-05-31 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.01205v1) | [PDF](https://arxiv.org/pdf/2606.01205v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language navigation (VLN) for UAVs demands grounding free-form instructions into 6-DoF flight under partial observability. While Vision-Language-Action (VLA) models excel at semantic reasoning, they suffer from brittleness due to geometric inconsistency and dynamics mismatch. To address this, we propose ImagineUAV, an imagination-driven framework leveraging cascaded world-action modeling. Instead of direct regression, ImagineUAV employs a latent video diffusion model to generate instructi...

</details>

---

### [Beyond Task Success: Behavioral and Representational Diagnostics for WAM and VLA](https://arxiv.org/abs/2606.01095v1)

**Authors:** Hung Mai, Bin Zhu, Tuan Do

**Published:** 2026-05-31 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.01095v1) | [PDF](https://arxiv.org/pdf/2606.01095v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies and World-Action Models (WAM) represent two increasingly important paradigms for robotic manipulation. However, it remains unclear whether future prediction in WAMs leads to behaviorally meaningful improvements beyond final task success. In this paper, we ask whether WAMs merely add future prediction, or whether they change robot behavior and internal representations in ways that are actionable for control. We introduce a model-agnostic diagnostic framework ...

</details>

---

### [Threading Optimization for Vision-Language-Action Model Inference in Low-Cost Smart Agricultural Manipulation](https://arxiv.org/abs/2606.00966v1)

**Authors:** Keith Truongcao, Christopher Nhu, Zijian An, Phong Nguyen, Siwei Cai et al. (6 authors)

**Published:** 2026-05-31 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.00966v1) | [PDF](https://arxiv.org/pdf/2606.00966v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language Action (VLA) models continue to face challenges such as slow inference speed and difficulty performing fine-grained motion adjustments, limiting their widespread adoption in industry. While the Real-Time Action Chunking (RTAC) algorithm has been proposed to address these bottlenecks, bridging the gap between the algorithm provided in pseudocode to a stable, real-world deployment on a low-cost robotic arm remains a challenge. In this work, we present a complete system-level implem...

</details>

---
