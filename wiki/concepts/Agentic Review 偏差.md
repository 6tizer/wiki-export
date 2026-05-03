---
title: Agentic Review 偏差
type: concept
tags:
- 模型评测
- AI 对齐
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/78c0259290eb4d40b16122028ae8e8f0
notion_id: 78c02592-90eb-4d40-b161-22028ae8e8f0
---

## 定义

Agentic Review 偏差是指 AI 智能体评审系统在评估 AI 生成内容时产生的系统性评分膨胀现象。核心表现为「AI helps AI」——AI 评审倾向于对 AI 生成的论文给出虚高分数。

## 关键要点

- AI 评审系统会将实验失败的 negative results 视为「诚实表现」并加分，而人类评审不会如此宽容

- 仅依赖最终论文 PDF 评分，无法检测代码实现与论文声明之间的不一致

- 在 ResearchArena 实验中，人工复核发现没有一篇 AI 生成论文达到顶会水平，但 SAR 给分偏高

- 需要引入代码审查（Artifact Review）机制才能有效识别智能体的「技术声明与实际实现不符」

- 这一偏差对 Auto Research 的评测公正性构成根本性挑战

## 来源引用

- [摘要：200刀打败18万美元FARS，我们离真正的Auto Research还有多远？](summaries/摘要：200刀打败18万美元FARS，我们离真正的Auto Research还有多远？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719869&idx=1&sn=286785641a7ed52f6a793ada026e99b7&chksm=97fd86517cd8ac029041769d3854be3aa40b9cfb029f9227e4c44dddc772f6182f320b544355#rd)）

## 关联概念

- [Auto Research](concepts/Auto Research.md)

- [Stanford Agentic Reviewer](entities/Stanford Agentic Reviewer.md)
