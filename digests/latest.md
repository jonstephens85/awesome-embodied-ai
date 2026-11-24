# What's New

Papers discovered in the run at **2026-11-24 05:40 UTC**.

**New this run:** 56

[Dashboard](../docs/index.html) · [Back to Home](../README.md)

---

## Egocentric Data (3)

### [Ego2Wrist: Bootstrapping Wrist-View Synthesis from Egocentric Video](https://arxiv.org/abs/2611.29850)

**Authors:** Ziyao Zeng, Xiatao Sun, Hao Wang, Ziyu Guo, Youheng Yao et al. (11 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "egocentric video" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29850) | [PDF](https://arxiv.org/pdf/2611.29850) | [Project Page](https://adonis-galaxy.github.io/Ego2Wrist/)

<details>
<summary>Abstract</summary>

Wrist cameras provide an action-centric view that is directly relevant to robot manipulation. However, collecting human wrist-camera videos at scale is challenging due to cumbersome setups that can interfere with natural hand movements. In contrast, head-mounted human egocentric videos are much easier to scale. We introduce Ego2Wrist, which synthesizes synchronized wrist-camera views from human egocentric videos and task descriptions. Trained on approximately 940 hours of paired head- and wrist-camera recordings, Ego2Wrist jointly generates three views. To evaluate generated wrist views withou...

</details>

<details>
<summary>Share</summary>

```
Ego2Wrist: Bootstrapping Wrist-View Synthesis from Egocentric Video

Wrist cameras provide an action-centric view that is directly relevant to robot manipulation.

arXiv: https://arxiv.org/abs/2611.29850
Project page: https://adonis-galaxy.github.io/Ego2Wrist/

#egocentric #robotlearning
```

</details>

---

### [Ego-HMB: Human Motion Bridging from Egocentric Images via A Motion Bridge Diffusion Model](https://arxiv.org/abs/2611.29218)

**Authors:** Gaoge Han, Yongkang Cheng, Shaoli Huang, Jing Zhang, Mingming Gong et al. (7 authors)

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric human" in abstract; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29218) | [PDF](https://arxiv.org/pdf/2611.29218) | [Code](https://github.com/gaogehan/Ego-HMB)

<details>
<summary>Abstract</summary>

We introduce Egocentric Human Motion Bridging, a task that generates a coherent 3D human motion sequence from two endpoint egocentric images. Unlike conventional motion in-betweening, which requires structured 3D endpoint poses, this setting uses raw first-person observations available from wearable devices in VR/AR and robotics. It presents challenges due to viewpoint variations, partial body visibility, and temporal ambiguity under cross-modal endpoint constraints. To address these challenges, we propose Ego-HMB, a unified diffusion-based framework that learns endpoint pose estimation and te...

</details>

<details>
<summary>Share</summary>

```
Ego-HMB: Human Motion Bridging from Egocentric Images via A Motion Bridge Diffusion Model

We introduce Egocentric Human Motion Bridging, a task that generates a coherent 3D human motion sequence from two endpoint egocentric images.

arXiv: https://arxiv.org/abs/2611.29218
Code: https://github.com/gaogehan/Ego-HMB

#egocentric #robotlearning
```

</details>

---

### [HandiVid: A High-Quality Dataset for Hand-Driven Interactive Video Generation](https://arxiv.org/abs/2611.29693)

**Authors:** Chaoyang Zhang, Shaohao Rui, Xiaofeng Mao, Yuanxun Xu, Haoyuan Xia et al. (8 authors)

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "egocentric video" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29693) | [PDF](https://arxiv.org/pdf/2611.29693)

<details>
<summary>Abstract</summary>

Hand-driven egocentric interactive video generation aims to generate dynamic scenes with realistic interaction responses conditioned on hand movements and camera motion. However, existing egocentric video datasets struggle to provide scene diversity, meaningful hand-object interactions, and reliable motion annotations simultaneously. To address these limitations, we introduce HandiVid, a high-quality dataset comprising 200K curated and annotated egocentric interaction video clips for hand-driven interactive video generation. We develop a unified data processing pipeline that integrates public...

</details>

<details>
<summary>Share</summary>

```
HandiVid: A High-Quality Dataset for Hand-Driven Interactive Video Generation

Hand-driven egocentric interactive video generation aims to generate dynamic scenes with realistic interaction responses conditioned on hand movements and camera motion.

arXiv: https://arxiv.org/abs/2611.29693

#egocentric #robotlearning
```

</details>

---

## Vision-Language-Action Models (26)

### [Quantizing in the Loop: Drift-Aware Ultra-Low-Bit Vision-Language-Action Models](https://arxiv.org/abs/2611.30178)

**Authors:** Yanlong Chen, Thongthornpatch Chamadol, Yichen Guo, Yunfei Gao, Mohan Liu et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30178) | [PDF](https://arxiv.org/pdf/2611.30178) | [Code](https://github.com/ForeverBlue816/LoopQ)

<details>
<summary>Abstract</summary>

Deploying large vision-language-action (VLA) models on resource-constrained robots demands extreme compression, yet existing post-training quantization (PTQ) methods frequently collapse at ultra-low bit-widths ($\le$ 2 bits). We trace this failure to two mismatches in standard pipelines. First, calibrating on static offline demonstrations induces distribution shift: minor quantization perturbations drive the policy into unseen states where uncalibrated errors compound. Second, minimizing the layer-wise weight reconstruction error is a flawed proxy, as action generation depends only on the repr...

</details>

<details>
<summary>Share</summary>

```
Quantizing in the Loop: Drift-Aware Ultra-Low-Bit Vision-Language-Action Models

Deploying large vision-language-action (VLA) models on resource-constrained robots demands extreme compression, yet existing post-training quantization (PTQ) methods frequently collapse at ultra-low bit-widths ($\le$...

arXiv: https://arxiv.org/abs/2611.30178
Code: https://github.com/ForeverBlue816/LoopQ

#VLA #robotics
```

</details>

---

### [$ζ_0$: A Framework for World Action Models with Joint Scene and Body Foresight in Humanoid Control](https://arxiv.org/abs/2611.29277)

**Authors:** Yizhi Chen, Zhanxiang Cao, Yitong Wang, Junyu Liu, Hongchu Zeng et al. (22 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.CV, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in abstract; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29277) | [PDF](https://arxiv.org/pdf/2611.29277) | [Project Page](https://chenyizhi123.github.io/zeta0-project/) | [Code](https://github.com/chenyizhi123/Zeta0)

<details>
<summary>Abstract</summary>

World Action Models anticipate visual outcomes to guide robot actions, yet humanoid interaction also depends on how the robot's body responds. Visual foresight alone can miss body motion, while latent-distance losses do not directly supervise action responses. We present $ζ_0$, a framework that turns vision-language-action policies into World Action Models by foreseeing future visual features and measured joint trajectories in a shared latent representation. During training, a teacher conditioned on recorded futures provides a reference action response, and dual-response transfer trains the ca...

</details>

<details>
<summary>Share</summary>

```
$ζ_0$: A Framework for World Action Models with Joint Scene and Body Foresight in Humanoid Control

World Action Models anticipate visual outcomes to guide robot actions, yet humanoid interaction also depends on how the robot's body responds.

arXiv: https://arxiv.org/abs/2611.29277
Project page: https://chenyizhi123.github.io/zeta0-project/
Code: https://github.com/chenyizhi123/Zeta0

#VLA #robotics
```

</details>

---

### [JEPA-Tuner: From Predictive Fine-Tuning to Asynchronous Execution of Vision-Language-Action Models](https://arxiv.org/abs/2611.29096)

**Authors:** Jingxiang Qu, Tian Xie, Youngjin Hong, Changhyun Choi, Yang Katie Zhao et al. (6 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29096) | [PDF](https://arxiv.org/pdf/2611.29096) | [Project Page](https://qujx.github.io/JEPA-Tuner-Website)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models generate sequences of actions from visual observations, proprioceptive states, and language instructions. In embodied interaction, executing these actions influences subsequent observations and robot states, providing a natural predictive signal for policy learning. However, standard action-supervised fine-tuning does not explicitly capture these action-conditioned temporal dependencies in the guidance consumed by the action predictor. We introduce JEPA-Tuner, a predictive fine-tuning framework that regularizes the VLA's native policy guidance through action...

</details>

<details>
<summary>Share</summary>

```
JEPA-Tuner: From Predictive Fine-Tuning to Asynchronous Execution of Vision-Language-Action Models

Vision-Language-Action (VLA) models generate sequences of actions from visual observations, proprioceptive states, and language instructions.

arXiv: https://arxiv.org/abs/2611.29096
Project page: https://qujx.github.io/JEPA-Tuner-Website

#VLA #robotics
```

</details>

---

### [ConsisX: Cross-View Consistency Thinking in 3D for Vision-Language-Action Models](https://arxiv.org/abs/2611.30308)

**Authors:** Yunhe Zhang, Long Gao, Yuedong Fu, Gang He, Li Xu et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30308) | [PDF](https://arxiv.org/pdf/2611.30308)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models integrate visual perception and language understanding from vision-language models (VLMs) with action prediction for robotic manipulation. Although multi-view observations provide complementary scene information, VLMs model cross-view interactions based on 2D feature similarity, which can lead to physical inconsistency in the form of cross-view incorrect association between distinct entities and cross-view information fragmentation about the same entity. To address these challenges, we propose ConsisX, a novel VLA framework that integrates cross-view associa...

</details>

<details>
<summary>Share</summary>

```
ConsisX: Cross-View Consistency Thinking in 3D for Vision-Language-Action Models

Vision-language-action (VLA) models integrate visual perception and language understanding from vision-language models (VLMs) with action prediction for robotic manipulation.

arXiv: https://arxiv.org/abs/2611.30308

#VLA #robotics
```

</details>

---

### [Beyond Which: Where, How, and When in Vision-Language-Action Models](https://arxiv.org/abs/2611.30291)

**Authors:** Yunhe Zhang, Long Gao, Yuedong Fu, Gang He, Li Xu et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30291) | [PDF](https://arxiv.org/pdf/2611.30291)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models typically rely on vision-language model (VLM) features as the primary perceptual source for action prediction, showing strong generalization across diverse robotic manipulation tasks. Although VLM features can identify which entities are relevant to action prediction, precise manipulation also requires understanding where task-relevant entities are located within the spatial layout, how their geometric structure constrains physical interaction, and when spatial or geometric information should make a greater contribution to action prediction. To this end, we...

</details>

<details>
<summary>Share</summary>

```
Beyond Which: Where, How, and When in Vision-Language-Action Models

Vision-language-action (VLA) models typically rely on vision-language model (VLM) features as the primary perceptual source for action prediction, showing strong generalization across diverse robotic manipulation tasks.

arXiv: https://arxiv.org/abs/2611.30291

#VLA #robotics
```

</details>

---

### [RMR-VLA: Recurrent Memory Reasoning for Vision-Language-Action Models](https://arxiv.org/abs/2611.30145)

**Authors:** Yiheng Du, Jingqi Tian, Xu Jiang, Jiexuan Zhang, Shuyu Wang et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30145) | [PDF](https://arxiv.org/pdf/2611.30145)

<details>
<summary>Abstract</summary>

Long-horizon, history-dependent robotic manipulation often requires acting on visual cues that have disappeared, such as an object indicated earlier or a target hidden under a moving cup. The key challenge is to maintain what past evidence means for the next action as the scene changes. We introduce Recurrent Memory Reasoning (RMR), an explicit reasoning step that connects memory to action inside a vision-language-action model (VLA), with no external reasoning model. At each update, the VLA first infers an event from visual evidence, then revises the task state and grounds a subgoal in the cur...

</details>

<details>
<summary>Share</summary>

```
RMR-VLA: Recurrent Memory Reasoning for Vision-Language-Action Models

Long-horizon, history-dependent robotic manipulation often requires acting on visual cues that have disappeared, such as an object indicated earlier or a target hidden under a moving cup.

arXiv: https://arxiv.org/abs/2611.30145

#VLA #robotics
```

</details>

---

### [RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See](https://arxiv.org/abs/2611.30209)

**Authors:** Yunbei Zhang, Zijian Jin, Shuaicheng Niu, Baian Chen, Weirui Ye et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30209) | [PDF](https://arxiv.org/pdf/2611.30209) | [Project Page](https://RoboAda.github.io/)

<details>
<summary>Abstract</summary>

Pretrained robot policies decide what to do from camera images, yet some of the physics that decides whether their plans succeed is not visible. An object may look light but be 100 times heavier, and a weakened joint or a lagging controller leaves no trace in the image. When the physics at deployment differs from training, the plan is often still right but is executed as if nothing had changed. Training on such variations in advance cannot handle unseen changes, while adapting once deployed either changes the plan, leaving the miscalibrated commands in place, or updates a robot model by gradie...

</details>

<details>
<summary>Share</summary>

```
RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See

Pretrained robot policies decide what to do from camera images, yet some of the physics that decides whether their plans succeed is not visible.

arXiv: https://arxiv.org/abs/2611.30209
Project page: https://RoboAda.github.io/

#VLA #robotics
```

</details>

---

### [RoboThink: Let the Agent Think, Let the Policy Act](https://arxiv.org/abs/2611.30111)

**Authors:** Yunbei Zhang, Zijian Jin, Janet Wang, Xingchen Zhao, Zhenyu Zhang et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30111) | [PDF](https://arxiv.org/pdf/2611.30111) | [Project Page](https://robo-think.github.io/)

<details>
<summary>Abstract</summary>

Robot policies act in real time but fail without knowing why, whereas a reasoning agent that watches the robot can often tell what went wrong. Existing systems either hand the agent control, which takes minutes per episode, or let it send instructions. Yet a policy follows a new instruction only from a fresh start, since a half-finished task leaves it in states outside its training data. Nor can an instruction fix how the robot moves. If a drift keeps pulling the hand to the left, "push right, slightly" is not a task the policy has learned. We propose RoboThink, in which the agent thinks and t...

</details>

<details>
<summary>Share</summary>

```
RoboThink: Let the Agent Think, Let the Policy Act

Robot policies act in real time but fail without knowing why, whereas a reasoning agent that watches the robot can often tell what went wrong.

arXiv: https://arxiv.org/abs/2611.30111
Project page: https://robo-think.github.io/

#VLA #robotics
```

</details>

---

### [Hierarchical Reasoning Action Head for Tiny Vision-Language-Action Models](https://arxiv.org/abs/2611.29813)

**Authors:** Aditya Makineni, Amitesh Sahoo, Qing Tian

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29813) | [PDF](https://arxiv.org/pdf/2611.29813)

<details>
<summary>Abstract</summary>

Real-time onboard robot control calls for a lightweight vision-language-action (VLA) model, yet shrinking the backbone leaves less capacity for deliberation at inference time. Chain-of-thought decoding, dual-system architectures, and larger backbones can restore deliberation but reintroduce the latency and memory costs that motivated going small. Recurrent action heads offer a lighter alternative by iterating in latent space before committing to an action, but existing designs refine a single undifferentiated state that must simultaneously encode slowly evolving task context and rapidly changi...

</details>

<details>
<summary>Share</summary>

```
Hierarchical Reasoning Action Head for Tiny Vision-Language-Action Models

Real-time onboard robot control calls for a lightweight vision-language-action (VLA) model, yet shrinking the backbone leaves less capacity for deliberation at inference time.

arXiv: https://arxiv.org/abs/2611.29813

#VLA #robotics
```

</details>

---

### [A2I-VLA: A Two-Stage Vision-Language-Action model with Semantic-Physical Alignment and Integration](https://arxiv.org/abs/2611.29279)

**Authors:** Kun Dai, Tianqi Wang, Haibo Lei, Chaoyang Li, Kai Zhang et al. (11 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 3 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29279) | [PDF](https://arxiv.org/pdf/2611.29279)

<details>
<summary>Abstract</summary>

Force and tactile feedback provide essential information about physical interactions in contact-rich manipulation that visual observations alone cannot reliably capture.However, integrating these signals into vision-language-action (VLA) models remains challenging owing to the representational gap between visual-language semantics and physical measurements.To address this challenge, we propose A2I-VLA, a two-stage VLA framework that first learns semantically Aligned force-tactile representations and then Integrates them into a VLA model.In Stage I, a cross-modal alignment loss is introduced to...

</details>

<details>
<summary>Share</summary>

```
A2I-VLA: A Two-Stage Vision-Language-Action model with Semantic-Physical Alignment and Integration

Force and tactile feedback provide essential information about physical interactions in contact-rich manipulation that visual observations alone cannot reliably capture.However, integrating these signals into vision-l...

arXiv: https://arxiv.org/abs/2611.29279

#VLA #robotics
```

</details>

---

### [JKO-GRPO: Augmenting GRPO with Wasserstein Proximal Steps for Flow-Matching VLAs](https://arxiv.org/abs/2611.29646)

**Authors:** Jiyong Kwon, Yikun Bai, Amirhossein Mollaali, Guang Lin

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29646) | [PDF](https://arxiv.org/pdf/2611.29646)

<details>
<summary>Abstract</summary>

Flow-based vision-language-action (VLA) models such as $π_0,π_{0.5}$ generate continuous action chunks by flow matching, and online reinforcement learning (RL) can improve them beyond supervised fine-tuning. Existing methods, such as Flow-GRPO and $π_{\mathrm{RL}}$, optimize likelihood ratios of stochastic denoising transitions, which reweight the sampled actions by their advantages but do not use the distances between them. We propose JKO-GRPO, which augments Flow-GRPO with Wasserstein proximal steps, with two contributions: (1) At each state, we treat the group of sampled actions as an empir...

</details>

<details>
<summary>Share</summary>

```
JKO-GRPO: Augmenting GRPO with Wasserstein Proximal Steps for Flow-Matching VLAs

Flow-based vision-language-action (VLA) models such as $π_0,π_{0.5}$ generate continuous action chunks by flow matching, and online reinforcement learning (RL) can improve them beyond supervised fine-tuning.

arXiv: https://arxiv.org/abs/2611.29646

#VLA #robotics
```

</details>

---

### [Detecting Is Not Choosing: What a World Model Needs to Keep a VLA Policy Safe](https://arxiv.org/abs/2611.29553)

**Authors:** Thanish Bolla

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Also relevant to:** World Models

**Links:** [arXiv](https://arxiv.org/abs/2611.29553) | [PDF](https://arxiv.org/pdf/2611.29553)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) policies complete most benchmark tasks but often violate safety constraints. Since they are stochastic, one remedy is to sample several candidate action chunks and execute one that a world model predicts is safe. We ask what such a model must do. In simulation, a lookahead safety filter with the simulator as an exact world model raises the safety rate of three VLA policies on LIBERO and of pi0.5 on LIBERO-Plus by 11.5 to 25.7 points. It also helps pi0.5 on three RoboCasa tasks. Learned critics trained on one policy's data detect dangerous states (pooled AUROC up to...

</details>

<details>
<summary>Share</summary>

```
Detecting Is Not Choosing: What a World Model Needs to Keep a VLA Policy Safe

Vision-language-action (VLA) policies complete most benchmark tasks but often violate safety constraints.

arXiv: https://arxiv.org/abs/2611.29553

#VLA #robotics
```

</details>

---

### [MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model](https://arxiv.org/abs/2611.29501)

**Authors:** Rongze Tang, Chenyu Zhou, Jianjie Fang, Ziming Liu, Zhaolu Wang et al. (11 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29501) | [PDF](https://arxiv.org/pdf/2611.29501) | [Project Page](https://embodiedcity.github.io/MAWAM/)

<details>
<summary>Abstract</summary>

World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent. In practice, manipulation often requires multiple robots to collaborate across disjoint workspaces, coupled timing, and heterogeneous embodiments. Such coordination demands both spatiotemporal alignment of future interactions and awareness of individual embodiment and role identities, whereas existing decentralized per-robot policies, flat centralized models, and multi-robot VLAs fail to unite both. To bridge this gap, we presen...

</details>

<details>
<summary>Share</summary>

```
MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model

World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent.

arXiv: https://arxiv.org/abs/2611.29501
Project page: https://embodiedcity.github.io/MAWAM/

#VLA #robotics
```

</details>

---

### [Self-Refining VLA Sampling](https://arxiv.org/abs/2611.29383)

**Authors:** Jeff Duan, Arjun Sharma, Jennifer Cruden, Vansh Tibrewal

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "VLA" in title; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29383) | [PDF](https://arxiv.org/pdf/2611.29383)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models typically use flow-based generative modeling to learn a rich, often multimodal, distribution of robot actions. Generating samples from flow-based methods involves iteratively updating random noise, and distinct noise samples from the same state can result in distinct trajectories and task outcomes. Existing test-time scaling methods improve action chunk generation via selection, aggregation, or correction, but commonly require the generation of large ensembles of candidates or the training of an external corrector. We adapt Predict-and-Perturb (P&P), a self-...

</details>

<details>
<summary>Share</summary>

```
Self-Refining VLA Sampling

Vision-Language-Action (VLA) models typically use flow-based generative modeling to learn a rich, often multimodal, distribution of robot actions.

arXiv: https://arxiv.org/abs/2611.29383

#VLA #robotics
```

</details>

---

### [Spatially Grounded Latent Lookahead for Vision-Language-Action Models](https://arxiv.org/abs/2611.28839)

**Authors:** Qihang Chen, Tengjie Li, Hongwei Lu, Jason Wu, Chyna Qu et al. (7 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "vision-language-action" in title; 3 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28839) | [PDF](https://arxiv.org/pdf/2611.28839)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models benefit from strong semantic representations that support object recognition and instruction understanding. However, precise manipulation also depends on resolving object locations and workspace relations, and on selecting actions with an estimate of how the scene will evolve. Existing geometry-aware methods make the current scene more explicit, while predictive methods model future observations or representations. Yet future information is often neither grounded in a control-relevant spatial state nor directly used to guide action generation. We introduce S...

</details>

<details>
<summary>Share</summary>

```
Spatially Grounded Latent Lookahead for Vision-Language-Action Models

Vision-language-action (VLA) models benefit from strong semantic representations that support object recognition and instruction understanding.

arXiv: https://arxiv.org/abs/2611.28839

#VLA #robotics
```

</details>

---

### [MotionServe: Efficient Multi-Robot Serving by Exploiting Robot Execution Slack](https://arxiv.org/abs/2611.30083)

**Authors:** Zikang Wen, Yuning Zhang, Dong Yuan

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.DC | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30083) | [PDF](https://arxiv.org/pdf/2611.30083)

<details>
<summary>Abstract</summary>

As robotic arms undertake diverse manipulation tasks, a deployment may need to serve many task-specific vision-language-action (VLA) policies concurrently. Dedicating a GPU to each robot is costly, motivating shared-GPU inference. Low-rank adaptation (LoRA) allows compatible policies to share a frozen backbone with lightweight policy-specific adapters, reducing model-weight memory and enabling cross-policy batching. However, robot inference must keep pace with physical execution. With action chunking, robots continue executing buffered actions while awaiting new predictions, and the remaining...

</details>

<details>
<summary>Share</summary>

```
MotionServe: Efficient Multi-Robot Serving by Exploiting Robot Execution Slack

As robotic arms undertake diverse manipulation tasks, a deployment may need to serve many task-specific vision-language-action (VLA) policies concurrently.

arXiv: https://arxiv.org/abs/2611.30083

#VLA #robotics
```

</details>

---

### [ProMix: Efficient Data Mixture Optimization for Robotic Imitation via Proxy-Reference DRO](https://arxiv.org/abs/2611.29873)

**Authors:** Qie Sima, Wei Xue, Yike Guo

**Published:** 2026-11-23 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29873) | [PDF](https://arxiv.org/pdf/2611.29873)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models excel in open-world manipulation, yet their performance often saturates when training data are naively pooled across heterogeneous robots, tasks, and environments. Distributionally robust data mixture optimization, exemplified by Re-Mix, can recover much of this performance, but its weight search requires training full-scale policies twice on the entire corpus, placing it out of reach for most laboratories. We present ProMix, a compute-efficient instantiation of the proxy-reference DRO recipe for robotic imitation learning: a 15M-parameter proxy learns per-d...

</details>

<details>
<summary>Share</summary>

```
ProMix: Efficient Data Mixture Optimization for Robotic Imitation via Proxy-Reference DRO

Vision-Language-Action (VLA) models excel in open-world manipulation, yet their performance often saturates when training data are naively pooled across heterogeneous robots, tasks, and environments.

arXiv: https://arxiv.org/abs/2611.29873

#VLA #robotics
```

</details>

---

### [Representation Alignment Is Only as Good as the Teacher's Behavioral Structure](https://arxiv.org/abs/2611.29483)

**Authors:** Zhengfeiyang Zhang, Haoyuan Chen, Hexin Wang, Hanyu Zhou, Zhenglin Wan et al. (7 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29483) | [PDF](https://arxiv.org/pdf/2611.29483)

<details>
<summary>Abstract</summary>

Recent works align the intermediate features of vision-language-action (VLA) models with frozen vision encoders during fine-tuning, hoping to inject additional priors such as 3D awareness or affordances. Unlike in image generation, where teachers for representation alignment (REPA) are assessed with encoder-intrinsic metrics, teachers for VLAs are still chosen largely by heuristics. We show that this practice is unreliable: across 14 teachers and 16 manipulation tasks, under matched training budgets, no off-the-shelf vision encoder improves the clean success rate of $π_{0.5}$ by more than 1 po...

</details>

<details>
<summary>Share</summary>

```
Representation Alignment Is Only as Good as the Teacher's Behavioral Structure

Recent works align the intermediate features of vision-language-action (VLA) models with frozen vision encoders during fine-tuning, hoping to inject additional priors such as 3D awareness or affordances.

arXiv: https://arxiv.org/abs/2611.29483

#VLA #robotics
```

</details>

---

### [More Than Picturing the Future: Motion-Oriented Latent Reasoning for Generalizable Robot Manipulation](https://arxiv.org/abs/2611.29339)

**Authors:** Xin Zhang, Yushuo Hou, Anqi Zhao, Moyun Liu, Xingwei Zhao et al. (8 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29339) | [PDF](https://arxiv.org/pdf/2611.29339)

<details>
<summary>Abstract</summary>

Latent reasoning lets Vision-Language-Action (VLA) models deliberate at a fraction of the cost of explicit chain-of-thought, increasingly through visual foresight, which we show to be indispensable for predicting actions. Yet this paradigm is inherited from Vision-Language Models, where it serves understanding rather than action: each latent is aligned with an isolated future frame, often enriched with further modalities of that frame. We find that this binds the policy to the appearance of its training scenes, so that it degrades sharply once the scene changes. We argue that visual latents fo...

</details>

<details>
<summary>Share</summary>

```
More Than Picturing the Future: Motion-Oriented Latent Reasoning for Generalizable Robot Manipulation

Latent reasoning lets Vision-Language-Action (VLA) models deliberate at a fraction of the cost of explicit chain-of-thought, increasingly through visual foresight, which we show to be indispensable for predicting acti...

arXiv: https://arxiv.org/abs/2611.29339

#VLA #robotics
```

</details>

---

### [InfoField3D: Differentiable Information Field for Embodied Task-Oriented View Planning](https://arxiv.org/abs/2611.29230)

**Authors:** Huan Lyu, Yawei Luo

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29230) | [PDF](https://arxiv.org/pdf/2611.29230)

<details>
<summary>Abstract</summary>

Effective task execution requires embodied agents to select observation positions that provide sufficient task-relevant information. Existing approaches typically predict viewpoints with learned models or score discrete candidates, but they either struggle to incorporate new constraints such as reachability or require extensive candidate evaluation to search. We introduce InfoField3D, which lifts geometry-bound information into a differentiable analytic field, whose value at each 3D observation position represents the task-required information accessible there. It uses low-order spherical harm...

</details>

<details>
<summary>Share</summary>

```
InfoField3D: Differentiable Information Field for Embodied Task-Oriented View Planning

Effective task execution requires embodied agents to select observation positions that provide sufficient task-relevant information.

arXiv: https://arxiv.org/abs/2611.29230

#VLA #robotics
```

</details>

---

### [LIBERO-MOR: A Multimodal Robustness Benchmark Across the Vision-Language-Action Pipeline](https://arxiv.org/abs/2611.28867)

**Authors:** Qihang Chen, Tengjie Li, Hongwei Lu, Jason Wu, Chyna Qu et al. (7 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in title; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28867) | [PDF](https://arxiv.org/pdf/2611.28867)

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models have achieved strong performance on robot manipulation benchmarks. Translating this progress into reliable deployment calls for systematic evaluation of how policies respond to variations throughout the robot interaction loop. We introduce LIBERO-MOR, a multimodal robustness benchmark across the vision-language-action pipeline. Built on standard LIBERO, it covers five deployment-facing domains: vision, language, proprioception, action execution, and environment. The benchmark comprises 22 deployment-inspired perturbations, each evaluated at three severity le...

</details>

<details>
<summary>Share</summary>

```
LIBERO-MOR: A Multimodal Robustness Benchmark Across the Vision-Language-Action Pipeline

Vision-language-action (VLA) models have achieved strong performance on robot manipulation benchmarks.

arXiv: https://arxiv.org/abs/2611.28867

#VLA #robotics
```

</details>

---

### [Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation](https://arxiv.org/abs/2611.29377)

**Authors:** Shilin Shan, Yuxuan Hu, Chuhao Zhou, Yimeng Dong, Bohan Hou et al. (9 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29377) | [PDF](https://arxiv.org/pdf/2611.29377)

<details>
<summary>Abstract</summary>

Agents built on pretrained VLMs have demonstrated zero-shot control of real robots, but vision alone is often insufficient for reliable contact-state assessment in contact-rich manipulation. Force and tactile feedback provide complementary information, but their semantic ambiguity makes them difficult for agents to use directly. These signals must be interpreted according to their physical meaning, together with task phase and visual evidence. We propose Contact Harness, which uses reusable, optimized skills to guide a VLM agent in assessing contact states from multimodal feedback and selectin...

</details>

<details>
<summary>Share</summary>

```
Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation

Agents built on pretrained VLMs have demonstrated zero-shot control of real robots, but vision alone is often insufficient for reliable contact-state assessment in contact-rich manipulation.

arXiv: https://arxiv.org/abs/2611.29377

#VLA #robotics
```

</details>

---

### [A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation](https://arxiv.org/abs/2611.29338)

**Authors:** Meng-Hao Guo, Yi Zhang, Zhe-Han Mo, Han-Zheng Wang, Jia-Jun Wang et al. (14 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29338) | [PDF](https://arxiv.org/pdf/2611.29338)

<details>
<summary>Abstract</summary>

Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced. We introduce nanoAstra, an approach to training vision-language models (VLMs) for generalizable manipulation that combines semantic action modeling with capability-preserving supervised fine-tuning (CP-SFT). nanoAstra represents robot behavior as semantic steps composed of reusable, parameterized action primitives, guided by explicit progress descriptions. Meanwhile, CP-SFT uses an explicit robot-specific system prompt to constra...

</details>

<details>
<summary>Share</summary>

```
A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation

Recently, GPT-6 Astra demonstrates strong generalization in robot control, yet limited disclosure of its training leaves open how such capabilities can be reproduced.

arXiv: https://arxiv.org/abs/2611.29338

#VLA #robotics
```

</details>

---

### [DeRail: Escaping Trajectory Priors via Counterfactual Action Steering for Mid-Execution Instruction Switching](https://arxiv.org/abs/2611.28803)

**Authors:** Yitong Hong, Xiangdong Feng, Xiaoxi Sun, Senqiao Yang, Boyao Han et al. (12 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "VLA" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28803) | [PDF](https://arxiv.org/pdf/2611.28803)

<details>
<summary>Abstract</summary>

Robots operating in the real world must often adapt when user instructions change mid-execution, yet current instruction-conditioned robot policies, including Vision-Language-Action (VLA) models and World-Action Models (WAMs), are largely evaluated under fixed-instruction episodes. We study mid-execution instruction switching and identify trajectory hijacking as a key failure mode, where the policy fails to redirect sufficiently toward the switched target, with its post-switch behavior remaining fully or partially drawn toward trajectories associated with non-target tasks. We propose Counterfa...

</details>

<details>
<summary>Share</summary>

```
DeRail: Escaping Trajectory Priors via Counterfactual Action Steering for Mid-Execution Instruction Switching

Robots operating in the real world must often adapt when user instructions change mid-execution, yet current instruction-conditioned robot policies, including Vision-Language-Action (VLA) models and World-Action Model...

arXiv: https://arxiv.org/abs/2611.28803

#VLA #robotics
```

</details>

---

### [NAT: Scaling Causal Neural Action Tokenizers Across Embodiments](https://arxiv.org/abs/2611.28873)

**Authors:** Ahad Jawaid, Alexander Swerdlow, Yu Xiang

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "vision-language-action" in abstract; 2 distinct keyword hits

**Links:** [arXiv](https://arxiv.org/abs/2611.28873) | [PDF](https://arxiv.org/pdf/2611.28873)

<details>
<summary>Abstract</summary>

Action tokenizers let robot policies treat control as autoregressive next-token prediction. As these policies are trained on larger and more diverse datasets, they will need a universal tokenizer that can encode actions from many embodiments and data sources, including ones it has not seen. We study action tokenization at scale, training on 49k hours of action data from real-world robots, handheld grippers, simulation, and humans. We introduce Neural Action Tokenizer (NAT), a causal tokenizer whose decoder lets actions be executed as their tokens are generated. Across four simulation benchmark...

</details>

<details>
<summary>Share</summary>

```
NAT: Scaling Causal Neural Action Tokenizers Across Embodiments

Action tokenizers let robot policies treat control as autoregressive next-token prediction.

arXiv: https://arxiv.org/abs/2611.28873

#VLA #robotics
```

</details>

---

### [VTLA-RL: Learning Visuotactile Policies for Load-Adaptive Grasping](https://arxiv.org/abs/2611.28752)

**Authors:** Qiwei Wu, Qixuan Li, Xin Xiang, Xiangyu Chen, Xiang Xiao et al. (8 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO | **Relevance:** ★☆☆☆☆

**Why surfaced:** "vision-language-action" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.28752) | [PDF](https://arxiv.org/pdf/2611.28752)

<details>
<summary>Abstract</summary>

Vision-language-action foundation models learn general manipulation priors, but object mass and local slip are difficult to infer from vision alone. Changing loads require contact-driven grasp adjustments that demonstrations collected under fixed conditions may not adequately cover. We present VTLA-RL to study visuotactile grasping policies and their reinforcement learning (RL) post-training under varying loads. Our main approach shares a visual encoder between tactile-image histories and RGB inputs to jointly generate and execute motion and bilateral force targets in a unified action space. M...

</details>

<details>
<summary>Share</summary>

```
VTLA-RL: Learning Visuotactile Policies for Load-Adaptive Grasping

Vision-language-action foundation models learn general manipulation priors, but object mass and local slip are difficult to infer from vision alone.

arXiv: https://arxiv.org/abs/2611.28752

#VLA #robotics
```

</details>

---

## World Models (27)

### [JEPA-Shield: Safe Diffusion Planning with Latent World Models via Conformal Shielding](https://arxiv.org/abs/2611.29609)

**Authors:** Taekyung Kim, Ege Yuceel, Steven Hong, Georgios Fainekos, Dimitra Panagou et al. (6 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.AI | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29609) | [PDF](https://arxiv.org/pdf/2611.29609) | [Project Page](https://www.taekyung.me/jepa-shield)

<details>
<summary>Abstract</summary>

Latent world models enable planning from images, but their predictions do not directly establish whether a robot will satisfy physical constraints. We present JEPA-Shield, which connects a frozen action-conditioned Joint-Embedding Predictive Architecture (JEPA) world model to task-space safety enforcement. Two downstream models predict relative motion from imagined latent rollouts and decode unsafe geometry from the current image. Split conformal prediction turns end-to-end motion-prediction errors into multi-horizon uncertainty tubes. A backup-based shield checks these tubes against physical...

</details>

<details>
<summary>Share</summary>

```
JEPA-Shield: Safe Diffusion Planning with Latent World Models via Conformal Shielding

Latent world models enable planning from images, but their predictions do not directly establish whether a robot will satisfy physical constraints.

arXiv: https://arxiv.org/abs/2611.29609
Project page: https://www.taekyung.me/jepa-shield

#worldmodels #robotics
```

</details>

---

### [DriveOddsBench: Are Driving Video World Models Aligned with Real-World Odds?](https://arxiv.org/abs/2611.29275)

**Authors:** Jiaxi Liu, Keshu Wu, Bin Ran, Xiaopeng Li

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★★★☆

**Why surfaced:** "world model" in title; project page; code repo; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29275) | [PDF](https://arxiv.org/pdf/2611.29275) | [Project Page](https://hhjj233.github.io/DriveOddsBench-page/) | [Code](https://github.com/hhjj233/DriveOddsBench)

<details>
<summary>Abstract</summary>

Video world models predict how a scene will evolve, and their sampled futures are increasingly used in place of the real one, from planning to simulation. These uses assume that the samples are aligned with real-world odds, with each future appearing among them as often as it would follow the same history in reality, yet current evaluations only score how real each sample looks. Testing this assumption on real driving data is hard for three reasons. Each recorded history has only one real future, so the true probabilities are unknown. Physical quantities must be read from video, where reading...

</details>

<details>
<summary>Share</summary>

```
DriveOddsBench: Are Driving Video World Models Aligned with Real-World Odds?

Video world models predict how a scene will evolve, and their sampled futures are increasingly used in place of the real one, from planning to simulation.

arXiv: https://arxiv.org/abs/2611.29275
Project page: https://hhjj233.github.io/DriveOddsBench-page/
Code: https://github.com/hhjj233/DriveOddsBench

#worldmodels #robotics
```

</details>

---

### [EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution](https://arxiv.org/abs/2611.30004)

**Authors:** Zehao Liu, Huashuo Lei, Xi Lin, Haoang Li, Yuliang Chen et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.CR, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30004) | [PDF](https://arxiv.org/pdf/2611.30004) | [Code](https://github.com/INKSIR/Envtrap)

<details>
<summary>Abstract</summary>

As AI models evolve from text and vision to physical agents, embodied AI faces a fundamentally different attack surface. Prior attacks on embodied systems have used crafted instructions, adversarial visual inputs, and training-time policy modifications; we study environment-only object rearrangements with unchanged models and instructions. We reveal an attack surface in safety-critical spatial relations among existing objects. An adversary who rearranges objects, without modifying instructions or accessing models, can cause hazardous consequences. In this work, we propose EnvTrap, a diagnostic...

</details>

<details>
<summary>Share</summary>

```
EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution

As AI models evolve from text and vision to physical agents, embodied AI faces a fundamentally different attack surface.

arXiv: https://arxiv.org/abs/2611.30004
Code: https://github.com/INKSIR/Envtrap

#worldmodels #robotics
```

</details>

---

### [AxE: Benchmarking Agent-Environment Generalization of Video World Models via Grounded Events](https://arxiv.org/abs/2611.30120)

**Authors:** Haiyu Xu, Yiyang Chen, Jiayi Zhou, Jiaming Ji, Juntao Dai et al. (7 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.30120) | [PDF](https://arxiv.org/pdf/2611.30120) | [Project Page](https://AxEBench.github.io)

<details>
<summary>Abstract</summary>

Edge cases are not the long tail; they are the norm. An embodied system deployed across changing environments, bodies, objects, and tasks will routinely encounter combinations that were absent from its training data. General-purpose physical intelligence therefore requires world models that reuse prior knowledge, predict consequences, and adapt with little or no additional training. Yet current evaluations of conditional video generation emphasize visual quality, prompt alignment, or isolated physical plausibility, leaving systematic generalization difficult to measure. We introduce AxE Bench,...

</details>

<details>
<summary>Share</summary>

```
AxE: Benchmarking Agent-Environment Generalization of Video World Models via Grounded Events

Edge cases are not the long tail; they are the norm.

arXiv: https://arxiv.org/abs/2611.30120
Project page: https://AxEBench.github.io

#worldmodels #robotics
```

</details>

---

### [Seeing Together, Acting Apart: Shared Environmental Understanding for Multi-Robot Navigation](https://arxiv.org/abs/2611.30310)

**Authors:** Haihong Hao, Lei Chen, Mingfei Han, Chenglong Yan, Dong An et al. (10 authors)

**Published:** 2026-11-23 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30310) | [PDF](https://arxiv.org/pdf/2611.30310)

<details>
<summary>Abstract</summary>

Multi-robot embodied systems are typically designed to collaborate by coordinating actions, sharing trajectories, or learning joint policies. We ask a complementary question: can collaboration emerge before decision-making, by first building a shared understanding of the environment? We introduce Shared Environmental Understanding, a policy-agnostic representation that aggregates partial egocentric observations from multiple robots into a shared latent world model. This shifts collaboration from the policy space to the representation space, enabling decentralized decision-making with shared en...

</details>

<details>
<summary>Share</summary>

```
Seeing Together, Acting Apart: Shared Environmental Understanding for Multi-Robot Navigation

Multi-robot embodied systems are typically designed to collaborate by coordinating actions, sharing trajectories, or learning joint policies.

arXiv: https://arxiv.org/abs/2611.30310

#worldmodels #robotics
```

</details>

---

### [How Latent Transition Geometry Matters for Planning in World Models](https://arxiv.org/abs/2611.30064)

**Authors:** Xuanya Zhu, Da Li, Xiatian Zhu

**Published:** 2026-11-23 | **Categories:** cs.LG, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30064) | [PDF](https://arxiv.org/pdf/2611.30064)

<details>
<summary>Abstract</summary>

World models support planning by predicting how the environment evolves under candidate actions. However, one-step predictive accuracy alone does not characterize multi-step planning utility, which depends on distinguishing candidate futures. This raises a natural question: How does latent transition geometry shape planning? We investigate this through an action-conditioned transition-field view, using curvature regularization as a controlled intervention. Across four continuous-control tasks, appropriately tuned regularization improves planning, while excessive regularization can be detriment...

</details>

<details>
<summary>Share</summary>

```
How Latent Transition Geometry Matters for Planning in World Models

World models support planning by predicting how the environment evolves under candidate actions.

arXiv: https://arxiv.org/abs/2611.30064

#worldmodels #robotics
```

</details>

---

### [CarlHOI: Counterfactual Predictive Imagination for Generalizable Multi-Humanoid Object Interaction under Constrained Environments](https://arxiv.org/abs/2611.29749)

**Authors:** Wenjie Lin, Jin Wei-Kocsis

**Published:** 2026-11-22 | **Categories:** cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; project page; posted in last 2 days

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.29749) | [PDF](https://arxiv.org/pdf/2611.29749) | [Project Page](https://carlhoi.github.io)

<details>
<summary>Abstract</summary>

Recent advances in physics-based humanoid control enable teams of varying sizes to coordinate their movements and cooperatively transport shared objects. However, adapting learned cooperative behaviors to unseen environmental constraints remains challenging, particularly when obstacles require coordinated detours and changes in team configuration. We propose CarlHOI, a counterfactual predictive imagination framework built upon a counterfactual-anchored relational latent world model (CarlWM) for human-object interaction (HOI), enabling multi-humanoid teams to adapt to unseen environmental const...

</details>

<details>
<summary>Share</summary>

```
CarlHOI: Counterfactual Predictive Imagination for Generalizable Multi-Humanoid Object Interaction under Constrained Environments

Recent advances in physics-based humanoid control enable teams of varying sizes to coordinate their movements and cooperatively transport shared objects.

arXiv: https://arxiv.org/abs/2611.29749
Project page: https://carlhoi.github.io

#worldmodels #robotics
```

</details>

---

### [Imagine Smarter, Drive Faster: Efficient World Modeling for Decision-Aware Autonomous Driving](https://arxiv.org/abs/2611.28779)

**Authors:** Feiyang Jia, Lin Liu, Zhicheng Bao, Caiyan Jia, Ziying Song et al. (9 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★★☆☆

**Why surfaced:** "world model" in abstract; code repo; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.28779) | [PDF](https://arxiv.org/pdf/2611.28779) | [Code](https://github.com/MoyangSensei/FastWorld)

<details>
<summary>Abstract</summary>

World models hold great promise for autonomous driving planning, yet their ability to imagine the future often comes at a formidable computational cost. Efficiency efforts, such as knowledge distillation and domain-specific pre-training, often shift this burden to costly teachers or training pipelines, leaving lightweight world modeling an open challenge. We introduce FastWorld, a natively lightweight world-model framework for efficient autonomous driving planning. FastWorld reduces computation through compact scene representations, short-horizon action-conditioned prediction, and selective ca...

</details>

<details>
<summary>Share</summary>

```
Imagine Smarter, Drive Faster: Efficient World Modeling for Decision-Aware Autonomous Driving

World models hold great promise for autonomous driving planning, yet their ability to imagine the future often comes at a formidable computational cost.

arXiv: https://arxiv.org/abs/2611.28779
Code: https://github.com/MoyangSensei/FastWorld

#worldmodels #robotics
```

</details>

---

### [SANA-Robot: Efficient World Action Model with Hybrid Memory](https://arxiv.org/abs/2611.28943)

**Authors:** Yuyang Zhao, Zekai Li, Yicheng Pan, Jiaming Tang, Zhuoyang Zhang et al. (12 authors)

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.CV | **Relevance:** ★★★☆☆

**Why surfaced:** "world simulator" in abstract; project page; robotics / embodied focus

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.28943) | [PDF](https://arxiv.org/pdf/2611.28943) | [Project Page](https://nvlabs.github.io/Sana/Robot/)

<details>
<summary>Abstract</summary>

World action models (WAMs) leverage the world knowledge of video generation models to improve action generation by aligning visual prediction with action prediction. However, their prediction overhead prevents real-time deployment on edge devices, and they usually lack an effective long-term memory. We introduce SANA-Robot, a 4.5B WAM with minute-level memory that runs in real time on edge devices, built on the following core designs: (1) hybrid memory at constant cost: our WAM relies on linear attention to maintain a global memory with a fixed-size state, and on sliding window softmax attenti...

</details>

<details>
<summary>Share</summary>

```
SANA-Robot: Efficient World Action Model with Hybrid Memory

World action models (WAMs) leverage the world knowledge of video generation models to improve action generation by aligning visual prediction with action prediction.

arXiv: https://arxiv.org/abs/2611.28943
Project page: https://nvlabs.github.io/Sana/Robot/

#worldmodels #robotics
```

</details>

---

### [SilentWAM: Planning in the Masked State of a Diffusion World Model](https://arxiv.org/abs/2611.29125)

**Authors:** Ziyu Zhao, Casey Sun, Zeyu Wang, Shicong Ma, Emily T Zhang et al. (6 authors)

**Published:** 2026-11-22 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29125) | [PDF](https://arxiv.org/pdf/2611.29125)

<details>
<summary>Abstract</summary>

World-action models learn from future prediction, but accessing their future representations directly at test time can require costly frame generation. Methods that generate future frames before planning incur additional forward passes, while future co-training methods omit explicit future predictions at inference. We introduce \method, a planner that reads the hidden states of masked future tokens without decoding future frames. We pretrain MMaDA-Parallel-M on driving video using frame-level masked world modeling, which predicts a masked suffix of future frames and explicitly includes inputs...

</details>

<details>
<summary>Share</summary>

```
SilentWAM: Planning in the Masked State of a Diffusion World Model

World-action models learn from future prediction, but accessing their future representations directly at test time can require costly frame generation.

arXiv: https://arxiv.org/abs/2611.29125

#worldmodels #robotics
```

</details>

---

### [MOVER: Planning Beyond Motion](https://arxiv.org/abs/2611.30022)

**Authors:** Xiangyu Li, Yu Jiang, Tianyi Wang, Liang He, Qixing Huang et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.CV, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; robotics / embodied focus; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30022) | [PDF](https://arxiv.org/pdf/2611.30022)

<details>
<summary>Abstract</summary>

Residual world models forecast a driving scene through its temporal change, so feature components that stay constant over time vanish from the residual pathway. We ask whether evidence with weak temporal change, such as a waiting pedestrian or a stopped vehicle, can be used more effectively for planning, and introduce MOVER, a complementary event-routing mechanism. A training-time teacher measures how each spatially grounded event query responds when a past frame is removed from shared history and contrasts that sensitivity with the event's pooled temporal residual, prioritizing events that de...

</details>

<details>
<summary>Share</summary>

```
MOVER: Planning Beyond Motion

Residual world models forecast a driving scene through its temporal change, so feature components that stay constant over time vanish from the residual pathway.

arXiv: https://arxiv.org/abs/2611.30022

#worldmodels #robotics
```

</details>

---

### [Dynamics Forcing: Mitigating Error Accumulation in Causal Video World Models](https://arxiv.org/abs/2611.29839)

**Authors:** Xin Zhou, Cong Miao

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.AI, cs.RO | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29839) | [PDF](https://arxiv.org/pdf/2611.29839)

<details>
<summary>Abstract</summary>

Causal video world models generate block by block from their own previous outputs. Small errors in early blocks are fed back as history and grow until the scene and the robot fall apart. Teacher forcing trains on clean ground-truth history, so the model never sees the history it will actually condition on, and it also finds a shortcut: copying the previous frame instead of predicting how the scene changes. We present Dynamics Forcing, a training scheme that keeps real video as the only supervision and reshapes how history is presented. History is perturbed in three ways: random noising, self-r...

</details>

<details>
<summary>Share</summary>

```
Dynamics Forcing: Mitigating Error Accumulation in Causal Video World Models

Causal video world models generate block by block from their own previous outputs.

arXiv: https://arxiv.org/abs/2611.29839

#worldmodels #robotics
```

</details>

---

### [What Test-Time Training Corrects in Latent World Models? A Slow-Fast Approach](https://arxiv.org/abs/2611.29453)

**Authors:** Shuaicheng Niu, Guohao Chen, Kevin Z. Shen, Yunbei Zhang, Peilin Zhao et al. (7 authors)

**Published:** 2026-11-22 | **Categories:** cs.RO, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29453) | [PDF](https://arxiv.org/pdf/2611.29453)

<details>
<summary>Abstract</summary>

Latent world models plan toward a goal by predicting the outcomes of candidate actions, but under the distribution shift, prediction errors can lead the planner astray. Test-time training using executed actions helps, yet what it corrects and whether its updates should persist across episodes remains unclear. We address both by analyzing the world model's prediction error. On PushObj, an object-pushing task, we probe multiple actions from the same state and decompose the error into an offset shared across actions and an action-dependent component. The offset effectively shifts the planner's go...

</details>

<details>
<summary>Share</summary>

```
What Test-Time Training Corrects in Latent World Models? A Slow-Fast Approach

Latent world models plan toward a goal by predicting the outcomes of candidate actions, but under the distribution shift, prediction errors can lead the planner astray.

arXiv: https://arxiv.org/abs/2611.29453

#worldmodels #robotics
```

</details>

---

### [SWAM: State-aware World Action Model for Multi-Agent 3D Environments](https://arxiv.org/abs/2611.30042)

**Authors:** Jenna Kang, Bingxuan Li, Colin Groth, Anatolii Evdokimov, Sai Zhang et al. (6 authors)

**Published:** 2026-11-23 | **Categories:** cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; 2 distinct keyword hits; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.30042) | [PDF](https://arxiv.org/pdf/2611.30042)

<details>
<summary>Abstract</summary>

Interactive world models generate virtual environments autoregressively from player actions and visual history. However, visual history alone cannot reliably capture the evolving states of independently acting non-player characters (NPCs) in real games, particularly when they are outside the camera view. Recent multi-agent world models address this challenge through joint multi-view generation or persistent shared state, but often rely on external observations, like maps or scene geometry, or predefined state transitions. We present SWAM, a State-aware World Action Model that separates agent-s...

</details>

<details>
<summary>Share</summary>

```
SWAM: State-aware World Action Model for Multi-Agent 3D Environments

Interactive world models generate virtual environments autoregressively from player actions and visual history.

arXiv: https://arxiv.org/abs/2611.30042

#worldmodels #robotics
```

</details>

---

### [World Models and the Law](https://arxiv.org/abs/2611.29899)

**Authors:** Claudio Novelli

**Published:** 2026-11-23 | **Categories:** cs.ET, cs.AI, cs.CY | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29899) | [PDF](https://arxiv.org/pdf/2611.29899)

<details>
<summary>Abstract</summary>

Current AI may have a model of how we use human language, but this does not translate into a reliable representation of physical reality. World models promise to fill this gap by learning how an environment changes over time and predicting the consequences of an action, and they are already used to steer robots and generate explorable worlds. This article asks how AI regulation in three major legal contexts, the European Union, California, and China, copes with the distinctive challenges they raise. I propose a definition and a taxonomy of world models based on who or what acts on their predic...

</details>

<details>
<summary>Share</summary>

```
World Models and the Law

Current AI may have a model of how we use human language, but this does not translate into a reliable representation of physical reality.

arXiv: https://arxiv.org/abs/2611.29899

#worldmodels #robotics
```

</details>

---

### [World Models Are the Right Foundation for Simulating Mars Terraforming](https://arxiv.org/abs/2611.29856)

**Authors:** Sameera S Kashyap, Akshitha Nagaraj, Razvan Marinescu

**Published:** 2026-11-23 | **Categories:** cs.LG, astro-ph.EP, astro-ph.IM | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29856) | [PDF](https://arxiv.org/pdf/2611.29856)

<details>
<summary>Abstract</summary>

Terraforming Mars is a long-horizon, action-conditioned control problem that requires predicting atmospheric responses to interventions over centuries to identify effective policies. This position paper argues that physics-regularized recurrent state-space world models are the most promising foundation for this setting. Data-driven climate emulators lack action-conditioning, and physics-based general circulation models (GCMs) are too expensive for policy search. Among learned world models, recurrent state-space architectures with physics constraints are better suited than transformer-based alt...

</details>

<details>
<summary>Share</summary>

```
World Models Are the Right Foundation for Simulating Mars Terraforming

Terraforming Mars is a long-horizon, action-conditioned control problem that requires predicting atmospheric responses to interventions over centuries to identify effective policies.

arXiv: https://arxiv.org/abs/2611.29856

#worldmodels #robotics
```

</details>

---

### [What Should World Models Plan Over? Learning Geometry-Aligned Representations of Body Motion](https://arxiv.org/abs/2611.29759)

**Authors:** Renhao Zhang, Abhranil Chandra, Bruno Castro da Silva

**Published:** 2026-11-22 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29759) | [PDF](https://arxiv.org/pdf/2611.29759)

<details>
<summary>Abstract</summary>

We introduce MotionPort, which learns low-dimensional latent representations of body motion for accurate dynamics prediction and effective long-horizon planning. Existing world-model planners often search over action representations learned for prediction, yet we show that predictive accuracy alone does not ensure that optimization can discover successful trajectories. MotionPort addresses this mismatch by representing body trajectories rather than action chunks and organizing the search space by motion similarity, helping predicted improvements translate into successful execution. Without fin...

</details>

<details>
<summary>Share</summary>

```
What Should World Models Plan Over? Learning Geometry-Aligned Representations of Body Motion

We introduce MotionPort, which learns low-dimensional latent representations of body motion for accurate dynamics prediction and effective long-horizon planning.

arXiv: https://arxiv.org/abs/2611.29759

#worldmodels #robotics
```

</details>

---

### [RadioWorld: Transferring World Models to Radio-Frequency Radiance Fields](https://arxiv.org/abs/2611.29282)

**Authors:** Hu Zhou, Jiazhou Zhou, Shuowen Zhang, Ying-Chang Liang, Liang Liu

**Published:** 2026-11-22 | **Categories:** cs.CV, cs.NI, eess.SP | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29282) | [PDF](https://arxiv.org/pdf/2611.29282)

<details>
<summary>Abstract</summary>

Electromagnetic (EM) wave propagation in the physical world constitutes a Radio-Frequency (RF) radiance field, providing rich information for 6G communication and sensing. However, existing neural RF field methods suffer from three fundamental limitations: (1) they predominantly rely on per-scene optimization and cannot generalize to unseen scenes; (2) they require costly reference RF measurements in each target scene; and (3) they degrade severely when extrapolating beyond the vicinity of reference measurements. To overcome these limitations, we present RadioWorld, a general framework that ad...

</details>

<details>
<summary>Share</summary>

```
RadioWorld: Transferring World Models to Radio-Frequency Radiance Fields

Electromagnetic (EM) wave propagation in the physical world constitutes a Radio-Frequency (RF) radiance field, providing rich information for 6G communication and sensing.

arXiv: https://arxiv.org/abs/2611.29282

#worldmodels #robotics
```

</details>

---

### [When Do Better Visual World Models Make Better Plans? Decision-Aligned Selection for Latent Planning](https://arxiv.org/abs/2611.28919)

**Authors:** Chan Aristella Lu, Arya Fayyazi, Junil Yeo, Jin Lu, Kyu Hyung Lee et al. (7 authors)

**Published:** 2026-11-21 | **Categories:** cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28919) | [PDF](https://arxiv.org/pdf/2611.28919)

<details>
<summary>Abstract</summary>

Visual world models enable goal-conditioned planning by predicting the outcomes of candidate actions in latent space. However, planning depends on how well a model ranks candidates, whereas training optimizes how accurately it predicts each one. We identify the Decision-Relevant Residual (DRR), the part of the cost error that can reorder candidates, and show that the more training reduces the DRR, the more it improves selection (Spearman $ρ= 0.82$, vs. $0.61$ for prediction error). Building on this insight, we introduce Decision-Aligned Selection (DAS), a plug-in selection rule that scores can...

</details>

<details>
<summary>Share</summary>

```
When Do Better Visual World Models Make Better Plans? Decision-Aligned Selection for Latent Planning

Visual world models enable goal-conditioned planning by predicting the outcomes of candidate actions in latent space.

arXiv: https://arxiv.org/abs/2611.28919

#worldmodels #robotics
```

</details>

---

### [ViTrust: Learning 3D Observation Trust for Deformable Physical World Models](https://arxiv.org/abs/2611.28815)

**Authors:** Zhihao Guo, Zhihao Li, Xu Ge, Lijian Zhong, Yu Lu et al. (8 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28815) | [PDF](https://arxiv.org/pdf/2611.28815)

<details>
<summary>Abstract</summary>

Learning deformable physical world models requires dynamics that generalize beyond observed motion. Accurate reconstruction alone does not ensure accurate future prediction, motivating us to learn how observations should influence physical identification. However, visual reliability alone does not determine how informative an observation is about physical dynamics. We propose ViTrust to learn 3D observation trust, determining how strongly each tracked point influences physical identification. Its key design is a visual-contact trust adapter that combines pointwise spatiotemporal evidence with...

</details>

<details>
<summary>Share</summary>

```
ViTrust: Learning 3D Observation Trust for Deformable Physical World Models

Learning deformable physical world models requires dynamics that generalize beyond observed motion.

arXiv: https://arxiv.org/abs/2611.28815

#worldmodels #robotics
```

</details>

---

### [ArgsWorld: Unifying 3DGS Scene Reconstruction, Generation and Extrapolation with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2611.28792)

**Authors:** Weiming Chen, Shuaiyan Liu, Xinyu Shao, Zhewen Chen, Tian Guan et al. (7 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; project page

**Links:** 🔗 [arXiv](https://arxiv.org/abs/2611.28792) | [PDF](https://arxiv.org/pdf/2611.28792) | [Project Page](https://m4a1tastegood.github.io/ArgsWorld/)

<details>
<summary>Abstract</summary>

Autoregressive diffusion world models deliver strong video generation performance, yet they typically output only RGB frames rather than explicit 3D Gaussian Splatting (3DGS) scene representations, creating a gap between learned visual world dynamics and usable 3D assets for downstream robotics, simulation and rendering. To bridge this gap, we introduce ArgsWorld, an autoregressive diffusion model that also produces an explicit 3DGS scene. For each generation chunk, the diffusion transformer jointly processes clean historical image latents and noisy latents for new views. It keeps the historic...

</details>

<details>
<summary>Share</summary>

```
ArgsWorld: Unifying 3DGS Scene Reconstruction, Generation and Extrapolation with Autoregressive Diffusion Transformer

Autoregressive diffusion world models deliver strong video generation performance, yet they typically output only RGB frames rather than explicit 3D Gaussian Splatting (3DGS) scene representations, creating a gap betw...

arXiv: https://arxiv.org/abs/2611.28792
Project page: https://m4a1tastegood.github.io/ArgsWorld/

#worldmodels #robotics
```

</details>

---

### [AERIN: Aerial Instance Navigation with a Visual World Model](https://arxiv.org/abs/2611.28723)

**Authors:** Zhenzhen Jiao, Rui Tian, Zhineng Chen

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.AI | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title; robotics / embodied focus

**Links:** [arXiv](https://arxiv.org/abs/2611.28723) | [PDF](https://arxiv.org/pdf/2611.28723)

<details>
<summary>Abstract</summary>

Searching from high altitude and navigating to a target instance specified by a reference image is a common application for UAVs. In such tasks, high-altitude observations provide broad ground coverage for efficient search, but targets occupy fewer pixels, making instance verification and action selection more difficult. We present AERIN, a visual world model that uses action-conditioned prediction to guide the UAV toward the target while adjusting its viewpoint to obtain higherquality observations for subsequent instance verification. Highaltitude navigation requires fine-grained target detai...

</details>

<details>
<summary>Share</summary>

```
AERIN: Aerial Instance Navigation with a Visual World Model

Searching from high altitude and navigating to a target instance specified by a reference image is a common application for UAVs.

arXiv: https://arxiv.org/abs/2611.28723

#worldmodels #robotics
```

</details>

---

### [World Models for Ocean Engineering: A Critical Review of Maritime Autonomy, Adaptive Latent Prediction, Digital Twins, and Biodiversity Monitoring](https://arxiv.org/abs/2611.28978)

**Authors:** Basma Dokkara, Esteban W. G. Cluab, Luiz M. G. Goncalves, Paolo Spagnolo, Cosimo Distante

**Published:** 2026-11-21 | **Categories:** cs.RO, cs.AI, cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.28978) | [PDF](https://arxiv.org/pdf/2611.28978)

<details>
<summary>Abstract</summary>

Marine robots face partial observability, non-stationary dynamics, and sparse communication, motivating WMs that learn compact predictive states for planning. This review develops a functional taxonomy of WMs for ocean engineering, focusing on Joint-Embedding Predictive Architectures (JEPAs) and AdaJEPA's test-time adaptation within model predictive control, mapping them to navigation, adaptive sampling, digital twins, and biodiversity monitoring, and separating demonstrated evidence from prospective applications. The synthesis identifies key Gaps: benchmarks, uncertainty calibration, safe ada...

</details>

<details>
<summary>Share</summary>

```
World Models for Ocean Engineering: A Critical Review of Maritime Autonomy, Adaptive Latent Prediction, Digital Twins, and Biodiversity Monitoring

Marine robots face partial observability, non-stationary dynamics, and sparse communication, motivating WMs that learn compact predictive states for planning.

arXiv: https://arxiv.org/abs/2611.28978

#worldmodels #robotics
```

</details>

---

### [From States to Dynamics: Detecting Rule Violations in OthelloGPT](https://arxiv.org/abs/2611.29715)

**Authors:** David L. Cao, Sai Sumedh R. Hindupur, Demba Ba

**Published:** 2026-11-22 | **Categories:** cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29715) | [PDF](https://arxiv.org/pdf/2611.29715)

<details>
<summary>Abstract</summary>

Sequence models trained on game moves have been shown to encode world models, with structured linear probes revealing the underlying game states. World models, however, are inherently dynamic: in deterministic board games, a set of rules constrain how states evolve over time. We therefore ask if and how OthelloGPT, a transformer trained only on Othello move sequences, manifests the rules of the game in its activation space. We divide the rules of Othello, and symmetrically their violations, into three classes: placing a disc on an empty square (R1), flanking an opponent's disc (R2), and moving...

</details>

<details>
<summary>Share</summary>

```
From States to Dynamics: Detecting Rule Violations in OthelloGPT

Sequence models trained on game moves have been shown to encode world models, with structured linear probes revealing the underlying game states.

arXiv: https://arxiv.org/abs/2611.29715

#worldmodels #robotics
```

</details>

---

### [ClothCast: Generative Cloth World Modeling under Partial Observability](https://arxiv.org/abs/2611.29369)

**Authors:** Yushen Hu, Yilong Song, Zhen Zhou, Apurv Kushwaha, Harshvardhan Chandirasekar et al. (6 authors)

**Published:** 2026-11-22 | **Categories:** cs.CV | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in abstract; posted in last 2 days

**Links:** [arXiv](https://arxiv.org/abs/2611.29369) | [PDF](https://arxiv.org/pdf/2611.29369)

<details>
<summary>Abstract</summary>

World models support robotic manipulation by predicting how the scene evolves under a planned action. For garments this prediction is notoriously difficult: deformations are complex, and self-occlusion leaves much of the cloth unobserved. Planned gripper trajectories provide a useful motion prior because cloth held by a gripper moves with it, while the remaining deformation must be predicted. We introduce ClothCast, a world model that applies this prior to the cloth's points and learns the residual motion. ClothCast takes one RGB-D observation, the camera pose, the robot's own model and the pl...

</details>

<details>
<summary>Share</summary>

```
ClothCast: Generative Cloth World Modeling under Partial Observability

World models support robotic manipulation by predicting how the scene evolves under a planned action.

arXiv: https://arxiv.org/abs/2611.29369

#worldmodels #robotics
```

</details>

---

### [Learning Land-Surface Hydrology World Model from Satellite Observations](https://arxiv.org/abs/2611.28963)

**Authors:** Suya Li, Zekun Qi, Xiaochong Xu, Duo Zhang

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.AI, cs.LG | **Relevance:** ★★☆☆☆

**Why surfaced:** "world model" in title

**Links:** [arXiv](https://arxiv.org/abs/2611.28963) | [PDF](https://arxiv.org/pdf/2611.28963)

<details>
<summary>Abstract</summary>

A world model should tell us not only what will happen, but what would happen under a different action. Learned Earth models now forecast remarkably well, yet forecast skill says little about what their state means or how it responds to a changed driver. We build LandWM, a world model of land-surface water in which rain is the action, learned from seven years of SMAP and CYGNSS observations: physical observation operators tie its latent state to soil water, and a mass-conserving balance governs how that state responds to rain. Over the U.S. Southern Great Plains, the model, never shown a soil-...

</details>

<details>
<summary>Share</summary>

```
Learning Land-Surface Hydrology World Model from Satellite Observations

A world model should tell us not only what will happen, but what would happen under a different action.

arXiv: https://arxiv.org/abs/2611.28963

#worldmodels #robotics
```

</details>

---

### [KineState-SWAM: A Surgical World Action Model with Explicit Kinematics and Causal Interaction Dynamics](https://arxiv.org/abs/2611.28871)

**Authors:** Rulin Zhou, Yujie Ma, Rui Tang, Qiujie Song, Wanhao Liu et al. (9 authors)

**Published:** 2026-11-21 | **Categories:** cs.CV, cs.AI | **Relevance:** ★☆☆☆☆

**Why surfaced:** "world model" in abstract

**Links:** [arXiv](https://arxiv.org/abs/2611.28871) | [PDF](https://arxiv.org/pdf/2611.28871)

<details>
<summary>Abstract</summary>

Existing surgical world models often leave implicit how instrument motion drives localized tissue responses and how interaction history informs subsequent actions. We introduce KineState-SWAM, a surgical world-action model coupling action prediction and video generation through a persistent interaction state, separating kinematically determined instrument motion from learned scene evolution. A flow-matching policy predicts joint trajectories conditioned on interaction state, robot configuration, and task instruction. Kinematic Geometry Conditioning converts these trajectories into surface-moti...

</details>

<details>
<summary>Share</summary>

```
KineState-SWAM: A Surgical World Action Model with Explicit Kinematics and Causal Interaction Dynamics

Existing surgical world models often leave implicit how instrument motion drives localized tissue responses and how interaction history informs subsequent actions.

arXiv: https://arxiv.org/abs/2611.28871

#worldmodels #robotics
```

</details>

---
