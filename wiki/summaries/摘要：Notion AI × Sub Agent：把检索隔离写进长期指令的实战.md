---
title: 摘要：Notion AI × Sub Agent：把检索隔离写进长期指令的实战
type: summary
tags:
- 知识管理
- RAG/检索
- 笔记工具
- 多Agent协作
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: Agent, LLM, 自动化, Multi-Agent, skills
source_article_url: https://www.notion.so/f5953aef79544b9bb8611d3117804335
notion_url: https://www.notion.so/Tizer/60bbe87aabb14923937fca5fc3c05887
notion_id: 60bbe87a-abb1-4923-937f-ca5fc3c05887
---

## 一句话摘要

这篇材料把 NotebookLM 负责封闭语料检索、Claude 负责推理编排的分层范式，映射为 Notion AI 中由 sub agent 承担检索隔离、主线程只接收蒸馏结论的工作流设计。

## 关键洞察

- 贵模型不该反复重读大语料；把检索与推理解耦，才能同时控制成本、上下文污染和跨 session 复用问题。

- 在 Notion AI 里，`createAndRunThread` 提供了真正的子线程边界，能把检索、试错和工具调用隔离在主对话之外。

- 自建 Wiki Skill + sub agent 的组合，本质上等价于 NotebookLM + Claude：前者负责封闭知识召回，后者负责规划、判断与编排。

- 长期指令、Skill、Custom Agent 不是同一层抽象，分别对应约束、工具和角色三种封装粒度，适合不同成本—收益场景。

- 当规划层、检索层、执行层都被拆开后，Agent 系统更容易并行、替换后端、隔离失败，并保持主 context 的高密度。

## 提取的概念

- [检索/推理分层](concepts/检索-推理分层.md)

- [Sub agent 上下文隔离](concepts/Sub agent 上下文隔离.md)

- [蒸馏结论传递](concepts/蒸馏结论传递.md)

- [Agent 封装粒度](concepts/Agent 封装粒度.md)

- [规划/检索/执行三层隔离](concepts/规划-检索-执行三层隔离.md)

## 原始文章信息

- 作者：Tizer Luo × Notion AI

- 来源：X书签

- 发布时间：2026-04-20

- 链接：[原始对话](https://www.notion.so/)

## 个人评注

这套范式和 Tizer 当前的 Wiki Compiler、知识 Wiki、开发 Agent 分层非常契合。它不是单纯的省 token 技巧，而是在把“检索出来的原始噪音”限制在子线程里，让主线程只保留可执行判断、架构决策和下一步动作，从而让规划质量更稳定，也让后续把 Wiki、搜索、执行分别封装为独立模块变得更自然。
