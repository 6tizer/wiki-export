---
title: 摘要：用 Claude Code 调度 Codex 当 SubAgent：省 Token 的多 Agent 编排实践
type: summary
tags:
- 多Agent协作
- 代码生成
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: Agent, LLM, 自动化
source_article_url: https://www.notion.so/336701074b68817fb69be2c25a162cc9
notion_url: https://www.notion.so/Tizer/216bfd5fbb5a4acaaece1856730b4926
notion_id: 216bfd5f-bb5a-4aca-aece-1856730b4926
---

## 一句话摘要

这篇实践展示了一个朴素但有效的多 Agent 编排方法：让 Claude Code 负责规划与调度，把具体编码任务分发给 Codex 以节省高成本上下文。

## 关键洞察

- 多 Agent 的直接收益来自成本分层，而不只是“更聪明”

- Claude Code 适合做高层理解、任务拆解和结果审查，Codex 适合做被调度的执行者

- tmux 提供了最小可用的多 Agent 运行面板，使调度方案无需额外平台就能落地

- SubAgent 模式把用户与底层执行提示隔离开，降低了手工管理成本

- 这是把单一编程助手升级为“AI 开发团队”的第一步

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [Codex](entities/Codex.md)

- [tmux](entities/tmux.md)

- [Orchestrator 模式](concepts/Orchestrator 模式.md)

## 原始文章信息

- 作者：LawrenceW_Zen（劳伦斯）

- 来源：X书签

- 发布时间：2026-03-24

- 链接：[原文](https://x.com/LawrenceW_Zen/status/2035949835124351009)

## 个人评注

这类架构很适合 Tizer 的 HITL 编程流水线：把贵模型放在决策层，把便宜模型放在执行层，再为人保留审查和纠偏入口。
