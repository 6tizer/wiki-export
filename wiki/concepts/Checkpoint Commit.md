---
title: Checkpoint Commit
type: concept
tags:
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c186ae7e51084012a030aa5796609fbc
notion_id: c186ae7e-5108-4012-a030-aa5796609fbc
---

## 定义

Checkpoint Commit（检查点提交）是一种针对长时间运行的 Agent 任务的提交策略：要求 agent 在关键节点进行阶段性提交（以 `[WIP]` 前缀标记），而不是等任务全部完成再一次性提交。最终完成后通过 interactive rebase 整理历史。

## 关键要点

- **典型检查点**：完成数据模型/接口定义、核心逻辑实现、测试编写、文档更新等关键阶段时各做一次提交

- **恢复能力**：任务中断时可从最近的 checkpoint 恢复，无需从头开始

- **审查切分**：checkpoint commit 天然成为 code review 的切分点，reviewer 可分段审查

- **调试支持**：便于 `git bisect` 定位引入问题的具体阶段

- **与 Atomic Commit 的关系**：Checkpoint Commit 关注**进度记录**（阶段性存档），Atomic Commit 关注**语义边界**（一个 commit 做一件事）；两者互补——checkpoint 在任务中保存现场，最终通过 rebase 整理为 atomic commit

## 来源引用

- [摘要：万字干货｜AI 时代的 Git 版本管理，你用对了吗？](summaries/摘要：万字干货｜AI 时代的 Git 版本管理，你用对了吗？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxMTY4NTAyNQ%3D%3D&mid=2247510348&idx=1&sn=0eaed4bb608369011819fade6a28a188&chksm=c0583d219f4fda092c28dae7651cc941f4e0547dd5dedbffea47553e1c5866db75435efd9adc#rd)）
