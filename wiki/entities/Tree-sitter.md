---
title: Tree-sitter
type: entity
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/36400a424ac243109e0c4695df0b2cc3
notion_id: 36400a42-4ac2-4310-9e0c-4695df0b2cc3
---

## 定义

Tree-sitter 是一个增量解析器生成框架，常用于把源代码解析为抽象语法树（AST）。在 Agent 工具链里，它适合承担结构化代码理解层，为函数、类、导入关系等建立稳定语义索引。

## 关键要点

- **技术角色**：把原始代码文本转成结构化 AST，是代码知识图谱和影响分析的底层解析基础

- **适配能力**：支持多语言语法，适合跨语言仓库与 Notebook 场景

- **工程优势**：天然适配增量更新，不必在每次变更后重做全量解析

- **在本文语境中的作用**：作为 code-review-graph 的核心解析引擎，用于支撑上下文裁剪和变更追踪

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484353&idx=1&sn=f2ad30ea21fee327daac93a9143a76fb&chksm=f539ae6800aa8066504c6b4ed683e14b501d516a93882ddd92b4c501a2537281c3b85d7d3c8f#rd)｜《code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !》｜源页面：code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484493&idx=1&sn=a5ee52c8f58f8da657f54f32976bf1dd&chksm=f56db0775eab013c92bc978ab53e6fa4ac8d49e227f35e3313e988b7b0735bcc7310ae8ce2f6#rd)｜《codeflow:  github上最被低估的黑科技，仅用一个html文件，浏览器直接"透视"整个项目架构，自动计算代码变更的爆炸半径！》｜源页面：codeflow:  github上最被低估的黑科技，仅用一个html文件，浏览器直接"透视"整个项目架构，自动计算代码变更的爆炸半径！

- [摘要：Graphify-让Karpathy方法构建的知识库实现71.5倍效率提升](summaries/摘要：Graphify-让Karpathy方法构建的知识库实现71.5倍效率提升.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzcwMjIwMDk2Mg%3D%3D&mid=2247483836&idx=1&sn=87efe38320d976ed8850cded7a9919e8&chksm=f5738db7a5afe6ffd094c3453e8877b6266c1beda961858dc1d414bc80f787a3f74103f66e4c#rd)）

- [摘要：sentrux：一个开源的代码架构传感器，让大模型守住代码底线！](summaries/摘要：sentrux：一个开源的代码架构传感器，让大模型守住代码底线！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484673&idx=1&sn=9a52bf97b7c11eef0414da5f957caba2&chksm=f544a6ba6d1eae6bf4261adba920e882c604a63f51e87a21903d6ed42087d1a09eb0224e9d2d#rd)）

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Graphify](entities/Graphify.md)

- [AST+LLM 双阶段提取](concepts/AST+LLM 双阶段提取.md)
