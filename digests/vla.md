# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-25 23:07 UTC

**Papers found:** 14

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Reflective VLA: In-Context Action Consequences Make VLAs Generalize](https://arxiv.org/abs/2606.25215v1)

**Authors:** Qing Lian, Kent Yu, Lei Zhang

**Published:** 2026-06-23 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.25215v1) | [PDF](https://arxiv.org/pdf/2606.25215v1.pdf) | [Project Page](https://lianqing11.github.io/reflective-vla-page/)

<details>
<summary>Abstract</summary>

Most vision-language-action (VLA) models are reactive: they predict the next action from the current instruction and observation, implicitly assuming that the current observation fully specifies the action-relevant state. In embodied control, however, embodiment-specific factors such as camera-to-robot geometry, robot calibration, or systematic actuation bias are often hard to identify from a single observation. As a result, reactive policies cannot reliably disambiguate these factors in general...

</details>

---

### [InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884v1)

**Authors:** Maggie Wang, Lars Osterberg, Stephen Tian, Ola Shorinwa, Jiajun Wu et al. (6 authors)

**Published:** 2026-06-23 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.24884v1) | [PDF](https://arxiv.org/pdf/2606.24884v1.pdf) | [Project Page](https://insight-vla.github.io)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models can learn manipulation skills from demonstrations, but their capabilities are bounded by the skills in the training data. We present InSight, a framework that unlocks autonomous skill acquisition by rendering VLAs steerable at the primitive-action level (e.g., "move gripper to the bowl", "lift upward", "pour the bottle"). InSight consists of two primary stages: (1) an automated segmentation pipeline that partitions demonstrations into labeled primitives via VL...

</details>

---

### [G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models](https://arxiv.org/abs/2606.24472v1)

**Authors:** Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu et al. (8 authors)

**Published:** 2026-06-23 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.24472v1) | [PDF](https://arxiv.org/pdf/2606.24472v1.pdf) | [Project Page](is)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have made rapid progress in generalist robot manipulation by harnessing semantic knowledge from pretrained vision-language backbones, but their visual tokens remain grounded in 2D image coordinates rather than the calibrated geometry of the robot's cameras -- a mismatch especially pronounced in multi-camera setups, where views are coupled by known intrinsics and extrinsics yet processed as independent images. We propose G$^3$VLA, a camera-aware geometric modul...

</details>

---

### [DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model](https://arxiv.org/abs/2606.24051v1)

**Authors:** Jingke Wang, Zhenru Zhao, Shuangming Lei, Hao Su, Yuehao Huang et al. (11 authors)

**Published:** 2026-06-23 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.24051v1) | [PDF](https://arxiv.org/pdf/2606.24051v1.pdf) | [Project Page](https://anonymous.4open.science/w/drivestack-vla/)

<details>
<summary>Abstract</summary>

Vision-Language-Action driving models convert a pretrained Vision-Language Model into a driving policy, allowing them to use world knowledge and follow language guidances. However, existing VLA driving models still lack driving-oriented spatial intelligence: their policies are mainly grounded on perspective image tokens and language priors, while precise motion planning requires metric geometry, top-down scene structure, and attention to safety-critical perceptual cues. This limitation makes cur...

</details>

---

## Other Recent Papers

### [Learning Action Priors for Cross-embodiment Robot Manipulation](https://arxiv.org/abs/2606.26095v1)

**Authors:** Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun et al. (8 authors)

**Published:** 2026-06-24 | **Categories:** cs.RO, cs.AI, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26095v1) | [PDF](https://arxiv.org/pdf/2606.26095v1.pdf)

<details>
<summary>Abstract</summary>

Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in ...

</details>

---

### [In-Context World Modeling for Robotic Control](https://arxiv.org/abs/2606.26025v1)

**Authors:** Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji et al. (7 authors)

**Published:** 2026-06-24 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26025v1) | [PDF](https://arxiv.org/pdf/2606.26025v1.pdf)

<details>
<summary>Abstract</summary>

Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Mode...

</details>

---

### [FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation](https://arxiv.org/abs/2606.26006v1)

**Authors:** Shuyi Zhang, Yunfan Lou, Hongyang Cheng, Yichen Guo, Chuyao Fu et al. (11 authors)

**Published:** 2026-06-24 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.26006v1) | [PDF](https://arxiv.org/pdf/2606.26006v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are often constrained by the imitation ceiling imposed by sub-optimal data. While Reinforcement Learning (RL) fine-tuning can surpass this limit, it is notoriously sample inefficient. This challenge arises from two core issues: (1) catastrophic initial unlearning due to an unstable Q-function and (2) inefficient policy updates caused by low-quality exploration data, often forcing a reliance on costly human interventions. We introduce FORCE, a 3-stage framework...

</details>

---

### [Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models](https://arxiv.org/abs/2606.25985v1)

**Authors:** Tiecheng Guo, Meng Guo

**Published:** 2026-06-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.25985v1) | [PDF](https://arxiv.org/pdf/2606.25985v1.pdf)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have shown strong potential for general-purpose robot manipulation, but their inference latency remains a major obstacle to stable high-frequency control. Asynchronous execution mitigates this bottleneck by overlapping policy inference with action execution, yet the next action chunk is still predicted from stale observations while the robot continues to move. Direct chunk stitching therefore introduces handoff discontinuities, action jitter, and failures in c...

</details>

---

### [ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models](https://arxiv.org/abs/2606.25800v1)

**Authors:** Kejing Wang, Toan Nguyen, Minh Hoang Nguyen, Simon Khan, Flora D. Salim

**Published:** 2026-06-24 | **Categories:** cs.LG, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.25800v1) | [PDF](https://arxiv.org/pdf/2606.25800v1.pdf)

<details>
<summary>Abstract</summary>

Effective online adaptation of vision-language-action (VLA) models remains challenging, as sparse rewards provide weak supervision for high-dimensional autoregressive action policies. Although self-distillation can in principle provide denser training signals, we find that text-based privileged teachers conditioned on demonstrations, retrieved experiences, or high-level plans are ineffective for VLA adaptation, exposing a modality gap between symbolic guidance and low-level robot actions. We pro...

</details>

---

### [WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning](https://arxiv.org/abs/2606.25591v1)

**Authors:** Melya Boukheddimi, Omar Adjali, Daniel Sontag, Frank Kirchner

**Published:** 2026-06-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.25591v1) | [PDF](https://arxiv.org/pdf/2606.25591v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have recently demonstrated strong generalization in robotic manipulation, yet their applicability to whole-body, contact-rich humanoid locomotion remains severely underexplored due to data scarcity, the absence of dynamically consistent demonstrations, and the difficulty of encoding optimality and safety in learning-based pipelines. This work introduces a unified framework WOLF-VLA that integrates whole-body optimal-control (OC) motion synthesis with large-sca...

</details>

---

### [Decoupling Semantics and Geometric Grounding: Spatial Visual Prompts for Language-Conditioned Imitation Learning](https://arxiv.org/abs/2606.25360v1)

**Authors:** Yanzhe Tang, Xinyu Shao, Yuxuan Hu, Siyu Chen, Bowen Yang et al. (9 authors)

**Published:** 2026-06-24 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.25360v1) | [PDF](https://arxiv.org/pdf/2606.25360v1.pdf)

<details>
<summary>Abstract</summary>

While end-to-end Vision-Language-Action (VLA) models show promise in robotic manipulation, their monolithic paradigm inherently couples semantic reasoning and spatial control. This creates a severe alignment bottleneck, limiting precise target disambiguation in data-constrained imitation learning. To overcome this, we propose SVP-IL, a decoupled architecture that explicitly extracts spatial visual grounding from the action generation loop. By leveraging vision-language foundation models, we pars...

</details>

---

### [MANGO: Automated Multi-Agent Test Oracle Generation for Vision-Language-Action Models](https://arxiv.org/abs/2606.24815v1)

**Authors:** Pablo Valle, Shaukat Ali, Aitor Arrieta, Lionel Briand

**Published:** 2026-06-23 | **Categories:** cs.SE, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.24815v1) | [PDF](https://arxiv.org/pdf/2606.24815v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are emerging robotic control systems that integrate perception, language understanding, and action generation in a unified architecture. Existing testing approaches for VLA-enabled robots rely on manually constructed symbolic test oracles that determine task success from final environment states. These oracles are costly to construct, require domain expertise, and are often tightly coupled to specific tasks and environments, limiting scalability and reuse. Fur...

</details>

---

### [Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos](https://arxiv.org/abs/2606.24448v1)

**Authors:** Danze Chen, Yanzhe Chen, Qiming Huang, Zhijun Cao, Chen Gao et al. (6 authors)

**Published:** 2026-06-23 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.24448v1) | [PDF](https://arxiv.org/pdf/2606.24448v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models require large-scale video-action pairs, yet real teleoperation remains scarce. While generated robot videos offer a scalable alternative, existing methods treat them as real robot data by recovering pseudo-actions from synthesized pixels. We argue that deriving low-level control from generated visuals is a mismatched abstraction. A video captures only \emph{geometry}: the spatial trajectory representing the \emph{where} of a task. A real demonstration captures...

</details>

---

### [TuringViT: Making SOTA Vision Transformers Accessible to All](https://arxiv.org/abs/2606.24253v1)

**Authors:** Qiman Wu, Hanlin Chen, Lyujie Chen, Rui Xin, Jianlei Zheng et al. (22 authors)

**Published:** 2026-06-23 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.24253v1) | [PDF](https://arxiv.org/pdf/2606.24253v1.pdf)

<details>
<summary>Abstract</summary>

Modern VLMs and VLA systems commonly adopt off-the-shelf ViTs such as SigLIP2 as visual encoders, but diverse downstream requirements in latency, temporal modeling, and VLM integration often call for customized SOTA-level ViTs. Training such encoders remains beyond the reach of much of the community, as it requires massive image-text data, while standard softmax attention makes high-resolution or dynamic-resolution pretraining prohibitively costly and often forces low-resolution pretraining foll...

</details>

---
