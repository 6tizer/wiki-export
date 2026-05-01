---
title: Stanford Agentic Reviewer
type: entity
tags:
- 模型评测
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d31cf39f8b604a5eb599a82ad2e39c50
notion_id: d31cf39f-8b60-4a5e-b599-a82ad2e39c50
---

## 定义

Stanford Agentic Reviewer（SAR）是斯坦福大学开发的智能体论文评审系统，用于自动评估 AI 生成论文的质量。SAR 主要依赖最终生成的 PDF 论文进行打分。

## 关键要点

- 作为 Auto Research 领域的标准评测工具，被广泛用于比较不同自动化科研系统的输出质量

- 评分存在系统性偏差：倾向于对 negative results 给予高分（认为是「诚实表现」），导致评分虚高

- SAR 的分数与其 overall assessment（accept/reject 决策）有时不匹配

- 仅依赖 PDF 打分，无法检测代码实现与论文声明不一致的问题

- 更严格的同行交叉评审（PR）机制需要额外查看代码仓库和执行日志才能识别造假

## 来源引用

- [摘要：200刀打败18万美元FARS，我们离真正的Auto Research还有多远？](summaries/摘要：200刀打败18万美元FARS，我们离真正的Auto Research还有多远？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719869&idx=1&sn=286785641a7ed52f6a793ada026e99b7&chksm=97fd86517cd8ac029041769d3854be3aa40b9cfb029f9227e4c44dddc772f6182f320b544355#rd)）

## 关联概念

- [Auto Research](concepts/Auto Research.md)

- [FARS](entities/FARS.md)

- [Agentic Review 偏差](concepts/Agentic Review 偏差.md)
