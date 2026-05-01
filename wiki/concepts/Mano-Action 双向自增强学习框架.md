---
title: Mano-Action 双向自增强学习框架
type: concept
tags:
- 浏览器自动化
- 训练/微调
- 推理优化
status: 审核中
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/48fee8bc6443476585e683874c0bf371
notion_id: 48fee8bc-6443-4765-85e6-83874c0bf371
---

> **⚙️** **定义**：Mano-Action 双向自增强学习框架是 Mano-P 项目的核心训练方法，通过 Text ↔ Action 循环一致性学习，同时训练“自然语言到动作”和“动作到自然语言”两个方向。

### 关键要点

- 其目标是让模型不仅会执行 GUI 操作，也能反向理解动作背后的界面语义。

- 训练流程结合 SFT、离线强化学习与在线强化学习，形成递进式能力增强。

- 配合“思考 - 行动 - 验证”循环推理机制，提升 GUI 任务中的鲁棒性与纠错能力。

### 来源引用

- 《全球第一，13个SOTA！我们找到了龙虾界掌管GUI的神》｜作者：机器之心｜发布：2026-04-13T11:58:00.000+08:00｜原文：[文章链接](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651027314&idx=1&sn=5f962ab9416c2eee0c4769a51057ced7&chksm=85b9064525b8127699bc59956dff0aba0eaabb800d3001d9595f29adf5055370ff3d7259f0d8#rd)｜源页面：全球第一，13个SOTA！我们找到了龙虾界掌管GUI的神

### 关联概念

- GUI-VLA

- GSPruning

- Personalized AI
