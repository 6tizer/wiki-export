---
title: PreToolUse
type: concept
tags:
- Coding Agent
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/68dd85595090488f9ca611f51a2d4ce4
notion_id: 68dd8559-5090-488f-9ca6-11f51a2d4ce4
---

## 定义

PreToolUse 是 Claude Code Hooks 中在工具调用前触发的事件，可用于检查和阻断高风险操作。

## 核心要点

- 常用于拦截危险命令和敏感文件访问

- 能把规则从提示建议升级为确定性执行

- 是构建安全边界和审批机制的关键挂点

## 来源引用

- 《Claude Code Hooks：用 settings.json 把 AI 编程助手从「偶尔听话」升级成「永不出错的工程队友」》｜X书签文章｜原文链接：[https://x.com/AYi_AInotes/status/2040238450373435857](https://x.com/AYi_AInotes/status/2040238450373435857)｜来源条目：Claude Code Hooks：用 settings.json 把 AI 编程助手从「偶尔听话」升级成「永不出错的工程队友」

- [摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南](summaries/摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ%3D%3D&mid=2247486947&idx=1&sn=92ca2b4f44cadd181eb6b40087a2531b&chksm=a7e11bb1d385c29bce1587e79207574fba3835086a7fbed287fbf12e86194e37111fb2982d78#rd)）

- [摘要：什么才是真正的 Harness Engineering？](summaries/摘要：什么才是真正的 Harness Engineering？.md)（[原文](https://x.com/SaitoWu/status/2045458721929892345)）

- [摘要：rtk：给 AI 编码工具装上「信息压缩阀」，Token 消耗最高降 90%](summaries/摘要：rtk：给 AI 编码工具装上「信息压缩阀」，Token 消耗最高降 90%.md)（[原文](https://x.com/laogui/status/2045677115341934867)）

## 关联概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [PostToolUse](concepts/PostToolUse.md)

- [Command Hooks](concepts/Command Hooks.md)

- [Prompt Hooks](concepts/Prompt Hooks.md)

- [Agent Hooks](concepts/Agent Hooks.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Guardrails](concepts/Guardrails.md)

- [Review Agents](concepts/Review Agents.md)

- [RTK](entities/RTK.md)

- [上下文压缩](concepts/上下文压缩.md)
