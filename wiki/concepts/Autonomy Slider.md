---
title: Autonomy Slider
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7d7aee3617314cca9de2c4e72a88ff77
notion_id: 7d7aee36-1731-4cca-9de2-c4e72a88ff77
---

## 定义

Autonomy Slider（自主度滑块）是 Andrej Karpathy 在 2026 年 YC AI Startup School 演讲中提出的 Agent 设计模式。核心思想是：不要追求全自主（full autonomy），而是为 LLM 应用设计一个可调节的自主度控制机制，让用户或系统可以在「完全人工监督」和「高度自主」之间自由滑动。

## 关键要点

- 构建 partial-autonomy LLM 应用，而非追求完全自主的 Agent

- 将 LLM 类比为 1960 年代的操作系统——需要人类在 loop 中进行监督

- 提供 autonomy slider，让终端用户根据任务风险和信任程度调整 Agent 的自主等级

- 配合 human-AI supervision loop 和 generate-verify cycle 使用

- 在 Agent 友好的流程中加速「生成-验证」循环，而非试图消除人类参与

## 与其他概念的关系

- 与 HITL（Human-in-the-Loop）模式互补：Autonomy Slider 是 HITL 的产品化实现

- 与 Harness 工程相关：滑块机制属于执行环境的安全边界设计

- 与 Context Engineering 配合：在不同自主度下，上下文打包策略也应动态调整

## 来源引用

- [摘要：Build: Karpathy 2026 AI Agent Playbook](summaries/摘要：Build- Karpathy 2026 AI Agent Playbook.md)（[原文](https://x.com/DataChaz/status/2050114234973863975)）
