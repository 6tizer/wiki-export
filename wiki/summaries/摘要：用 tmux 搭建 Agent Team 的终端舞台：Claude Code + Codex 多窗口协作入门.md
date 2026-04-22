---
title: 摘要：用 tmux 搭建 Agent Team 的终端舞台：Claude Code + Codex 多窗口协作入门
type: summary
tags:
- Coding Agent
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: Agent, Cursor, LLM, 自动化
source_article_url: https://www.notion.so/336701074b68819b97eac2d3f8931516
notion_url: https://www.notion.so/cb75d6f8d1cd4e6b9f47b546e9b91f2e
notion_id: cb75d6f8-d1cd-4e6b-9f47-b546e9b91f2e
---

## 一句话摘要

tmux 在多 Agent 编程场景里不只是分屏工具，而是让 Claude Code、Codex 和观察面板共存的终端协作底座。

## 关键洞察

- 多 Agent 编程真正的基础设施常常不是新框架，而是老牌终端工具的重新组合

- tmux 的分屏与会话持久化能力，正好满足 Agent Team 的并行执行与长时运行需求

- 让 Claude 帮用户安装和配置 tmux，本身就是 AI 辅助开发环境搭建的典型范式

- 远程服务器、VPS 和 SSH 场景让 tmux 比本地 GUI 终端更有长期价值

- 对 Agent Team 来说，观察、接管与纠偏和执行本身一样重要

## 提取的概念

- [tmux](entities/tmux.md)

- [Agent Team](concepts/Agent Team.md)

- [Claude Code](entities/Claude Code.md)

- [Codex](entities/Codex.md)

## 原始文章信息

- 作者：劳伦斯（@LawrenceW_Zen）

- 来源：X书签

- 发布时间：未提及

- 链接：[原文](https://x.com/LawrenceW_Zen/status/2035383740239855810)

## 个人评注

这篇文章对 Tizer 的启发是，很多多 Agent 协作并不需要重型平台，先把观察窗口、执行窗口和日志窗口拆清楚，就能把 HITL 介入点设计得更自然。
