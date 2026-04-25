---
title: Claude Code 上下文管理
type: concept
tags:
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/9f11263429354910a39f09b999557f41
notion_id: 9f112634-2935-4910-a39f-09b999557f41
---

## 定义

Claude Code 上下文管理是 Claude Code 防止上下文窗口溢出的多层防御机制，通过 6 层防线在 Agent 长时间运行时保持上下文质量与可用性。

## 关键要点

- **6 层防线**：从最轻量到最重量级依次排列，优先使用低成本操作

  - 第 1 层：廉价截断（简单丢弃旧消息）

  - 第 2-5 层：逐步升级的摘要与压缩策略

  - 第 6 层：完整摘要重建（最重，仅在必要时触发）

- **渐进式降级**：系统根据当前上下文长度自动选择合适的压缩层级

- **与工具调用协作**：上下文管理需感知工具调用结果的大小，防止单次工具输出占满窗口

## 来源引用

- [摘要：这样用 Opus 4.7，才能发挥实力](summaries/摘要：这样用 Opus 4.7，才能发挥实力.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247515662&idx=1&sn=bfcc64cdceb913aef59f697c1ecbfa8d&chksm=c3914681eabbc4c3c559e95297d8d5b85aebabf0c4c93a5d517e6784d086e7b7ff3aa9abee9e#rd)）

- [摘要：把 Claude Code 源码蒸馏成 Agent Skill — Harness Engineering 实践](summaries/摘要：把 Claude Code 源码蒸馏成 Agent Skill — Harness Engineering 实践.md)（[原文](https://github.com/roger2ai/claude-code-internals)，2026-04-01）

- [摘要：Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统](summaries/摘要：Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统.md)（[原文](https://x.com/gerrox/status/2039137055746543860)）

- [摘要：深度使用半年，我总结了 Claude Code 的架构、治理与工程实践](summaries/摘要：深度使用半年，我总结了 Claude Code 的架构、治理与工程实践.md)｜X书签文章｜原文链接：[https://x.com/HiTw93/status/2032091246588518683](https://x.com/HiTw93/status/2032091246588518683)

- [摘要：Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统](summaries/摘要：Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统.md)｜X书签文章｜原文链接：[https://x.com/troyhua/status/2039052328070734102](https://x.com/troyhua/status/2039052328070734102)

- [摘要：Claude Code 的七层记忆体系：从亚毫秒级缓存到「梦境」式整合](summaries/摘要：Claude Code 的七层记忆体系：从亚毫秒级缓存到「梦境」式整合.md)｜X书签文章｜原文链接：[https://x.com/shao__meng/status/2039153466229088451](https://x.com/shao__meng/status/2039153466229088451)

- [摘要：继续分享一些 harness engineering 实际经验](summaries/摘要：继续分享一些 harness engineering 实际经验.md)（[原文](https://x.com/hylarucoder/status/2044041420475138514)）

- [摘要：Using Claude Code: Session Management & 1M Context](summaries/摘要：Using Claude Code- Session Management & 1M Context.md)（[原文](https://x.com/trq212/status/2044548257058328723)）

- [摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！](summaries/摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！.md)（[原文](https://x.com/AYi_AInotes/status/2044625894556230013)）

- [摘要：Claude Code Skills 会悄悄失效：一个被忽视的上下文截断问题](summaries/摘要：Claude Code Skills 会悄悄失效：一个被忽视的上下文截断问题.md)（[原文](https://x.com/garrytan/status/2046981289031667961)）

## 关联概念

- [Agent Loop](concepts/Agent Loop.md)

- Agent Teams

- [Verification Loop](concepts/Verification Loop.md)

- [四步 PRD 对齐法](concepts/四步 PRD 对齐法.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Context Rot](concepts/Context Rot.md)

- [Rewind](concepts/Rewind.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Claude Code](entities/Claude Code.md)
