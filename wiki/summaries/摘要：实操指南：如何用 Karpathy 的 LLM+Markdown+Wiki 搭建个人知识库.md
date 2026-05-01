---
title: 摘要：实操指南：如何用 Karpathy 的 LLM+Markdown+Wiki 搭建个人知识库
type: summary
tags:
- 知识管理
- RAG/检索
- 笔记工具
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: LLM, 自动化, Agent, wiki, Karpathy
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4d5e75b143854decb76fce59dcdae7c9
notion_id: 4d5e75b1-4385-4dec-b76f-ce59dcdae7c9
---

**一句话摘要**

系统介绍 Karpathy 知识库方法论的三层架构（原始资料层/LLM编译层/宪法规则层）和四个关键操作，推荐 Obsidian 和 CacheZero 作为工具组合。

**关键洞察**

- **三层分离架构**：

  1. 原始资料层（raw/）：未处理的原始内容

  1. LLM 编译产物层（wiki/）：AI 自动整理的结构化知识

  1. 宪法文件层（system/）：定义规则和约束，类似 agent instructions

- **四个关键操作**：资料灌入 → 提问检索 → 输出归档 → 健康检查

- 核心转变：从"人整理"到"LLM 编译"，知识库变成自我进化的系统

- 推荐工具：Obsidian（笔记管理）+ CacheZero（LLM缓存优化）

- 与本 Wiki Compiler Agent 的设计逻辑几乎完全一致

**提取的概念**

- LLM+Markdown+Wiki知识库（追加最完整的实操引用）

**原始文章信息**

- 作者：Alphana和大船的AI工作区

- 来源：微信

- 发布时间：2026-04-10

- 链接：[https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw==&mid=2247484010](https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw%3D%3D&mid=2247484010)

- 标签来源：知识管理、LLM、RAG/Memory、教程/实战、Agent

**个人评注**

**最高优先级参考文章！** 这篇文章描述的正是 Tizer 正在实现的工作流——本 Wiki 即是 LLM 编译产物层的实现。三层架构和宪法文件层的概念对优化 Wiki Compiler Agent 的 instructions 有直接指导价值。
