---
title: 摘要：实操指南：如何用 Karpathy 的 LLM + Markdown + Wiki 搭建个人知识库
type: summary
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: 知识管理, LLM, RAG/Memory, 教程/实战, Agent
source_article_url: ''
notion_url: https://www.notion.so/2e2506b1c37940539a1e8c0264c559a2
notion_id: 2e2506b1-c379-4053-9a1e-8c0264c559a2
---

**一句话摘要**

Karpathy的三层分离架构（原始资料层+LLM编译产物层+完法定义层）实现了从「人整理」到「LLM编译」的知识库升级，推荐工具Obsidian和CacheZero。

**关键洞察**

- **三层分离架构**：原始资料层（文章/笔记）、LLM编译产物层（Wiki/摘要）、完法层（规则定义如何编译）

- **四个关键操作**：资料灌入、提问检索、输出归档、健康检查（确保知识库完整性）

- 推荐工具：Obsidian（知识库管理）和CacheZero（快速索引）

- 局限：平台与工具需要配套设计，不是拿来就能用

- 实践延伸：这个Wiki Compiler Agent本身就是该架构的Notion实现

**提取的概念**

- LLM+Markdown+Wiki知识库工作流

- 知识库健康检查

- CacheZero

**原始文章信息**

- 作者：Alphana和大船的AI工作区

- 来源：微信

- 链接：[https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw==&mid=2247484010](https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw%3D%3D&mid=2247484010)

**个人评注**

这篇文章直接描述了Tizer正在做的事情。其中「健康检查」环节尤为关键：定期检查知识库的完整性、一致性和陈旧度，是保证知识库长期可用性的关键。
