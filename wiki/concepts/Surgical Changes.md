---
title: Surgical Changes
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/015077c5327347468c933745164f4ba1
notion_id: 015077c5-3273-4746-8c93-3745164f4ba1
---

## 定义

**Surgical Changes** 是一条 AI 编程改动准则，强调只修改与当前任务直接相关的代码，并仅清理由本次改动引入的副作用，避免顺手重构无关部分。

## 关键要点

- 每一处改动都应能直接追溯到用户请求

- 不顺手优化旁边的代码、注释或格式

- 不主动重构没有问题的既有逻辑

- 只清理由本次改动产生的冗余 import、变量或函数

## 关联概念

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [andrej-karpathy-skills](entities/andrej-karpathy-skills.md)

- [Think Before Coding](concepts/Think Before Coding.md)

- [Simplicity First](concepts/Simplicity First.md)

- [Goal-Driven Execution](concepts/Goal-Driven Execution.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzU3NTg5MjU1Mw%3D%3D&mid=2247496984&idx=1&sn=98f3a18047c1908f1b961052640e85a9&chksm=fc1c6bb03b47cbb0ba7d773e7d7e2f214a2492c4f081e9d9750d237912643aabf4e8b6628c58#rd)｜《一个 [CLAUDE.md](http://claude.md/) 文件竟然拿下 1.7 万 star，它到底写了什么》｜来源条目：[摘要：一个 CLAUDE.md 文件竟然拿下 1.7 万 star，它到底写了什么](summaries/摘要：一个 CLAUDE.md 文件竟然拿下 1.7 万 star，它到底写了什么.md)

- [原文链接](https://x.com/axiaisacat/status/2044260023161831620)｜《Looking for a managed agents platform?》｜来源条目：[摘要：Looking for a managed agents platform?](summaries/摘要：Looking for a managed agents platform.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI0ODk2NDIyMQ%3D%3D&mid=2247502836&idx=1&sn=bc1037b3490abbe4c22277672f9f0191&chksm=e86fcdd39fd3d2961bc8025efd7d093f04b7608ae7887433e37539f88532a95a6bfee7812824#rd)｜《就一个 skills，凭啥 4w Star？》｜来源条目：[摘要：就一个 skills，凭啥 4w Star？](summaries/摘要：就一个 skills，凭啥 4w Star？.md)
