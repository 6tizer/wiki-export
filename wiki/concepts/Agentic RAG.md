---
title: Agentic RAG
type: concept
tags:
- RAG/检索
- 多Agent协作
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0cb7a5f684a04c459e3b2e4b743e1c3a
notion_id: 0cb7a5f6-84a0-4c45-9e3b-2e4b743e1c3a
---

## 定义

Agentic RAG 是在传统检索增强生成流程中引入 Agent 规划、工具调用与循环决策能力的架构模式，使系统能够根据任务动态选择检索、推理与执行路径。

## 关键要点

- 在 RAG 的基础上增加 Planner、工具使用与多步循环，而不是一次性检索后直接回答

- 更适合复杂问题、开放式搜索和需要外部操作的任务场景

- 常与 Tool Calling、记忆系统、搜索代理等能力组合出现

- 在可视化表达上通常需要显式展示检索链路、Agent 决策层与工具层

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484388&idx=1&sn=d2f897dce455cb4abdcaa39f7f91a864&chksm=f5f28e3e3d180a1e33285f77fa24c32d02bd1a720aa00b7f6b5850934693a9f64e247fac389a#rd)｜《fireworks-tech-graph：用自然语言生成工业级架构图，Claude Code 绘图神器！》｜源文章：fireworks-tech-graph：用自然语言生成工业级架构图，Claude Code 绘图神器！

## 关联概念

- [Tool Calling](concepts/Tool Calling.md)

- [Mem0](entities/Mem0.md)

- [Multi-Agent 群聊](concepts/Multi-Agent 群聊.md)
