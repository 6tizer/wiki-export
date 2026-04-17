---
title: 摘要：Google AI 代理白皮书：读完这篇，你就搞懂了 LLM Agent 的底层逻辑
type: summary
tags:
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/e699a0758ede4f2ca249d75f149a21b0
notion_id: e699a075-8ede-4f2c-a249-d75f149a21b0
---

**一句话摘要**：Google 白皮书将 AI 代理定义为"能用工具、有记忆、会规划的 LLM 系统"，三类工具（扩展/函数/数据存储）+ 四类记忆（上下文/外部数据库/缓存/模型参数）构成代理能力的完整框架。

## 关键洞察

- 代理 vs 普通 LLM：增加感知（多模态输入）、规划（多步骤任务分解）、行动（工具调用改变外部状态）三个关键能力

- 工具三分类：扩展（预定义 API）、函数（开发者自定义逻辑）、数据存储（RAG 向量数据库）

- 记忆四层次：上下文窗口（工作记忆）/ 外部数据库（长期知识）/ 缓存（加速检索）/ 模型参数（直觉/本能）

- Google ADK（Agent Development Kit）已获 18,700+ Stars，与 Gemini/GCP 原生集成

- 配合 Google《5 天 AI 代理强化课》学习效果更佳

## 提取的概念

- **ReAct Agent** — 代理的感知-规划-工具-记忆循环在 LangChain 中的实现

- **RAG** — 白皮书中作为数据存储工具的向量数据库检索技术

## 原始文章信息

- **作者**：AI Will（@FinanceYF5）转介，原作者 @marcb_xyz；白皮书作者：Julia Wiesinger/Patrick Marlow/Vladimir Vuskovic（Google）

- **来源**：X书签

- **发布时间**：2025-01-05

- **链接**：[https://www.kaggle.com/whitepaper-agents](https://www.kaggle.com/whitepaper-agents)

## 个人评注

Google 白皮书是目前最系统的 AI 代理入门材料，工具分类框架（扩展/函数/数据存储）可直接指导 OpenClaw 的工具接入设计。四类记忆层次尤其値得参考，对内容管道的上下文管理有直接指导意义。
