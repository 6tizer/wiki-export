---
title: SkVM
type: entity
tags:
- Harness 工程
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/485191971c9a4595b7aa5681c8f9ec02
notion_id: 48519197-1c9a-4595-b7aa-5681c8f9ec02
---

## 定义

SkVM 是一个面向 Skill 的编译与运行时系统，它把 Skill 视为自然语言程序，目标是在异构 LLM、不同 Agent Harness 与不同宿主环境之间，实现更稳定、更可移植的执行。

## 关键要点

- 它把 Skill、LLM 与 Harness 重新抽象为“程序、处理器、运行环境”的关系。

- 安装阶段会做 AOT 编译、环境绑定与并发提取。

- 运行阶段会做 JIT 优化、代码固化与资源感知调度。

- 它的核心价值不是把提示词写得更长，而是把 Skill 变成可编译、可复用、可回滚的系统组件。

## 来源引用

- [摘要：SkVM：优化你的Skills能够跨模型、跨Harness、跨环境稳定运行 ｜SJTU最新](summaries/摘要：SkVM：优化你的Skills能够跨模型、跨Harness、跨环境稳定运行 ｜SJTU最新.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508119&idx=1&sn=8576b881967cee0b33dc2c424c9853a5&chksm=ce7a42ad8a773a9cdc3297389c1915b62ee8ee06d86ae09cbf47c11c9141230f4f6a7f8916f7#rd)）
