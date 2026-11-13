# What's New

Papers discovered in the run at **2026-11-13 02:16 UTC**.

**New this run:** 6

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Vision-Language-Action Models (2)

### [Scaling VLA Serving Under Robotic Execution Constraints](https://arxiv.org/abs/2611.14969)

**Authors:** Yue Zhang, Zicong Ye, Lufang Chen, Dance Yang, Mingyang Li et al. (17 authors)

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.DC | **Relevance:** ★★★★☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.14969) | [PDF](https://arxiv.org/pdf/2611.14969) | [Code](https://github.com/X-Square-Robot/xinfer)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation. In our production setting, hundreds of VLA-powered robots are already operating in real-world environments, creating an immediate need for efficient fleet serving. We present XInfer, a production-deployed VLA serving system designed to reduce the inference infrastructure cost of large-scale robotic deployments. XInfer jointly coordinates heterogeneous VLA computation with the evolving response requirements of robotic execution. By exploiting computational parallelism while managin...

</details>

<details>
<summary>Share</summary>

```
Scaling VLA Serving Under Robotic Execution Constraints

Vision-language-action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation.

arXiv: https://arxiv.org/abs/2611.14969
Code: https://github.com/X-Square-Robot/xinfer

#VLA #robotics
```

</details>

---

### [Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models](https://arxiv.org/abs/2611.14834)

**Authors:** Wen-Han Hsieh, Ken Jiankun Zheng, Chia-Chien Chen, David M. Chan, Trevor Darrell

**Published:** 2026-11-10 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.14834) | [PDF](https://arxiv.org/pdf/2611.14834)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation. However, sampled action sequences can be ineffective, while evaluating alternatives with computationally expensive verifiers adds latency at each policy query. In this work, we propose HDH, a lightweight framework that uses hindsight from a frozen VLA's own deployments to improve action verification. The framework has three stages. First, we deploy the policy and collect its autonomous rollouts. We then train a compact action verifier to assign each action chunk a predicted task-success...

</details>

<details>
<summary>Share</summary>

```
Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models

Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation.

arXiv: https://arxiv.org/abs/2611.14834

#VLA #robotics
```

</details>

---

## World Models (4)

### [BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model](https://arxiv.org/abs/2611.14815)

**Authors:** Junyoung Seo, Jaewoo Seo, Seungryong Kim, Laura Leal-Taixé, Xiuming Zhang et al. (6 authors)

**Published:** 2026-11-10 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.14815) | [PDF](https://arxiv.org/pdf/2611.14815) | [Project Page](https://research.nvidia.com/labs/sil/projects/birddreams/)

<details>
<summary>Abstract</summary>

Driving world models aim to simulate how a scene unfolds under different ego actions. This requires plausible motion of surrounding vehicles as well as precise ego-trajectory control. Learning vehicle motion from perspective video alone is challenging because motion is entangled with appearance and vehicles can be occluded. Prior work therefore conditions video generation on layouts that specify vehicle motion, providing control over surrounding vehicles but requiring their future trajectories as inputs. We introduce BirdDreams, an autoregressive driving world model that jointly generates pers...

</details>

<details>
<summary>Share</summary>

```
BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model

Driving world models aim to simulate how a scene unfolds under different ego actions.

arXiv: https://arxiv.org/abs/2611.14815
Project page: https://research.nvidia.com/labs/sil/projects/birddreams/

#worldmodels #robotics
```

</details>

---

### [Fast Inference-Time Policy Refinement via Action-Affine World Models](https://arxiv.org/abs/2611.15011)

**Authors:** Run Wang, Yilin Mo, Liang Wu

**Published:** 2026-11-11 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.15011) | [PDF](https://arxiv.org/pdf/2611.15011)

<details>
<summary>Abstract</summary>

Imitation policies can perform complex manipulation, yet small execution errors can accumulate and cause failure. Refinement can correct these errors, but existing approaches often require additional on-policy learning or costly online planning. Our key insight is that a pretrained policy already supplies a useful nominal behavior: refinement can focus on predicting how small action corrections change its outcome. We therefore learn this local response in a form that is cheap to optimize. Our \textit{action-affine world model} (A\textsuperscript{2}WM) learns local action sensitivities offline...

</details>

<details>
<summary>Share</summary>

```
Fast Inference-Time Policy Refinement via Action-Affine World Models

Imitation policies can perform complex manipulation, yet small execution errors can accumulate and cause failure.

arXiv: https://arxiv.org/abs/2611.15011

#worldmodels #robotics
```

</details>

---

### [The Posterior-Prior Epistemic Gap: When World Model Imagination Fails to Carry Task-Relevant Signals](https://arxiv.org/abs/2611.14955)

**Authors:** Jaerock Kwon, Elahe Delavari, Donghyun Kim, Haewoon Nam

**Published:** 2026-11-11 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.14955) | [PDF](https://arxiv.org/pdf/2611.14955)

<details>
<summary>Abstract</summary>

Model-based planners that roll out imagined futures assume the transition model faithfully propagates task-relevant signals---a property rarely measured directly. In a single-seed case study of a Recurrent State Space Model world model with active-inference planning in the CARLA driving simulator, we identify a \textbf{posterior-prior gap}---posterior (observation-filtered) states retain obstacle information that imagined rollout states progressively lose: a supervised obstacle probe achieves AUC 0.85 on posterior states, but the same probe applied to imagined prior states shows monotonic deca...

</details>

<details>
<summary>Share</summary>

```
The Posterior-Prior Epistemic Gap: When World Model Imagination Fails to Carry Task-Relevant Signals

Model-based planners that roll out imagined futures assume the transition model faithfully propagates task-relevant signals---a property rarely measured directly.

arXiv: https://arxiv.org/abs/2611.14955

#worldmodels #robotics
```

</details>

---

### [FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks](https://arxiv.org/abs/2611.14880)

**Authors:** Yinuo Du, Christopher Kiekintveld

**Published:** 2026-11-11 | **Categories:** cs.LG, cs.CR | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.14880) | [PDF](https://arxiv.org/pdf/2611.14880)

<details>
<summary>Abstract</summary>

Autonomous cyber defense is widely studied with deep reinforcement learning, but most work trains policies inside simulators because learning requires many trial-and-error interactions. Simulator-based training carries a fidelity gap: trained policies face authentication delays, partial action failures, service dependencies, and user traffic patterns that the simulator did not represent, and degrade on transfer. Training directly in the network being defended removes the gap but makes every interaction slow and costly, so sample efficiency becomes the binding constraint. Model-based reinforcem...

</details>

<details>
<summary>Share</summary>

```
FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks

Autonomous cyber defense is widely studied with deep reinforcement learning, but most work trains policies inside simulators because learning requires many trial-and-error interactions.

arXiv: https://arxiv.org/abs/2611.14880

#worldmodels #robotics
```

</details>

---
