---
title: Mercury
type: entity
tags:
- Agent 安全
- 上下文管理
- CLI 工具
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6483e3b3316c4a0da176aebd11365630
notion_id: 6483e3b3-316c-4a0d-a176-aebd11365630
---

## 定义

Mercury 是 Cosmic Stack 推出的本地 AI Agent / CLI 框架，主打权限硬化、Token Budget 控制、纯文本 Soul 配置与后台常驻运行，定位是一个“先请求授权、再执行”的工具型 Agent 基座。

## 关键要点

- **权限优先**：对文件访问范围、命令执行和第三方技能授权做显式边界控制。

- **成本可控**：提供每日 Token Budget，并在接近阈值时自动收缩上下文。

- **身份可维护**：用 `soul.md`、`persona.md`、`taste.md`、`heartbeat.md` 四个文件定义 Agent 的人格与偏好。

- **后台常驻**：支持以零依赖守护进程方式运行，具备开机自启、崩溃恢复与定时调度能力。

- **多通道接入**：同时覆盖 CLI 与 Telegram 等交互入口。

## 来源引用

- [摘要：Mercury: The AI Agent We All Wanted - Where Control, Permissions, and Autonomy Finally Got Real](summaries/摘要：Mercury- The AI Agent We All Wanted - Where Control, Permissions, and Autonomy Finally Got Real.md)（[原文](https://x.com/Ctrl_Alt_Zaid/status/2046902326657749114)）

- [摘要：Why Karpathy's Second Brain Breaks at Agent Scale. How Mercury Solves It.](summaries/摘要：Why Karpathy's Second Brain Breaks at Agent Scale. How Mercury Solves It.md)（[原文](https://x.com/Ctrl_Alt_Zaid/status/2049082538686382397)）

- [摘要：Mercury asks first — and remembers what matters.](summaries/摘要：Mercury asks first — and remembers what matters.md)（[原文](https://x.com/AYi_AInotes/status/2049318687065174449)）

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [CerebroCortex](entities/CerebroCortex.md)

- [Agent 记忆基础设施](concepts/Agent 记忆基础设施.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)
