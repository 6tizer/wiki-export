---
title: Ralph Wiggum 方法
type: concept
tags:
- Harness 工程
- 代码生成
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3e1b2b551a3c4636bfece56ee9d353e0
notion_id: 3e1b2b55-1a3c-4636-bfec-e56ee9d353e0
---

## 定义

Ralph Wiggum 方法是 2025 年底流行的一种 AI 编程循环模式，核心做法是 `while true; do cat PROMPT.md | claude; done`——将规格写入 PROMPT 文件，让单个 Agent 在无限循环中自主执行任务。

## 关键要点

- 解决了人类需要逐轮 chat 交互的问题，实现 Agent 自主循环

- 本质是单 Agent 自我循环：自己写、自己测、自己改，缺少外部审核视角

- 质量完全依赖测试 backpressure 和 prompt 质量

- 是 autoresearch 方法论的前身之一，后者在此基础上增加了量化 metric 和多 Agent 交叉审核

## 来源引用

- [摘要：我把 Karpathy 的 AutoResearch 搬到了软件开发领域，效果炸了](summaries/摘要：我把 Karpathy 的 AutoResearch 搬到了软件开发领域，效果炸了.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ%3D%3D&mid=2247606664&idx=1&sn=34e95bd76d66935c85b61ed791983041&chksm=c14a0674bcce5652baa86c6abc2cd4e4c262f81d5315768d929af6f36022a87c42917c19224f#rd)）

## 关联概念

- [autoresearch](entities/autoresearch.md)

- [多 Agent 交叉审核](concepts/多 Agent 交叉审核.md)

- [Keep-or-revert loop](concepts/Keep-or-revert loop.md)
