---
title: 摘要：Claude + Obsidian | How to use your second brain
type: summary
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b68819aa64ce484e7f7fcea
notion_url: https://www.notion.so/Tizer/e46bb96c2fee47e6b969d06672ee3f34
notion_id: e46bb96c-2fee-47e6-b969-d06672ee3f34
---

## 一句话摘要

这篇文章把 `Claude Code + Obsidian + claude-obsidian` 组合包装成一个可持续增长的第二大脑方案，核心是让 AI 负责把原始资料、对话与研究结果持续编译成结构化 Wiki，而不是只做一次性的聊天检索。

## 关键洞察

- **claude-obsidian** 的核心卖点不是“让 AI 搜索笔记”，而是让 Claude 直接维护一个持续增长的知识 Wiki

- 它明确继承了 **Karpathy LLM Wiki 方法论**，强调把 PDF、URL、转录稿等原始资料编译成结构化页面，并保持交叉链接

- `/wiki`、`/save`、`/autoresearch`、`/canvas` 四类命令分别承担初始化、会话归档、深度研究和可视化整理的角色

- 系统通过 `hot.md`、`index.md` 和按需加载相关页面来控制上下文成本，体现了 **记忆分层架构** 的工程思路

- `.raw/ → ingest → wiki/` 的日常摄入循环，让知识资产以增量方式积累，而不是堆积成孤立文件

## 提取的概念

- [claude-obsidian](entities/claude-obsidian.md)

- [Claude Code](entities/Claude Code.md)

- [Obsidian](entities/Obsidian.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Ingest 摄入流程](concepts/Ingest 摄入流程.md)

- [记忆分层架构](concepts/记忆分层架构.md)

- [autoresearch](entities/autoresearch.md)

## 原始文章信息

- 作者：@defileo

- 来源：X书签

- 发布时间：2026-04-13

- 原文链接：[https://x.com/defileo/status/2043762213597397179](https://x.com/defileo/status/2043762213597397179)

## 个人评注

- 这类工作流和 Tizer 当前的内容编译链路高度一致，本质上都是把“原始输入 → 摘要 → 概念/实体 → 交叉引用”做成可持续运行的知识编译系统

- 对 Tizer 而言，最值得吸收的不是 Obsidian 本身，而是 **编译式知识库 + 分层记忆 + 增量摄入** 这一整套组织方式
