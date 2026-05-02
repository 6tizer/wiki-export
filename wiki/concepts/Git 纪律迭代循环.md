---
title: Git 纪律迭代循环
type: concept
tags:
- 代码生成
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a774463a509e464eacaa1defd88d4787
notion_id: a774463a-509e-464e-acaa-1defd88d4787
---

## 定义

Git 纪律迭代循环（Git-disciplined Iteration Loop）是一种在自动化代码改进过程中，利用 Git 版本控制保障每次迭代安全性的工程模式。每次 Agent 迭代成功则创建独立 commit，失败则用 `git reset --hard` 回滚到上次已知良好状态，确保工作分支始终保持可用。

## 关键要点

- **成功即提交**：每次成功的改动变成独立 Git commit，支持单独 cherry-pick 或回滚

- **失败即回滚**：失败迭代通过 `git reset --hard` 恢复，不留残留

- **连续失败熔断**：设定阈值（如连续 3 次失败）自动中止，防止无效循环

- **可审计性**：所有工作过程通过 commit history 和日志文件（如 [notes.md](http://notes.md/)）完整记录

- 这一模式使 Agent 可以长时间无人值守运行，同时保持代码库的完整性

## 关联概念

- [gnhf](entities/gnhf.md)

- [Agent 隔夜编排](concepts/Agent 隔夜编排.md)

- [autoresearch](entities/autoresearch.md)

## 来源引用

- [摘要：1.3K Star！让 Coding Agent 在你睡觉时持续工作的神奇开源工具！](summaries/摘要：1.3K Star！让 Coding Agent 在你睡觉时持续工作的神奇开源工具！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247506012&idx=1&sn=59df2a6364a3fa6f7b5c6fd4fc260317&chksm=c19e01c3a46ee4fa7c969e3448080d0d1b886bf7118572e4e3e26f60022a32a35d7c8ab3b2da#rd)）
