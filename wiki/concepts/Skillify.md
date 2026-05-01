---
title: Skillify
type: concept
tags:
- Harness 工程
- 加密资产
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/cb4a9377b27c46ed9ef2bfd453a25eb4
notion_id: cb4a9377-b27c-46ed-9ef2-bfd453a25eb4
---

## 定义

Skillify 是一种把 Agent 的单次成功经验或失败修复，升级为可复用 Skill 的工程化方法：将问题处理流程、确定性代码、测试、路由与评测一起固化，使同类错误在结构上更难再次发生。

## 关键要点

- 它强调“不是记住答案，而是记住做法”，把会话中的临时修补沉淀为长期能力。

- Skillify 通常不只生成一份 `SKILL.md`，还要求补齐脚本、单元测试、集成测试、LLM eval、resolver trigger 与 smoke test。

- 它把 Agent 可靠性从 prompt 约束转向工程约束，让改进具备可验证、可回归的特性。

- 在实践中，Skillify 既可以用于失败复盘，也可以用于把一次成功原型升级成可持续复用的基础设施。

## 关联概念

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Resolver](concepts/Resolver.md)

- [check-resolvable](concepts/check-resolvable.md)

- [Latent vs. Deterministic](concepts/Latent vs. Deterministic.md)

- [确定性工具](concepts/确定性工具.md)

- [GBrain](entities/GBrain.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [self-improving-agent](concepts/self-improving-agent.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Claude Code](entities/Claude Code.md)

## 来源引用

- [摘要：How to really stop your agents from making the same mistakes](summaries/摘要：How to really stop your agents from making the same mistakes.md)（[原文](https://x.com/garrytan/status/2046876981711769720)）

- [摘要：Claude Code Skills 会悄悄失效：一个被忽视的上下文截断问题](summaries/摘要：Claude Code Skills 会悄悄失效：一个被忽视的上下文截断问题.md)（[原文](https://x.com/garrytan/status/2046981289031667961)）

- [摘要：Had no idea but there is a lot of simultaneous discovery in agentic engineering these days](summaries/摘要：Had no idea but there is a lot of simultaneous discovery in agentic engineering these days.md)（[原文](https://x.com/garrytan/status/2047039110326673872)）

- [摘要：Big drop for GBrain v0.19.](summaries/摘要：Big drop for GBrain v0.19.md)（[原文](https://x.com/garrytan/status/2047504667127799974)）
