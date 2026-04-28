---
title: Atomic Commit
type: concept
tags:
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c115417956a7484c89fa142c4d17c22f
notion_id: c1154179-56a7-484c-89fa-142c4d17c22f
---

## 定义

Atomic Commit（原子提交）是一种版本控制原则：每个 commit 只表达一个可解释、可回滚、可验证的语义变化，且在该 commit 节点上代码可以编译、测试可以通过。

## 关键要点

- **核心定义**：一个 commit = 一个独立的逻辑关注点，不是「一行一提交」

- **在 Agentic Coding 中更关键**：agent 执行长任务时往往将多个不相关修改混入同一提交，atomic commit 是对抗熵增的直接手段

- **可回滚性**：保持每个 commit 可独立回滚，降低 agent 引入问题时的修复成本

- **审查效率**：reviewer 可按 commit 逐步理解变更，而非面对巨型 diff

- **git bisect 精度**：二分搜索的定位精度直接取决于 commit 粒度

- **Monorepo 中的边界**：修改共享 library 同时必须同步更新消费方，只要逻辑上不可分割就可放在同一 commit

- **与 Checkpoint Commit 互补**：checkpoint 记录进度，最终通过 rebase 整理为 atomic commit

## 来源引用

- [摘要：万字干货｜AI 时代的 Git 版本管理，你用对了吗？](summaries/摘要：万字干货｜AI 时代的 Git 版本管理，你用对了吗？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxMTY4NTAyNQ%3D%3D&mid=2247510348&idx=1&sn=0eaed4bb608369011819fade6a28a188&chksm=c0583d219f4fda092c28dae7651cc941f4e0547dd5dedbffea47553e1c5866db75435efd9adc#rd)）
