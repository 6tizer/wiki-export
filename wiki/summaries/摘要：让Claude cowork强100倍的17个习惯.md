---
title: 摘要：让Claude cowork强100倍的17个习惯
type: summary
tags:
- 上下文管理
- 多Agent协作
- 内容自动化
status: 已审核
confidence: medium
last_compiled: '2026-04-27'
source_tags: LLM
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b992293b532c4f0e9c3cce760bbd526e
notion_id: b992293b-532c-4f0e-9c3c-ce760bbd526e
---

## 一句话摘要

总结 17 个提升 Claude Cowork 效率的实践习惯，核心思路是通过分层上下文管理、外化信息到文件、并行子代理、定时任务等方式，把 Cowork 当作「强力员工」来系统性管理。

## 关键洞察

- [**MANIFEST.md**](http://manifest.md/)** 三层分级**：Tier 1 核心必读、Tier 2 按需加载、Tier 3 归档忽略——严格控制上下文范围比塞满百万 token 窗口更有效

- **三个持久化上下文文件**：[about-me.md](http://about-me.md/)（个人信息）、[brand-voice.md](http://brand-voice.md/)（品牌调性）、[working-style.md](http://working-style.md/)（工作风格），解决跨会话记忆缺失

- **Subagents 并行是隐藏功能**：4 个子代理同时评估供应商，40 分钟→10 分钟，是 Cowork 最被低估的能力

- **外化一切到文件**：Cowork 无跨会话记忆，偏好→上下文文件，流程→Skill，决策→日志

- **schedule + connectors 组合**：连接 Gmail/Slack/Notion 等 50+ 集成后，定时任务变成真正的自动化流水线

## 提取的概念

- MANIFEST 分层管理

- Subagents 并行

- Claude Cowork Skills（已有概念，追加引用）

## 原始文章信息

- **作者**：向量空性

- **来源**：微信公众号

- **发布时间**：2026-03-03

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NjgzMTE5MQ%3D%3D&mid=2247483883&idx=1&sn=0feb4de317a4be3117675449a20558aa)

## 个人评注

MANIFEST 分层管理和外化信息到文件的思路，与 Tizer 的知识 Wiki 结构化管理理念高度一致。Subagents 并行模式可应用于 OpenClaw 的多 Agent 编排场景。schedule + connectors 的自动化组合正是 HITL 工作流的核心模式。
