---
title: 摘要：Live streaming
type: summary
tags:
- 多Agent协作
- Agent 协作模式
status: 已审核
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881d8aea2f22a76ee83a7
notion_url: https://www.notion.so/Tizer/f59d9747d6d4435cbc20befe05885a41
notion_id: f59d9747-d6d4-435c-bc20-befe05885a41
---

## 一句话摘要

Multica 是一个开源的模型无关多智能体编排平台，定位为 OpenAI Symphony 的通用替代方案，支持 Claude Code、Hermes、OpenClaw、Cursor Agent 等多种编程智能体在同一工作空间内协作。

## 关键洞察

- **模型无关是核心卖点**：Symphony 绑定 Codex，而 Multica 支持任意 coding agent，消除供应商锁定风险

- **面向团队的多用户协作**：与 Paperclip（侧重零人工公司）不同，Multica 以 issue/project 为组织单元，支持多人在同一 workspace 协作

- **社区反馈积极**：多人表示已在尝试，尤其看重 agent-agnostic gateway 带来的灵活性

- **共识挑战：共享上下文与冲突解决**：社区讨论指出，多 agent 协同的难点不在于生成更多 agent，而在于跨 agent 的上下文共享和冲突解决

- **生态位对比**：Multica（轻量、issue 驱动、代码原生） vs Paperclip（重型、组织结构驱动、通用业务） vs Symphony（Codex 专用、隔离运行）

## 提取的概念

- [Multica](entities/Multica.md)

- [Symphony](entities/Symphony.md)

- [Paperclip](entities/Paperclip.md)

## 原始文章信息

- **作者**：@jiayuan_jy（Jiayuan (JY) Zhang）

- **来源**：X 书签

- **发布时间**：2026-04-28

- **原文链接**：[原推文](https://x.com/jiayuan_jy/status/2049027815195000840)

## 个人评注

本文展示了 coding agent 编排领域从单一供应商向模型无关方向演进的趋势。对 Tizer 的 OpenClaw 生态而言，Multica 作为 agent-agnostic 编排层是一个值得关注的集成目标——可以将 OpenClaw Agent 纳入 Multica 的 issue 驱动工作流中，实现团队级别的多 agent 协作。此外，社区关于「共享上下文与冲突解决」的讨论也与 OpenClaw 的 Context Engine 设计方向高度相关。
