---
title: Context Compaction
type: concept
tags:
- 记忆系统
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/51fe93af771146d5b0ce8629be812fa2
notion_id: 51fe93af-7711-46d5-b0ce-8629be812fa2
---

## 定义

Context Compaction 是在长对话或长任务中主动压缩上下文、保留关键状态并卸载冗余内容的工程策略，用于降低成本并延缓上下文腐烂。

## 关键要点

- 能同时改善 token 成本和执行稳定性

- 适合与记忆文件、阶段摘要和工具输出卸载结合

- 是长时程 Agent 的常见基础设施能力

## 来源引用

- [摘要：别问 Claude 能为你做什么，问你能为 Claude 做什么：Anthropic 内部的 Vibe Coding 方法论](summaries/摘要：别问 Claude 能为你做什么，问你能为 Claude 做什么：Anthropic 内部的 Vibe Coding 方法论.md)（[原文](https://x.com/GoSailGlobal/status/2046785975582667071)）

- [摘要：What is an Agent Harness](summaries/摘要：What is an Agent Harness.md)（[原文](https://x.com/aparnadhinak/status/2046980769747533830)）

- 《OpenClaw 烧 Token 的真相：最贵的不是写代码，而是 web fetch》｜X书签文章｜原文链接：[https://x.com/marvin_tong/status/2031557670826815705](https://x.com/marvin_tong/status/2031557670826815705)

- 《Why memory isn't a plugin (it's the harness)》｜X书签｜2026/04/03｜主链接：[X 原文](https://x.com/sarahwooders/status/2040121230473457921)｜源页面：记忆不是插件，它是 Harness 本身：Letta 对 Agent 架构的重新定义

- [原文链接](https://x.com/trq212/status/2044548257058328723)｜《Using Claude Code: Session Management & 1M Context》｜来源条目：[摘要：Using Claude Code: Session Management & 1M Context](summaries/摘要：Using Claude Code- Session Management & 1M Context.md)

- [原文链接](https://x.com/AYi_AInotes/status/2044625894556230013)｜《说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！》｜来源条目：[摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！](summaries/摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！.md)

## 关联概念

- [Context Rot](concepts/Context Rot.md)

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Rewind](concepts/Rewind.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Claude Code](entities/Claude Code.md)

- [Vibe Coding](concepts/Vibe Coding.md)

- [叶子节点策略](concepts/叶子节点策略.md)

- [可验证性设计](concepts/可验证性设计.md)
