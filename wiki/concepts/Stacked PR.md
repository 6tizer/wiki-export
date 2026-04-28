---
title: Stacked PR
type: concept
tags:
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/257edbb1bfc441779e10f2dd48c894f2
notion_id: 257edbb1-bfc4-4177-9e10-f2dd48c894f2
---

## 定义

Stacked PR（堆叠 PR / 层叠 PR）是一种将大型代码变更拆解为多个有序、有依赖关系的 Pull Request 的工作流。每个 PR 针对前一个 PR 的分支而非 main，形成依赖链，reviewer 可以独立审查每一层，合并时按顺序从底部开始依次合入。

## 关键要点

- **核心结构**：PR 链形成有序依赖，如 main → PR#1（数据模型）→ PR#2（业务逻辑）→ PR#3（API 接口）→ PR#4（测试）

- **聚焦 diff**：每个 PR 只展示本层相对于下一层的变更，降低审查复杂度

- **按层运行 CI**：每个 PR 针对其实际目标分支运行 CI

- GitHub 正通过 **gh-stack** 将 Stacked PR 作为原生特性引入（private preview 阶段）

- **工具支持**：Jujutsu 的提交链天然适配 Stacked PR；GitButler 通过 `but branch -a` 实现堆叠分支并自动级联 rebase

- 在 Monorepo 中尤为有价值：可将「修改共享 package」和「更新各消费方」拆成独立 PR 层

## 与 Agentic Coding 的关联

- Agent 往往一次完成大量工作（接口、测试、文档、依赖升级），Stacked PR 将巨型 PR 拆解为可审查的层叠单元

- 每层独立审查、独立合并，降低 agent 产出的审查门槛

## 来源引用

- [摘要：万字干货｜AI 时代的 Git 版本管理，你用对了吗？](summaries/摘要：万字干货｜AI 时代的 Git 版本管理，你用对了吗？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxMTY4NTAyNQ%3D%3D&mid=2247510348&idx=1&sn=0eaed4bb608369011819fade6a28a188&chksm=c0583d219f4fda092c28dae7651cc941f4e0547dd5dedbffea47553e1c5866db75435efd9adc#rd)）
