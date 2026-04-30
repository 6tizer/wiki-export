---
title: 多 Agent 交叉审核
type: concept
tags:
- 多Agent协作
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4a5720a0ea0f461dae3d14f73eab7356
notion_id: 4a5720a0-ea0f-461d-ae3d-14f73eab7356
---

## 定义

多 Agent 交叉审核是一种软件质量保证模式：让两个或多个不同的 AI Agent（如 Codex 与 Claude）轮流担任实现者和审核者——A 写完 B 审，B 写完 A 审。利用不同模型各自的盲区和强项互补，比单 Agent 自审能发现更多问题。

## 关键要点

- 核心思想：不同模型有不同的盲区，交叉视角能发现单 Agent 发现不了的缺陷

- 与单 Agent 自审（如 Ralph Wiggum 方法）的本质区别在于引入了外部审核视角

- 审核反馈直接注入下一轮 Agent 的提示词，形成「反馈驱动迭代」而非盲循环

- 实践证明双 Agent 交叉审核的代码质量远优于单 Agent 模式

## 来源引用

- [摘要：我把 Karpathy 的 AutoResearch 搬到了软件开发领域，效果炸了](summaries/摘要：我把 Karpathy 的 AutoResearch 搬到了软件开发领域，效果炸了.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ%3D%3D&mid=2247606664&idx=1&sn=34e95bd76d66935c85b61ed791983041&chksm=c14a0674bcce5652baa86c6abc2cd4e4c262f81d5315768d929af6f36022a87c42917c19224f#rd)）

## 关联概念

- [autoresearch](entities/autoresearch.md)

- [acpx](entities/acpx.md)

- [Ralph Wiggum 方法](concepts/Ralph Wiggum 方法.md)

- [program.md](concepts/program.md.md)

- 对抗式评审
