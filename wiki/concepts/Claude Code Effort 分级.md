---
title: Claude Code Effort 分级
type: concept
tags:
- Harness 工程
- 推理优化
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f32823cd8adf4fb29046cf4558896dd2
notion_id: f32823cd-8adf-4fb2-9046-cf4558896dd2
---

## 定义

Claude Code Effort 分级是 Claude Code 中用于控制模型推理深度的参数体系，允许用户按任务复杂度选择 low / medium / high / xhigh / max 五档推理努力程度，直接影响 Token 消耗和输出质量。

## 关键要点

- **五档分级**：low（快速修复、机械任务）、medium（多数提示的性价比最优）、high（需要深度推理）、xhigh（Opus 4.7 agentic coding 默认值）、max（边际收益递减，约为 xhigh 的 2 倍成本）

- **按提示设置，非按会话**：effort 应在每个 prompt 上单独调节，而非全局锁定在高档

- **默认推理消耗约为 medium 的 2 倍**：未主动降档的用户会在日常任务上产生不必要的 Token 开销

- **与模型路由配合**：在 Opus 会话中用 effort 控制主 Agent 推理深度，同时将机械任务委托给 Haiku/Sonnet 子 Agent

## 来源引用

- [摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.](summaries/摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.md)（[原文](https://x.com/PawelHuryn/status/2048170309396926577)）

## 关联概念

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Prompt Cache](concepts/Prompt Cache.md)
