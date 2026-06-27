# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-06-27 17:10 UTC

**Papers found:** 11

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [Scalable Behavior Cloning with Open Data, Training, and Evaluation](https://arxiv.org/abs/2606.27375v1)

**Authors:** Arthur Allshire, Himanshu Gaurav Singh, Ritvik Singh, Adam Rashid, Hongsuk Choi et al. (18 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.27375v1) | [PDF](https://arxiv.org/pdf/2606.27375v1.pdf) | [Project Page](https://abc.bot)

<details>
<summary>Abstract</summary>

We introduce ABC, a fully open-source stack for manipulation with behavior cloning. At its core is ABC-130K: the largest open-source teleoperation dataset to date, featuring 3,500 hours of data spanning over 130K episodes across 195 diverse tasks. Furthermore, we open-source our accessible hardware setup, training infrastructure, and simulation pipeline. We also release 400 hours of sim-teleop data and provide a co-training recipe that produces correlated simulation and real-world evaluation, of...

</details>

---

### [LA4VLA: Learning to Act without Seeing via Language-Action Pretraining](https://arxiv.org/abs/2606.27295v1)

**Authors:** Tao Lin, Yuxin Du, Yiran Mao, Zewei Ye, Yilei Zhong et al. (16 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.27295v1) | [PDF](https://arxiv.org/pdf/2606.27295v1.pdf) | [GitHub](https://github.com/MINT-SJTU/LA4VLA)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are commonly pretrained on robot demonstrations by jointly mapping visual observations and language instructions to actions. However, dense visual-action supervision can dominate the comparatively sparse language-action signal. As a result, policies may rely on visual shortcuts rather than learn how language conditions action execution, making them sensitive to visual variations. To address this limitation, we propose LA4VLA, a language-action pretraining fram...

</details>

---

### [Improving Vision-Language-Action Model Fine-Tuning with Structured Stage and Keyframe Supervision](https://arxiv.org/abs/2606.26801v1)

**Authors:** Yuan Xu, Yixiang Chen, Kai Wang, Jiabing Yang, Peiyan Li et al. (8 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO, cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2606.26801v1) | [PDF](https://arxiv.org/pdf/2606.26801v1.pdf) | [Project Page](https://hi-yuanxu.github.io/StaKe-Web/)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have shown strong potential for generalizable robotic manipulation. During fine-tuning, however, action supervision applies equally across all timesteps, without structured supervision on which manipulation stage the robot is in or what the next gripper-event target should be. This causes failures to concentrate around challenging gripper-event transitions. To address this, we propose StaKe, a plug-in auxiliary supervision framework that automatically derives ...

</details>

---

### [E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation](https://arxiv.org/abs/2606.27268v1)

**Authors:** Wen Ye, Peiyan Li, Tingyu Yuan, Yuan Xu, Xiangnan Wu et al. (10 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.27268v1) | [PDF](https://arxiv.org/pdf/2606.27268v1.pdf) | [Project Page](https://27yw.github.io/E-TTS-Web/)

<details>
<summary>Abstract</summary>

Recently, a few works have made early attempts to study test-time scaling for embodied tasks. However, two major challenges remain unsolved: (1) reasoning can effectively improve the performance of the policy, but its scaling mechanism has seldom been studied; (2) historical information is essential, as embodied tasks are inherently long-horizon and sequential, making sole reliance on current observations for action scaling inadequate due to the lack of historical context utilization. To address...

</details>

---

## Other Recent Papers

### [RouterVLA: Turning Smoke Tests into Supervision for Heterogeneous VLA Selection](https://arxiv.org/abs/2606.27355v1)

**Authors:** Xingyu Ren, Chugang Yi, Ge Ma, Youran Sun

**Published:** 2026-06-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.27355v1) | [PDF](https://arxiv.org/pdf/2606.27355v1.pdf)

<details>
<summary>Abstract</summary>

We study whether pre-deployment evaluation rollouts can be reused to supervise policy selection. Robot teams routinely smoke test candidate vision-language-action (VLA) policies, then compress those trials into a global winner. RouterVLA evaluates this idea with outcome-disjoint cross-fitting: recorded probes build a profile for each frozen expert, and a separate trial scores the selected expert without entering its profile. Across 34,752 LIBERO-Plus rollout records, a transparent probe-success ...

</details>

---

### [Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy](https://arxiv.org/abs/2606.27251v1)

**Authors:** Junhao Shi, Zezheng Huai, Siyin Wang, Jia Chen, Yubang Wang et al. (10 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO, cs.AI

**Links:** [arXiv](https://arxiv.org/abs/2606.27251v1) | [PDF](https://arxiv.org/pdf/2606.27251v1.pdf)

<details>
<summary>Abstract</summary>

Building persistent embodied agents in unstructured environments demands unified orchestration of heterogeneous tools spanning both cyber (APIs, IoT) and physical (manipulation, navigation) domains, coupled with autonomous recovery from physical failures that inevitably arise over extended operation. Existing systems treat these as separate problems: VLM-based planners lack a unified cyber-physical action space, agent frameworks accumulate unbounded context that degrades temporal coherence, and ...

</details>

---

### [Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline)](https://arxiv.org/abs/2606.27163v1)

**Authors:** Ilia Larchenko

**Published:** 2026-06-25 | **Categories:** cs.RO, cs.AI, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2606.27163v1) | [PDF](https://arxiv.org/pdf/2606.27163v1.pdf)

<details>
<summary>Abstract</summary>

I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition on bimanual garment folding. The system placed 1st of 62 teams in the online (simulation) round and 2nd in the real-world final. It improves a vision-language-action (VLA) policy with a reinforcement-learning loop. The policy is its own value function: the same network that predicts actions also predicts success, progress, and a few task-relevant future quantities, and those predictions drive advantage estimation, live...

</details>

---

### [PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies](https://arxiv.org/abs/2606.27146v1)

**Authors:** Jiayu Yang, Tao Yang, Weijun Li, Xiang Chang, Fei Chao et al. (7 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.27146v1) | [PDF](https://arxiv.org/pdf/2606.27146v1.pdf)

<details>
<summary>Abstract</summary>

Long-horizon robotic manipulation is highly sensitive to physically infeasible transitions, contact-induced disturbances, and the lack of effective self-correction during execution. Although Vision-Language-Action (VLA) models provide strong task grounding through multimodal learning, they typically generate actions in a feed-forward manner without explicitly checking physical feasibility or diagnosing execution errors online. We present PhysReflect-VLA, a plug-and-play execution-time reliabilit...

</details>

---

### [PAMAE: Phase-Aware-MoE Action Experts Towards Reliable Flow-Matching Vision-Language-Action Policies](https://arxiv.org/abs/2606.27144v1)

**Authors:** Jiayu Yang, Tao Yang, Xiang Chang, Fei Chao, Changjing Shang et al. (6 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.27144v1) | [PDF](https://arxiv.org/pdf/2606.27144v1.pdf)

<details>
<summary>Abstract</summary>

Reliable action generation for multi-stage robotic manipulation remains challenging for Vision-Language-Action (VLA) models. While existing flow-matching VLA policies offer strong multimodal grounding and generalization, they typically employ a single shared action expert, limiting their ability to capture phase-specific control patterns across distinct execution stages. We propose a plug-and-play Phase-Aware Mixture-of-Experts Action Module (PAMAE), as a step towards more reliable phase-consist...

</details>

---

### [ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2606.27079v1)

**Authors:** Mingyang Lyu, Yinqian Sun, Yiyang Jia, Sicheng Shen, Moquan Sha et al. (8 authors)

**Published:** 2026-06-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.27079v1) | [PDF](https://arxiv.org/pdf/2606.27079v1.pdf)

<details>
<summary>Abstract</summary>

In embodied intelligence, safety is a prerequisite for reliable robot deployment in the physical world. Current vision-language-action (VLA) models continue to advance toward general-purpose task capability, yet their embodied safety limits remain poorly understood. To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. We define a 13-category safety taxonomy covering physical interaction safety (Safe-Core), ...

</details>

---

### [Inference-Time Robot Behavior Steering through Physically-Aware Reconfiguration of Task-Structure](https://arxiv.org/abs/2606.26588v1)

**Authors:** Yiyuan Pan, Hanjiang Hu, Shangtao Li, Xusheng Luo, Changliu Liu

**Published:** 2026-06-25 | **Categories:** cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2606.26588v1) | [PDF](https://arxiv.org/pdf/2606.26588v1.pdf)

<details>
<summary>Abstract</summary>

A central challenge in deploying learned robot policies is inference-time behavior steering: redirecting a policy at test time to satisfy user preferences not anticipated during training, without retraining. Existing methods fail in two modes: end-to-end methods require fine-tuning or expert-level guidance, while neuro-symbolic methods rely on predefined symbols whose edits can result in logically reasonable but physically infeasible plans. To address this challenge, we propose ReStruct, which b...

</details>

---
