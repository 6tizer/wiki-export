---
title: 摘要：Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统
type: summary
tags:
- Coding Agent
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: Agent, LLM, 自动化
source_article_url: https://www.notion.so/33d701074b6881ec9a37c4894d775127
notion_url: https://www.notion.so/5e3d5c1e456c42199dd28a6b386338d6
notion_id: 5e3d5c1e-456c-4219-9dd2-8a6b386338d6
---

### 一句话摘要

这篇文章把 Claude Code 的长期可用性秘密讲清楚了：不是单靠大上下文，而是靠一套层层递进、成本优先的记忆与压缩系统维持长会话质量。

### 关键洞察

- Claude Code 的核心不是“记住所有内容”，而是按成本从低到高逐层拦截上下文膨胀。

- 微压缩、会话记忆和完整压缩分别承担不同层级的整理任务，避免一上来就做昂贵总结。

- Prompt Cache 被放在极高优先级，这说明上下文工程已经直接影响商业成本与产品体验。

- Dreaming 这类后台整理机制，代表 Coding Agent 开始具备真正的长期记忆维护能力。

### 提取的概念

- [Claude Code](entities/Claude Code.md)

- [Claude Code Memory](concepts/Claude Code Memory.md)

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [微压缩](concepts/微压缩.md)

- [会话记忆](concepts/会话记忆.md)

- Prompt Cache

- [Claude Code Dreaming](concepts/Claude Code Dreaming.md)

### 原始文章信息

- 作者：@troyhua

- 来源：X书签

- 发布时间：2026-03-31

- 链接：[原文](https://x.com/troyhua/status/2039052328070734102)

### 个人评注

这类条目非常适合进入 Tizer 的 Coding Agent 方法论层，因为它解释了为什么有些工具能越用越顺，而有些长会话会越用越笨。
