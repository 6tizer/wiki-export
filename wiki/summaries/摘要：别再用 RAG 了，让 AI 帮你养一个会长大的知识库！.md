---
title: 摘要：别再用 RAG 了，让 AI 帮你养一个会长大的知识库！
type: summary
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881e69504e1abf24febf0
notion_url: https://www.notion.so/Tizer/5771fc84609b4113bc435c8ee5427d07
notion_id: 5771fc84-609b-4113-bc43-5c8ee5427d07
---

## 一句话摘要

这篇文章主张用 LLM 持续维护一个会随资料摄入而增量生长的 Wiki，把知识管理从“查询时临时检索”升级为“摄入时预先编译”。

## 关键洞察

- RAG 的核心短板不是不能回答问题，而是**不会积累**，复杂问题会反复从碎片里重新拼答案。

- Karpathy 提出的思路是让 LLM 在每次新增资料时直接更新 Wiki，把摘要、概念、实体、索引和交叉引用提前整理好。

- 这套方法采用 **raw / wiki / schema** 三层分离，让原始资料保真、编译产物可持续维护、规则文件可持续迭代。

- 核心操作不只是摄入和查询，还包括定期的 lint 审查，用来处理矛盾、过期信息、孤岛页面和缺失条目。

- 这类系统更像“养一棵树”，前期需要配置 Agent 与规范，但长期价值会随着资料沉淀不断复利。

## 提取的概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [编译式知识库](concepts/编译式知识库.md)

- [三层知识架构](concepts/三层知识架构.md)

- [Ingest 摄入流程](concepts/Ingest 摄入流程.md)

- [Wiki 健康检查](concepts/Wiki 健康检查.md)

- [Idea File](concepts/Idea File.md)

## 原始文章信息

- 作者：@sitinme

- 来源：X书签

- 发布时间：2026-04-14

- 原文链接：[https://x.com/sitinme/status/2043865262982869105](https://x.com/sitinme/status/2043865262982869105)

- 源文章页面：Karpathy 的 LLM Wiki：用 AI 养一个会自我生长的知识库

## 个人评注

这篇文章和 Tizer 当前的内容编译链路高度一致。原始文章库相当于 raw，知识 Wiki 相当于 wiki，而 Agent 指令页本身就是 schema。它提醒我们，真正有复利的不是“把文章喂给模型问一次”，而是把每次摄入都沉淀成结构化条目，再通过 concept、summary 和后续 lint 形成持续可维护的知识资产。
