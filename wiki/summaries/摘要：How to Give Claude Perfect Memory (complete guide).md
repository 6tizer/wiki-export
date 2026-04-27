---
title: 摘要：How to Give Claude Perfect Memory (complete guide)
type: summary
tags:
- 长期记忆
- 上下文管理
- 笔记工具
status: 已审核
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b688151b403c18a118cb9da
notion_url: https://www.notion.so/Tizer/4a6d5c49e3ed4061a13711d8afb39a27
notion_id: 4a6d5c49-e3ed-4061-a137-11d8afb39a27
---

## 一句话摘要

本文系统介绍了为 Claude 构建持久记忆的三层渐进式方案——从基础设置清理、到本地 .MD 文件驱动的上下文系统、再到 Obsidian/Notion 驱动的 AI 第二大脑知识库。

## 关键洞察

- **Layer 1（基础记忆）**：通过 Settings → Memory 手动清理/添加偏好、Project Instructions 注入上下文、对话中直接指令 Claude 记住/忘记信息、以及从 ChatGPT 等平台导入记忆数据，可在几分钟内显著改善 Claude 的上下文保持能力

- **Layer 2（Context File System）**：在本地创建 "Claude Master Folder"，包含 [Instructions.md](http://instructions.md/)、[Memory.md](http://memory.md/)、[Context.md](http://context.md/) 和 Archive 四个核心 Markdown 文件，Claude 在 Cowork/Claude Code 中可直接读写这些文件作为持久化记忆数据库，关键指令 "Update [Memory.md](http://memory.md/) with my preferences over time" 实现了自动化记忆积累

- **Layer 3（AI 第二大脑）**：Notion 方案（5 分钟连接，适合快速集成）和 Obsidian 方案（本地存储 + Karpathy 的 LLM Wiki 系统提示词，适合深度知识库构建）两条路径

- **渐进式复杂度设计**：三层系统分别对应不同用户群体——90% 用户只需 Layer 1，进阶用户用 Layer 2，重度用户用 Layer 3，降低了采用门槛

- **回复区亮点**：社区补充了 claude-mem（68k Stars 的持久记忆插件）、h5i（AI 感知的 Git 版本控制）、本地向量存储 + MCP 方案、Atomic 知识图谱等进阶方案，形成了完整的记忆系统生态图谱

## 提取的概念

- [记忆分层架构](concepts/记忆分层架构.md)（文章核心方法论：三层渐进式记忆系统）

- [Context Files](concepts/Context Files.md)（Layer 2 的 .MD 文件驱动记忆模式）

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)（Layer 3 Obsidian 方案的核心提示词系统）

- [claude-mem](entities/claude-mem.md)（回复区推荐的 Claude Code 持久记忆插件，68k Stars）

- [h5i](entities/h5i.md)（回复区提及的 AI 感知 Git 版本控制工具）

- [Progressive Disclosure](concepts/Progressive Disclosure.md)（claude-mem 采用的分层记忆检索策略）

## 原始文章信息

- **作者**：@aiedge_

- **来源**：X 书签

- **发布时间**：2026-04-22

- **原文链接**：[原文](https://x.com/aiedge_/status/2046966170868486512)

## 个人评注

本文对 Tizer 的工作流有直接参考价值：Layer 2 的 Context File System 模式与 OpenClaw 的 [CLAUDE.md](http://claude.md/) / [AGENTS.md](http://agents.md/) 规范高度吻合——本质上都是通过结构化 Markdown 文件为 AI Agent 注入持久上下文。Layer 3 的 Obsidian + Karpathy Wiki 方案则与当前知识 Wiki 的编译管线形成互补思路：一个是人工驱动的本地知识库，一个是 Agent 自动编译的结构化 Wiki。回复区提到的 claude-mem 的 Progressive Disclosure 策略（先索引后按需加载详情，节省 ~10x token）对 OpenClaw 的上下文管理优化有借鉴意义。
