# Vision-Language-Action Models

Papers on VLAs and vision-language-action architectures for robotics.

**Last updated:** 2026-05-16 22:36 UTC

**Papers found:** 4

[Back to Home](../README.md)

---

## Papers with Project Pages / Code

### [IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/abs/2605.14712v1)

**Authors:** Shijie Lian, Bin Yu, Xiaopeng Lin, Zhaolong Shen, Laurence Tianruo Yang et al. (11 authors)

**Published:** 2026-05-14 | **Categories:** cs.RO, cs.AI, cs.CL

**Links:** [arXiv](https://arxiv.org/abs/2605.14712v1) | [PDF](https://arxiv.org/pdf/2605.14712v1.pdf) | [GitHub](https://github.com/ZGC-EmbodyAI/IntentVLA)

<details>
<summary>Abstract</summary>

Robot imitation data are often multimodal: similar visual-language observations may be followed by different action chunks because human demonstrators act with different short-horizon intents, task phases, or recent context. Existing frame-conditioned VLA policies infer each chunk from the current observation and instruction alone, so under partial observability they may resample different intents across adjacent replanning steps, leading to inter-chunk conflict and unstable execution. We introd...

</details>

---

### [VGGT-$Ω$](https://arxiv.org/abs/2605.15195v1)

**Authors:** Jianyuan Wang, Minghao Chen, Shangzhan Zhang, Nikita Karaev, Johannes Schönberger et al. (10 authors)

**Published:** 2026-05-14 | **Categories:** cs.CV

**Links:** [arXiv](https://arxiv.org/abs/2605.15195v1) | [PDF](https://arxiv.org/pdf/2605.15195v1.pdf) | [Project Page](http://vggt-omega.github.io/)

<details>
<summary>Abstract</summary>

Recent feed-forward reconstruction models, such as VGGT, have proven competitive with traditional optimization-based reconstructors while also providing geometry-aware features useful for other tasks. Here, we show that the quality of these models scales predictably with model and data size. We do so by introducing VGGT-$Ω$, which substantially improves reconstruction accuracy, efficiency, and capabilities for both static and dynamic scenes. To enable training this model at an unprecedented scal...

</details>

---

## Other Recent Papers

### [Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction](https://arxiv.org/abs/2605.15157v1)

**Authors:** Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin et al. (8 authors)

**Published:** 2026-05-14 | **Categories:** cs.RO, cs.LG

**Links:** [arXiv](https://arxiv.org/abs/2605.15157v1) | [PDF](https://arxiv.org/pdf/2605.15157v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models are prone to compounding errors in dexterous manipulation, where high-dimensional action spaces and contact-rich dynamics amplify small policy deviations over long horizons. While Interactive Imitation Learning (IIL) can refine policies through human takeover data, applying it to high-degree-of-freedom (DoF) robotic hands remains challenging due to a command mismatch between human teleoperation and policy execution at the takeover moment, which causes abrupt r...

</details>

---

### [Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model](https://arxiv.org/abs/2605.14950v1)

**Authors:** Tao Lin, Yuxin Du, Jiting Liu, Nuobei Zhu, Yunhe Li et al. (17 authors)

**Published:** 2026-05-14 | **Categories:** cs.CV, cs.RO

**Links:** [arXiv](https://arxiv.org/abs/2605.14950v1) | [PDF](https://arxiv.org/pdf/2605.14950v1.pdf)

<details>
<summary>Abstract</summary>

Vision-Language-Action models have emerged as a promising paradigm for robotic manipulation by unifying perception, language grounding, and action generation. However, they often struggle in scenarios requiring precise spatial understanding, as current VLA models primarily rely on 2D visual representations that lack depth information and detailed spatial relationships. While recent approaches incorporate explicit 3D inputs such as depth maps or point clouds to address this issue, they often incr...

</details>

---
