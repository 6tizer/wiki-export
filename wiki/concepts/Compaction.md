---
title: Compaction
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/db4d6197c3984185bb0c7d8ec325a815
notion_id: db4d6197-c398-4185-bb0c-7d8ec325a815
---

## 定义

Compaction 是 Anthropic Harness 工程指南中推荐的一种**上下文压缩技术**，让 Claude 在长时任务中总结过去的上下文，以保持对话连续性并避免超出上下文窗口限制。

## 核心机制

- 当对话历史过长时，系统自动将旧消息替换为精炼摘要

- 目的是在有限的 context window 内保留最关键的信息

- 属于 Anthropic 官方推荐的 Agent 长时运行策略之一

## 要点

- **优势**：有效延长 Agent 的有效工作时长，避免上下文窗口溢出

- **风险**：压缩后 Agent 可能丢失之前的决策细节和约定，导致行为退化

- 与 Memory Folder 是互补策略：Compaction 侧重「压缩保留」，Memory Folder 侧重「外部持久化」

- Sonnet 4.5 在感觉到 context 上限时会提前收工，加入 Compaction 后可延长有效工作时间

## 关联概念

- [Context Engineering](concepts/Context Engineering.md)

- [显式外部状态](concepts/显式外部状态.md)

- [Thought Signatures](concepts/Thought Signatures.md)

- [三省六部式多 Agent 架构](concepts/三省六部式多 Agent 架构.md)

- [Agent Harness](concepts/Agent Harness.md)

- [In Distribution](concepts/In Distribution.md)

- [Sandbox Agents](concepts/Sandbox Agents.md)

## 来源引用

- [摘要：这样用 Opus 4.7，才能发挥实力](summaries/摘要：这样用 Opus 4.7，才能发挥实力.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247515662&idx=1&sn=bfcc64cdceb913aef59f697c1ecbfa8d&chksm=c3914681eabbc4c3c559e95297d8d5b85aebabf0c4c93a5d517e6784d086e7b7ff3aa9abee9e#rd)）

- [摘要：Claude Code Auto Dream 记忆整理功能深度解析](summaries/摘要：Claude Code Auto Dream 记忆整理功能深度解析.md)— 数字生命卡兹克（微信）

- [摘要：OpenClaw 深度使用指南：10 个让 Agent 越用越顺手的实战技巧](summaries/摘要：OpenClaw 深度使用指南：10 个让 Agent 越用越顺手的实战技巧.md)（sitinme，X书签）— 从实操角度补充手动 /compact 与外部状态文件的搭配策略

- [原文链接](https://x.com/hwchase17/status/2042978500567609738)｜《Your harness, your memory》｜源文章：Harrison Chase：你的 Agent Harness，就是你的记忆

- [原文链接](https://x.com/sujingshen/status/2043898494818410731)｜《三省六部幻觉：为什么"虚拟公司"式多Agent架构在工程上不成立》｜来源条目：三省六部幻觉：为什么「虚拟公司」式多 Agent 架构在工程上走不通

- [原文链接](https://x.com/jxnlco/status/2044469127696556153)｜《Sandboxes are coming to the Agents SDK》｜源文章：OpenAI Agents SDK 沙盒：让 AI Agent 真正「留下工作成果」
