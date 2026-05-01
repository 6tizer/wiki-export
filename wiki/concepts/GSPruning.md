---
title: GSPruning
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/59914c3a64b34f4fa0f174cb931c2415
notion_id: 59914c3a-64b3-4f4f-a0f1-74cb931c2415
---

> **🪄** **定义**：GSPruning 是 Mano-P 在端侧优化中使用的视觉 Token 剪枝技术，通过保留全局空间锚点与关键语义异常值，在压缩视觉 Token 数量的同时尽量保持任务成功率。

### 关键要点

- 面向高分辨率 GUI 截图中的冗余视觉 Token，解决端侧推理算力与内存受限问题。

- 文章称其可将视觉 Token 保留率压缩至 12.57%，并带来 2 到 3 倍吞吐提升。

- 是 Mano-P 能在 Mac 等设备上落地的重要工程优化手段之一。

### 来源引用

- 《全球第一，13个SOTA！我们找到了龙虾界掌管GUI的神》｜作者：机器之心｜发布：2026-04-13T11:58:00.000+08:00｜原文：[文章链接](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651027314&idx=1&sn=5f962ab9416c2eee0c4769a51057ced7&chksm=85b9064525b8127699bc59956dff0aba0eaabb800d3001d9595f29adf5055370ff3d7259f0d8#rd)｜源页面：全球第一，13个SOTA！我们找到了龙虾界掌管GUI的神

### 关联概念

- Mano-P

- GUI-VLA

- Mano-Action 双向自增强学习框架
