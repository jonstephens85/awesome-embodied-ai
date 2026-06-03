# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-03 19:48 UTC

**Papers found:** 18

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation](https://arxiv.org/abs/2606.03385v1)

**Authors:** Jiahao Xu, Peiyuan Wang, Hanzhuo Zhang, Zihao Yu, Tianyu Fu et al. (10 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.03385v1) | [PDF](https://arxiv.org/pdf/2606.03385v1.pdf) | [Project Page](https://sites.google.com/view/gtp-fa/)

<details>
<summary>Abstract</summary>

In robotic manipulation, the tight coupling between grasping and motion planning often obscures the true source of failure, leading to inefficient trial-and-error. To enable efficient long-horizon manipulation, we propose GTP-FA (Grasp-Then-Plan with Failure Attribution), a task-oriented two-stage grasp-then-plan framework that generates grasp candidates and performs downstream motion planning conditioned on the selected grasp. Given a failed manipulation trajectory, we learn a failure attributi...

</details>

---

### [See Less, Specify More: Visual Evidence Budgets for Generalizable VLAs](https://arxiv.org/abs/2606.02735v1)

**Authors:** Yueh-Hua Wu, Tatsuya Matsushima, Kei Ota

**Published:** 2026-06-01 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.02735v1) | [PDF](https://arxiv.org/pdf/2606.02735v1.pdf) | [Project Page](https://s2.airoa.io)

<details>
<summary>Abstract</summary>

Generalization remains a central bottleneck for vision-language-action (VLA) models: under distractors, appearance shifts, and semantically similar tasks, the policy must often infer local execution details from coarse instructions while also deciding which parts of the image matter for control. We present S2 (See Less, Specify More), a framework for improving VLA generalization by training the executor under a cleaner interface. Specify More preserves the original instruction as a stable high-l...

</details>

---

### [RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models](https://arxiv.org/abs/2606.02277v1)

**Authors:** Bin Yu, Yao Zhang, Haishan Liu, Shijie Lian, Yuliang Wei et al. (12 authors)

**Published:** 2026-06-01 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.02277v1) | [PDF](https://arxiv.org/pdf/2606.02277v1.pdf) | [GitHub](https://github.com/ZGC-EmbodyAI/RoboSemanticBench)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are built on the premise that semantic understanding from pretrained language or vision-language backbones should guide robot action prediction. Yet robot fine-tuning is optimized as imitation over task-specific action distributions, and many evaluations can be solved through visual or instruction-action shortcuts. We introduce RoboSemanticBench (RSB), an embodied benchmark for diagnosing semantic grounding in action prediction: whether post-trained VLA models...

</details>

---

## Other Recent Papers

### [Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation](https://arxiv.org/abs/2606.03784v1)

**Authors:** Nan Sun, Yuan Zhang, Yongkun Yang, Wentao Zhao, Peiyan Li et al. (13 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03784v1) | [PDF](https://arxiv.org/pdf/2606.03784v1.pdf)

<details>
<summary>Abstract</summary>

Embodied chain-of-thought (CoT) aims to bridge linguistic reasoning and robotic control, but its effective form and integration strategy remain underexplored. In this paper, we revisit embodied CoT for vision-language-action (VLA) models at large scale. We construct the largest embodied CoT corpus to date, comprising 978,743 trajectories, 226.3M samples, and 2592.5 hours of robot data. Through extensive experiments, we find that effective embodied CoT should ground high-level semantic understand...

</details>

---

### [PHASER: Phase-Aware and Semantic Experience Replay for Vision-Language-Action Models](https://arxiv.org/abs/2606.03598v1)

**Authors:** Ziyang Chen, Shaoguang Wang, Weiyu Guo, Qianyi Cai, He Zhang et al. (8 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.03598v1) | [PDF](https://arxiv.org/pdf/2606.03598v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have achieved remarkable success in language-conditioned robotic manipulation. However, deploying these models in open-ended environments requires continuously acquiring novel skills, a process that inevitably triggers severe catastrophic forgetting of previously learned behaviors. While experience replay (ER) serves as a standard mitigating strategy, naive uniform sampling fundamentally misaligns with the temporal characteristics of manipulation trajectories....

</details>

---

### [Partially Observable Adversarial Patch Attacks on Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2606.03556v1)

**Authors:** Xiaofei Wang, Mingliang Han, Tianyu Hao, Yi Yang, Yun-Bo Zhao et al. (6 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03556v1) | [PDF](https://arxiv.org/pdf/2606.03556v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models are gaining attention in robotics, yet their robustness to adversarial attacks remains largely unexplored. Existing work shows that adversarial patches can mislead VLA-based robots but assumes full access to the entire execution trajectory, an unrealistic requirement in practice. We address this limitation by formulating a partially observable threat model, where the adversary can exploit only a short prefix of the trajectory to generate a fixed patch applied ...

</details>

---

### [OpenEAI-Platform: An Open-source Embodied Artificial Intelligence Hardware-Software Unified Platform](https://arxiv.org/abs/2606.03392v1)

**Authors:** Jinyuan Zhang, Luoyi Fan, Leiyu Wang, Yeqiang Wang, Yicheng Zhu et al. (7 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03392v1) | [PDF](https://arxiv.org/pdf/2606.03392v1.pdf)

<details>
<summary>Abstract</summary>

Embodied AI in the real world requires both accurate hardware and robust vision-language-action (VLA) policies. We present OpenEAI-Platform, a fully open-source platform that integrates a low-cost 6+1 degree-of-freedom (dof) robotic arm (OpenEAI-Arm) and a reproducible VLA model (OpenEAI-VLA). OpenEAI-Arm provides open-source mechanical designs for low manufacturing cost and compliant control methods for higher accuracy. OpenEAI-VLA builds on Qwen3-VL-4B and uses a Diffusion Transformer action h...

</details>

---

### [GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](https://arxiv.org/abs/2606.03240v1)

**Authors:** Yizhi Chen, Zhanxiang Cao, Xinyi Peng, Yixiao Zheng, Xiaxi Si et al. (17 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03240v1) | [PDF](https://arxiv.org/pdf/2606.03240v1.pdf)

<details>
<summary>Abstract</summary>

Current Vision--Language--Action (VLA) models often optimize for semantic grounding, whereas executable manipulation requires geometry-aware spatial alignment and dynamic affordance selection. We introduce GeoAlign, a state-guided spatial alignment architecture for VLA policy learning. GeoAlign post-trains an RGB geometry branch with robot-domain RGB-D supervision, yielding RGB-derived Geometry-Enhanced Post-Trained (GEP) features for policy rollout. The robot's proprioceptive state queries the ...

</details>

---

### [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159v1)

**Authors:**  NVIDIA,  :, Aarti Basant, Amlan Kar, Despoina Paschalidou et al. (35 authors)

**Published:** 2026-06-02 | **Categories:** cs.CV, cs.AI, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03159v1) | [PDF](https://arxiv.org/pdf/2606.03159v1.pdf)

<details>
<summary>Abstract</summary>

As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck. In closed-loop simulation, the driving policy model actively interacts with the environment, where its actions dynamically update the simulator state and directly influence the next set of generated sensor observations. While recent reconstruction-based neural simulators offer photorealism, they are fundamentally constrained by their initial captured data and ...

</details>

---

### [TTT-VLA: Test-Time Latent Prompt Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2606.03127v1)

**Authors:** Wenbo Zhang, Jianxiong Li, Shuai Yang, Sijin Chen, Jiajun Liu et al. (7 authors)

**Published:** 2026-06-02 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.03127v1) | [PDF](https://arxiv.org/pdf/2606.03127v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models trained on large-scale data have made remarkable progress, but they remain vulnerable to distribution shifts at deployment time. Recent VLA models suggest that prompts can serve as an efficient interface for steering policy behavior, but existing prompt-based steering typically relies on external guidance. This raises a natural question: can test-time training (TTT) for VLA be achieved by optimizing a prompt, so that the steering interface itself can be learne...

</details>

---

### [SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos](https://arxiv.org/abs/2606.02745v1)

**Authors:** Jaehyeon Son, Junhyun Kim, Kyle Kam, Jeremiah Coholich, Seok Joon Kim et al. (10 authors)

**Published:** 2026-06-01 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.02745v1) | [PDF](https://arxiv.org/pdf/2606.02745v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action models (VLAs) are promising general-purpose robot policies, but adapting them to new tasks typically requires costly task-specific teleoperation data. As an alternative, we study one-shot demo-conditioned VLAs, where a robot policy is conditioned on a single demonstration video of an unseen task. We find that existing end-to-end approaches often struggle when successful execution requires precisely localizing small target regions. To address this limitation, we propose See...

</details>

---

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

### [AURA: Action-Gated Memory for Robot Policies at Constant VRAM](https://arxiv.org/abs/2606.02775v1)

**Authors:** Josef Chen

**Published:** 2026-06-01 | **Categories:** cs.AI, cs.AR, cs.DC

**Links:** [arXiv](https://arxiv.org/abs/2606.02775v1) | [PDF](https://arxiv.org/pdf/2606.02775v1.pdf)

<details>
<summary>Abstract</summary>

The KV-cache is the right memory for datacenters but the wrong memory for robots. Datacenter inference batches many short requests and resets them, amortizing an attention cache across a crowd. Embodied agents instead run one long, non-resetting episode on bandwidth-limited edge hardware, where high-bandwidth memory and flash are scarce, flash has finite write endurance, and memory writes rather than compute can become the binding constraint. AURA-Mem (Action-Utility Recurrent Adaptive Memory) t...

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
