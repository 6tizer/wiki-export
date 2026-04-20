---
title: Agent 持续学习三层框架
type: concept
tags:
- Agent 编排
- 记忆系统
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/dee008b28f7c41bd8b875726df6538bc
notion_id: dee008b2-8f7c-41bd-8b87-5726df6538bc
---

## 定义

Agent 持续学习三层框架是 Harrison Chase 提出的分析框架，用来把 Agent 的自我进化拆成 **Model、Harness、Context** 三层，区分不同的学习对象、优化成本与落地路径。

## 关键要点

- **Model 层**关注权重更新，成本最高，通常依赖训练数据、评测闭环与模型发布机制

- **Harness 层**关注执行机制，包括提示、工具暴露、调用循环、回放与评测

- **Context 层**关注可持久化上下文，包括记忆、技能、用户偏好与团队规则

- 三层不该被当成一个笼统的“持续学习”开关，而应分别设计更新频率、评估方式和回滚机制

- 对大多数产品团队，更现实的推进顺序通常是 **Context → Harness → Model**

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Meta-Harness](concepts/Meta-Harness.md)

- [OpenClaw](entities/OpenClaw.md)

- [Claude Code](entities/Claude Code.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523832&idx=1&sn=8a7013894ddc0668c0f1c9f935599450&chksm=c1b17f5bd2d0ca49ee848d1dc13c14fb122c8f551ba00b307b566dfa7edc4c20a52573051f79#rd)｜《字节最火的开源Agent项目，如何思考Agent的自我进化？》｜来源文章：字节最火的开源Agent项目，如何思考Agent的自我进化？

- [摘要：Preparing for Radical Transformation](summaries/摘要：Preparing for Radical Transformation.md)（[原文](https://x.com/leonardtang_/status/2045179350547612043)）
