---
title: AST 感知分块
type: concept
tags:
- RAG/检索
- 上下文管理
- 知识管理
status: 审核中
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e6b3555963784488934fb8215767cdd4
notion_id: e6b35559-6378-4488-934f-b8215767cdd4
---

## 定义

AST 感知分块是指基于抽象语法树与代码结构边界来切分文档或代码片段，把函数、类、import 等完整语义单元作为检索块，而不是按固定字数或 token 粗暴截断。

## 关键要点

- **保留结构完整性**：尽量让一个函数、类或模块说明以完整片段进入检索结果，避免中途截断。

- **提升检索质量**：比起固定长度切块，更适合代码搜索、语义召回和 LLM 重排。

- **减少上下文噪音**：返回给 Agent 的内容更集中，能降低无关上下文混入。

- **适合 Coding Agent 场景**：尤其适用于本地代码库索引、RAG 检索和上下文注入。

## 来源引用

- [摘要：AI Agent的"海姆达尔计划"：让大模型看见代码的双眼](summaries/摘要：AI Agent的海姆达尔计划：让大模型看见代码的双眼.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI4MTc1Njg0MA%3D%3D&mid=2247486027&idx=1&sn=5044a57bef3d70a570db55273e382056&chksm=ea4fee508bee3d6d05240803fd1567e72c1dcc6d4a527b35a60dbca6b604e8a90021341f6c90#rd)）

## 关联概念

- [GitNexus](entities/GitNexus.md)

- [代码知识图谱](concepts/代码知识图谱.md)

- [QMD](entities/QMD.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)
