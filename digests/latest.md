# What's New

Papers discovered in the run at **2026-10-27 00:59 UTC**.

**New this run:** 9

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Vision-Language-Action Models (3)

### [TAD: Distilling Vision-Language-Action Policies from Teacher Trajectories Alone](https://arxiv.org/abs/2610.33650)

**Authors:** Yun Zhu, Da Wang

**Published:** 2026-10-24 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.33650) | [PDF](https://arxiv.org/pdf/2610.33650)

<details>
<summary>Abstract</summary>

Online distillation of vision-language-action (VLA) policies commonly relies on teacher action scores that an inference-only interface may not expose. Trajectory-only Adversarial Distillation (\gad{}) instead turns a fixed bank of teacher joint-position features into adaptive feedback: a discriminator compares feature marginals from teacher and student rollouts and supplies rewards for on-policy learning. The student interacts with the environment without online teacher queries or environment task rewards. On ManiSkill \texttt{PutOnPlateInScene25Main}, \gad{} improves OpenVLA-OFT (7B) from $26...

</details>

<details>
<summary>Share</summary>

```
TAD: Distilling Vision-Language-Action Policies from Teacher Trajectories Alone

Online distillation of vision-language-action (VLA) policies commonly relies on teacher action scores that an inference-only interface may not expose.

arXiv: https://arxiv.org/abs/2610.33650

#VLA #robotics
```

</details>

---

### [Learning Dexterous Manipulation: Hands, Simulators, Training, and Evaluation](https://arxiv.org/abs/2610.33486)

**Authors:** Luai Abuelsamen

**Published:** 2026-10-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.33486) | [PDF](https://arxiv.org/pdf/2610.33486)

<details>
<summary>Abstract</summary>

A dexterous hand can change an object's pose without setting it down. This survey covers 113 learning-based methods that attempt it, the hands they run on, the simulators they train in, and how they report results. The field has largely converged on one recipe: reinforcement learning on privileged state in a GPU simulator, distilled into a vision-only student for transfer to hardware. Almost half the corpus trains that way, nearly all of it in one simulator, whose own successors are barely used. A second and faster-growing branch learns from teleoperated demonstration instead, through vision-l...

</details>

<details>
<summary>Share</summary>

```
Learning Dexterous Manipulation: Hands, Simulators, Training, and Evaluation

A dexterous hand can change an object's pose without setting it down.

arXiv: https://arxiv.org/abs/2610.33486

#VLA #robotics
```

</details>

---

### [Late Breaking Results: Audio-Language-Action Models with Direct Speech Conditioning for Robotic Manipulation](https://arxiv.org/abs/2610.33866)

**Authors:** Enfu Nan, Pu Zhao, Yixiao Chen, Lin Zhao, Juyi Lin et al. (8 authors)

**Published:** 2026-10-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2610.33866) | [PDF](https://arxiv.org/pdf/2610.33866)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models enable robots to follow instructions in typed text, limiting broader deployment in natural speech. The traditional solution by prepending a speech recognition before VLA to convert speech into texts would incur additional latency and propagate errors. To address this, we present Speech-$π_{0.5}$, which maps raw speech directly to motor commands without explicit textual transcriptions. Specifically, built on $π_{0.5}$, we use a cross-modal projection to convert voice frames directly into audio tokens with significant response latency reduction. To further imp...

</details>

<details>
<summary>Share</summary>

```
Late Breaking Results: Audio-Language-Action Models with Direct Speech Conditioning for Robotic Manipulation

Vision-language-action (VLA) models enable robots to follow instructions in typed text, limiting broader deployment in natural speech.

arXiv: https://arxiv.org/abs/2610.33866

#VLA #robotics
```

</details>

---

## World Models (6)

### [WMEval: Evaluating Interactive World Models Grounded on Physical Simulations](https://arxiv.org/abs/2610.33894)

**Authors:** Lanxiang Hu, Yixin Huang, Abhilash Shankarampeta, Zilin Dai, Yuyuan Wu et al. (16 authors)

**Published:** 2026-10-24 | **Categories:** cs.CV | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; 2 distinct keyword hits; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.33894) | [PDF](https://arxiv.org/pdf/2610.33894) | [Code](https://github.com/hao-ai-lab/WMEval)

<details>
<summary>Abstract</summary>

Interactive world models hold immense potential for high-stakes applications in robotics, game engines, and immersive digital twins, yet existing benchmarks primarily focus on perceptual similarity rather than the physical-causal coherence essential for real-world utility. We introduce WMEval, a comprehensive benchmark that evaluates interactive world models against Unity-based physical simulations. By leveraging Unity as a high-fidelity ground-truth oracle, we shift evaluation beyond perceptual visual assessment toward the objective state-based verification required for downstream application...

</details>

<details>
<summary>Share</summary>

```
WMEval: Evaluating Interactive World Models Grounded on Physical Simulations

Interactive world models hold immense potential for high-stakes applications in robotics, game engines, and immersive digital twins, yet existing benchmarks primarily focus on perceptual similarity rather than the phy...

arXiv: https://arxiv.org/abs/2610.33894
Code: https://github.com/hao-ai-lab/WMEval

#worldmodels #robotics
```

</details>

---

### [RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models](https://arxiv.org/abs/2610.33807)

**Authors:** Doanh Le Thien, Viet-Thanh Nguyen, Pham Tri Quang, Nhi Pham, Christopher Wewer et al. (21 authors)

**Published:** 2026-10-24 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.33807) | [PDF](https://arxiv.org/pdf/2610.33807)

<details>
<summary>Abstract</summary>

Video world models (VWMs) are rapidly emerging as scalable neural simulators for robotic manipulation. However, most benchmarks only evaluate them as open-world video generators, using Vision-Language Models (VLMs) that lack strict 3D spatial and kinematic reasoning. To bridge this gap, we introduce RoboWorM, a comprehensive, deployment-aware benchmark that leverages known hardware priors such as robot kinematic trees and fixed camera configurations, to systematically examine structural and spatiotemporal fidelity. RoboWorM curates 1,605 episodes across single-arm, bimanual, and humanoid morph...

</details>

<details>
<summary>Share</summary>

```
RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models

Video world models (VWMs) are rapidly emerging as scalable neural simulators for robotic manipulation.

arXiv: https://arxiv.org/abs/2610.33807

#worldmodels #robotics
```

</details>

---

### [TurboWAM: Learning What Matters for Fast World Action Models](https://arxiv.org/abs/2610.33941)

**Authors:** Guile Wu, Shuangzhi Li, Xingxin Chen, Chengjie Huang, Sam Hosseini et al. (8 authors)

**Published:** 2026-10-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.33941) | [PDF](https://arxiv.org/pdf/2610.33941) | [Project Page](https://turbowam.github.io/)

<details>
<summary>Abstract</summary>

World action models have demonstrated promising performance in robot policy learning, yet their high inference latency remains a critical bottleneck for real-world deployment. Recent approaches have sought to improve inference efficiency by reducing test-time future-frame imagination or accelerating action prediction. However, these methods often leverage representations from all video world model layers without explicitly considering their varying relevance to action prediction, leading to redundant computation and suboptimal representation utilization. In this work, we propose TurboWAM, a fa...

</details>

<details>
<summary>Share</summary>

```
TurboWAM: Learning What Matters for Fast World Action Models

World action models have demonstrated promising performance in robot policy learning, yet their high inference latency remains a critical bottleneck for real-world deployment.

arXiv: https://arxiv.org/abs/2610.33941
Project page: https://turbowam.github.io/

#worldmodels #robotics
```

</details>

---

### [Distilling Dense Trajectory Teachers For Large-Motion Video World Models](https://arxiv.org/abs/2610.33566)

**Authors:** Shuofeng Sun, Linqing Zhao, Haibin Yan

**Published:** 2026-10-24 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2610.33566) | [PDF](https://arxiv.org/pdf/2610.33566)

<details>
<summary>Abstract</summary>

Video world models are expected to generate videos that accurately follow specified camera trajectories while maintaining consistent 3D structures. However, existing models are predominantly trained on densely sampled videos with small inter-frame camera motions. When applied to sparse, large step trajectories, they often produce frozen frames, inaccurate camera motion, and severe geometric drift. We attribute this degradation to a mismatch between the gradual viewpoint transitions seen during training and the large viewpoint changes required at inference time. To address this problem, we prop...

</details>

<details>
<summary>Share</summary>

```
Distilling Dense Trajectory Teachers For Large-Motion Video World Models

Video world models are expected to generate videos that accurately follow specified camera trajectories while maintaining consistent 3D structures.

arXiv: https://arxiv.org/abs/2610.33566

#worldmodels #robotics
```

</details>

---

### [World-in-Context: Interactive Video World Modeling with In-Context Conditioning](https://arxiv.org/abs/2610.33169)

**Authors:** Harold Haodong Chen, Rui Peng, Rongjin Guo, Lingteng Qiu, Kejie Qiu et al. (7 authors)

**Published:** 2026-10-23 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2610.33169) | [PDF](https://arxiv.org/pdf/2610.33169) | [Project Page](https://haroldchen19.github.io/WiC-site/)

<details>
<summary>Abstract</summary>

Interactive video world models require coordinated control over viewing perspectives, character actions, and camera motion. Existing methods typically leave view modes implicit in text captions, conflate action with camera motion, and inject controls through fragmented architectural pathways that capture interdependencies only indirectly. In this work, we present World-in-Context, an interactive world modeling framework powered by In-Context Conditioning (ICC). Rather than relying on specialized conditioning pathways, World-in-Context unifies view, action, and camera controls into explicit tok...

</details>

<details>
<summary>Share</summary>

```
World-in-Context: Interactive Video World Modeling with In-Context Conditioning

Interactive video world models require coordinated control over viewing perspectives, character actions, and camera motion.

arXiv: https://arxiv.org/abs/2610.33169
Project page: https://haroldchen19.github.io/WiC-site/

#worldmodels #robotics
```

</details>

---

### [WorldFailBench: Do World Models Understand Policy Failures?](https://arxiv.org/abs/2610.33565)

**Authors:** Zheng Zhang, Xiaoyang Tang, Shuaiqi Cheng, Jiakai Huang, Zhongbo Wu et al. (14 authors)

**Published:** 2026-10-24 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2610.33565) | [PDF](https://arxiv.org/pdf/2610.33565)

<details>
<summary>Abstract</summary>

Robot policy evaluation informs deployment decisions and policy improvement, but physical testing and simulator preparation require substantial effort. World models offer a complementary route through closed-loop interaction in generated environments. Recent benchmarks have demonstrated their potential as policy evaluators through outcome-based evaluation (i.e., assessing task success or failure). However, such evaluation does not establish whether world models faithfully simulate how policies fail. Misrepresenting failures can lead to incorrect diagnoses of policy weaknesses and make policies...

</details>

<details>
<summary>Share</summary>

```
WorldFailBench: Do World Models Understand Policy Failures?

Robot policy evaluation informs deployment decisions and policy improvement, but physical testing and simulator preparation require substantial effort.

arXiv: https://arxiv.org/abs/2610.33565

#worldmodels #robotics
```

</details>

---
