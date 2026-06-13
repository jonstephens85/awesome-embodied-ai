# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-13 17:22 UTC

**Papers found:** 8

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories](https://arxiv.org/abs/2606.13578v1)

**Authors:** Baochang Ren, Xinjie Liu, Xi Chen, Yanshuo Liu, Chenxi Li et al. (18 authors)

**Published:** 2026-06-11 | **Categories:** cs.CL, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.13578v1) | [PDF](https://arxiv.org/pdf/2606.13578v1.pdf) | [Project Page](at)

<details>
<summary>Abstract</summary>

Scientific laboratories increasingly rely on AI systems to reason about experiments, but the physical act of doing science remains largely outside their reach. AI can help read literature, generate hypotheses, and plan protocols, yet the execution of those protocols at the bench still requires a human operator. Vision-Language-Action (VLA) models provide one possible interface between written protocols and robot execution, but existing policies are trained mostly on household and tabletop demons...

</details>

---

### [GIVE: Grounding Human Gestures in Vision-Language-Action Models](https://arxiv.org/abs/2606.13435v1)

**Authors:** Pengfei Liu, Gen Li, Junqiao Fan, Boyu Ma, Jindou Jia et al. (7 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.13435v1) | [PDF](https://arxiv.org/pdf/2606.13435v1.pdf) | [Project Page](https://luis-cloud-sg.github.io/GIVE-project/)

<details>
<summary>Abstract</summary>

Human communication is inherently multimodal, where language is often accompanied by non-verbal cues such as gestures to convey intentions. However, current Vision-Language-Action (VLA) models treat robotic manipulation as a pure text-driven task, overlooking the important role of gestures in Human-Robot Interaction (HRI). This often leads to inaccurate intent grounding and unreliable manipulation when language instructions are ambiguous or underspecified. To address this challenge, we propose G...

</details>

---

### [Trajectory-Level Redirection Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2606.12978v1)

**Authors:** Gokul Puthumanaillam, Vardhan Dongre, Pranay Thangeda, Hooshang Nayyeri, Dilek Hakkani-Tür et al. (6 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO, cs.CV, eess.SY

**Links:** [arXiv](https://arxiv.org/abs/2606.12978v1) | [PDF](https://arxiv.org/pdf/2606.12978v1.pdf) | [Project Page](https://vla-redirection-attack.github.io/)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies bring natural language into closed-loop robot control, enabling robots to execute manipulation tasks directly from text instructions. The same interface gives text a recurring role in control because the prompt is reused at every replanning step, and each prompt-conditioned action changes the future observations on which the policy acts. Existing VLA attacks study adversarial prompts that elicit targeted low-level actions or make such actions persist across ...

</details>

---

### [SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2606.12956v1)

**Authors:** Sunghwan Kim, Byeonghyun Pak, Kehan Long, Yulun Tian, Nikolay Atanasov

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12956v1) | [PDF](https://arxiv.org/pdf/2606.12956v1.pdf) | [Project Page](https://existentialrobotics.org/serf/)

<details>
<summary>Abstract</summary>

Long-horizon robot mobile manipulation requires continual reasoning about localization, environment changes, and task progress, all of which are challenging to infer from image observations alone. In this paper, we show that conditioning a mobile manipulation policy on a spatiotemporal feature map improves reasoning over long horizons. The map represents the environment and the articulated robot body as neural points in a shared latent space and is updated online from egocentric observations and...

</details>

---

## Other Recent Papers

### [See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation](https://arxiv.org/abs/2606.13279v1)

**Authors:** Yoon-Ji Choi, Young-Chae Son, Soo-Chul Lim

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.13279v1) | [PDF](https://arxiv.org/pdf/2606.13279v1.pdf)

<details>
<summary>Abstract</summary>

In bimanual robotic manipulation, task-relevant visual information varies with the task stage and context, while the interaction of the two arms shifts between independent and coordinated modes, making policy learning challenging. However, existing monolithic Vision-Language-Action (VLA) policies process diverse visual inputs and interaction patterns through a single shared representation and action generation pathway, often failing to separately account for visual relevance and bimanual interac...

</details>

---

### [An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics](https://arxiv.org/abs/2606.12936v1)

**Authors:** Zhe Liu, Huanbo Jin, Zhaohui Du, Zhe Wang, He Xu et al. (11 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.12936v1) | [PDF](https://arxiv.org/pdf/2606.12936v1.pdf)

<details>
<summary>Abstract</summary>

Wet-lab robots can improve the reproducibility, throughput, and safety of biomedical experiments, but scaling their learning requires customizable simulators for safe and reproducible task generation, open editable laboratory assets, and efficient pipelines that turn limited demonstrations into usable training data. We present Pipette, an embodied simulation platform, benchmark, and data-efficient augmentation framework for wet-lab robot learning. Pipette releases over 43 open-source and re-edit...

</details>

---

### [AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots](https://arxiv.org/abs/2606.12859v1)

**Authors:** Jianli Sun, Bin Tian, Qiyao Zhang, Zijian Liu, Yutong Wang et al. (9 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.12859v1) | [PDF](https://arxiv.org/pdf/2606.12859v1.pdf)

<details>
<summary>Abstract</summary>

Aerial manipulation systems have long suffered from representation coupling in end-to-end control, as platform-level Unmanned Aerial Vehicle (UAV) movement and end-effector-level arm manipulation differ substantially in action scale, dynamics, and control objectives. In this paper, we propose AIR-VLA+, a flow matching action generation architecture specifically designed for aerial manipulation, featuring cascaded dual-action decoders and an asymmetric feature-level Mixture of Experts (MoE). We c...

</details>

---

### [Real-Time Execution with Autoregressive Policies](https://arxiv.org/abs/2606.13355v1)

**Authors:** Sangkyu Lee, Seohyeon Park, Tackgeun You, Avi Caciularu, Idan Szpektor et al. (7 authors)

**Published:** 2026-06-11 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.13355v1) | [PDF](https://arxiv.org/pdf/2606.13355v1.pdf)

<details>
<summary>Abstract</summary>

Real-time execution, enabled by asynchronous inference that ensures both smooth action trajectories and fast reactivity, is critical for realistic deployments of large-scale Vision-Language-Action models. However, recent work on real-time execution primarily focuses on variants of diffusion policies, even though it is more critical for autoregressive policies given their slower rollout speed in synchronous inference. In contrast, we demonstrate that autoregressive policies can achieve real-time ...

</details>

---
