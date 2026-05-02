---
title: Agent 隔夜编排
type: concept
tags:
- 代码生成
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/05c2dfc4de3c47e6a74d6c7e4ca42379
notion_id: 05c2dfc4-de3c-47e6-a74d-6c7e4ca42379
---

## 定义

Agent 隔夜编排（Overnight Agent Orchestration）是一种让 Coding Agent 在开发者休息期间自主持续运行的工程模式。用户在睡前设定高层目标（如「降低代码复杂度」「补充测试」），编排器自动将目标拆解为多次迭代，每次迭代调用 Agent 执行并根据结果决定提交或回滚，次日开发者审核成果。

## 关键要点

- 核心假设：机械性、重复性的编码任务适合无人值守自动执行，核心业务逻辑仍需人工审核

- 依赖严格的版本控制纪律（如 Git commit/rollback）确保长时间运行的安全性

- 需要容错机制：连续失败自动中止、指数退避重试、运行上限（迭代次数/token 用量）

- 跨迭代记忆（如共享笔记文件）帮助后续迭代理解前序上下文

- 代表工具：gnhf、ralph、autoresearch

## 与相关概念的区别

- 与一般的 CI/CD 不同：隔夜编排的目标是开放式的代码改进，而非固定的构建/测试流水线

- 与交互式 Coding Agent 不同：强调无人值守、长时间自主运行

## 关联概念

- [gnhf](entities/gnhf.md)

- [Git 纪律迭代循环](concepts/Git 纪律迭代循环.md)

- [autoresearch](entities/autoresearch.md)

## 来源引用

- [摘要：1.3K Star！让 Coding Agent 在你睡觉时持续工作的神奇开源工具！](summaries/摘要：1.3K Star！让 Coding Agent 在你睡觉时持续工作的神奇开源工具！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247506012&idx=1&sn=59df2a6364a3fa6f7b5c6fd4fc260317&chksm=c19e01c3a46ee4fa7c969e3448080d0d1b886bf7118572e4e3e26f60022a32a35d7c8ab3b2da#rd)）
