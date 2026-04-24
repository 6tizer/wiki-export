---
title: Claude Code Agent 循环
type: concept
tags:
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/148adef65ba343f2b8a26c0f5b73f959
notion_id: 148adef6-5ba3-43f2-b8a2-6c0f5b73f959
---

## 定义

Claude Code Agent 循环是 Claude Code 内部驱动 AI 编程任务执行的核心状态机机制，决定了 Agent 如何在每一步决策中推进任务直至完成。

## 关键要点

- **状态机设计**：Agent 循环以状态机形式实现，每次迭代根据当前状态决定下一步动作

- **7 种 transition 原因**：循环的状态转移有 7 种明确定义的原因，涵盖工具调用、用户输入、任务完成等场景

- **pre-API pipeline**：在每次调用 LLM API 之前，存在专门的预处理管线，用于整理上下文、注入系统提示等

- **工具驱动执行**：循环的主要动力来自 40+ 工具的调用与响应，包括 Bash、文件读写、搜索、WebFetch 等

## 来源引用

- 来源：[@gerrox 对 Claude Code 内部架构的深度分析](https://github.com/roger2ai/claude-code-internals)（2026-04-01）

- 原始推文：[https://x.com/gerrox/status/2039137055746543860](https://x.com/gerrox/status/2039137055746543860)

- 《Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行》｜X书签文章｜原文链接：[https://x.com/gerrox/status/2039137055746543860](https://x.com/gerrox/status/2039137055746543860)｜来源条目：[摘要：Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行](summaries/摘要：Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行.md)

- 《Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构》｜X书签文章｜原文链接：[https://x.com/gerrox/status/2039137055746543860](https://x.com/gerrox/status/2039137055746543860)｜来源条目：[摘要：Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构](summaries/摘要：Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构.md)

- 《Claude Code 动态循环（Dynamic Looping）来了！》｜X书签文章｜原文链接：[https://x.com/servasyy_ai/status/2043107256846422407](https://x.com/servasyy_ai/status/2043107256846422407)｜来源条目：[摘要：Claude Code 动态循环（Dynamic Looping）来了！](summaries/摘要：Claude Code 动态循环（Dynamic Looping）来了！.md)

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [上下文压缩](concepts/上下文压缩.md)

- [Claude Code 多 Agent 协调](concepts/Claude Code 多 Agent 协调.md)

- [Claude Code 动态循环](concepts/Claude Code 动态循环.md)

- [Claude Code Monitor 工具](concepts/Claude Code Monitor 工具.md)

- [异步事件驱动编排](concepts/异步事件驱动编排.md)

- 《Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行》｜X书签文章｜来源条目：[摘要：Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行](summaries/摘要：Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行.md)

- 《Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构》｜X书签文章｜来源条目：[摘要：Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构](summaries/摘要：Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构.md)
