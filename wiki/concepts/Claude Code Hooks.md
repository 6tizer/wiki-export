---
title: Claude Code Hooks
type: concept
tags:
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/88f43e60c3b84b75af2b9ee8ab534371
notion_id: 88f43e60-c3b8-4b75-af2b-9ee8ab534371
---

## 定义

Claude Code Hooks 是 Claude Code 2.1 引入的事件驱动钩子机制，允许在特定时机（会话开始、工具调用后、上下文压缩前）自动执行用户自定义脚本，实现完全自动化的工作流增强。

## 关键要点

- **三个关键 Hook 时机**：

  - **SessionStart**：会话开始时触发，用于加载记忆和上下文

  - **PostToolUse**：工具调用后触发，用于提取和保存知识

  - **PreCompact**：上下文压缩前触发，用于保存当前会话状态防丢失

- **核心价值**：无需用户手动触发，完全在后台静默执行

- **典型应用**：三层记忆系统（知识图谱自动积累 + 每日笔记 + 隐性知识管理）

- **与 Wiki Compiler 的类比**：本质都是「事件触发 → 知识提取 → 结构化存储」模式

## 来源引用

- [摘要：Claude Code自动记忆来了！配合老金三层记忆系统全开源](summaries/摘要：Claude Code自动记忆来了！配合老金三层记忆系统全开源.md)（老金带你玩AI, 2026-02-28）— 详细讲述 Hooks 在三层记忆系统中的应用

- 《深度使用半年，我总结了 Claude Code 的架构、治理与工程实践》｜X书签文章｜原文链接：[https://x.com/HiTw93/status/2032091246588518683](https://x.com/HiTw93/status/2032091246588518683)

- [原文链接](https://x.com/shao__meng/status/2033497056460079453)｜[摘要：self-improving-agent：让 AI 编程助手从错误中真正学习的 OpenClaw Skills](summaries/摘要：self-improving-agent：让 AI 编程助手从错误中真正学习的 OpenClaw Skills.md)

- [原文链接](https://x.com/AYi_AInotes/status/2040238450373435857)｜[摘要：Claude Code Hooks：用 settings.json 把 AI 编程助手从「偶尔听话」升级成「永不出错的工程队友」](summaries/摘要：Claude Code Hooks：用 settings.json 把 AI 编程助手从「偶尔听话」升级成「永不出错的工程队友」.md)

- [原文链接](https://x.com/claudeai/status/2044131493966909862)｜《Learn more in the official documentation》｜来源条目：[摘要：Learn more in the official documentation](summaries/摘要：Learn more in the official documentation.md)

- [原文链接](https://x.com/rywiggs/status/2044448092477661638)｜《Creating a Second Brain with Claude Code》｜来源条目：[摘要：Creating a Second Brain with Claude Code](summaries/摘要：Creating a Second Brain with Claude Code.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ%3D%3D&mid=2247484861&idx=1&sn=53c1d6917185609b0f7342e8a06958cf&chksm=e9dd96a4a2b2e8e3b8f6566016312d36df186b16e1f374bd1dd87659ad8b5d9649bbdc1cd05f#rd)｜[摘要：这个开源工具太猛了！让 Claude Code 成本爆降 89%](summaries/摘要：这个开源工具太猛了！让 Claude Code 成本爆降 89%.md)

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [MCP 协议](concepts/MCP 协议.md)

- [第二大脑系统](concepts/第二大脑系统.md)

- [RTK](entities/RTK.md)

- [终端输出净化](concepts/终端输出净化.md)

- [上下文压缩](concepts/上下文压缩.md)
