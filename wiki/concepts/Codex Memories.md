---
title: Codex Memories
type: concept
tags:
- 长期记忆
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c2effac8535143689aad3b3903ca0c07
notion_id: c2effac8-5351-4368-9aad-3b3903ca0c07
---

## 定义

Codex Memories 是 OpenAI Codex 的记忆持久化功能，允许 Codex 将早期线程中的稳定偏好、工作流习惯、技术栈选择、项目约定和已知陷阱带入后续工作中。该功能默认关闭，需要用户手动开启。

## 关键要点

- 解决长跑 Agent 的**上下文断裂**问题：当任务跨越数小时或多个会话时，Memories 提供连续性

- 官方定位为「本地 recall layer」，不替代 [AGENTS.md](http://agents.md/) 等项目级配置文件

- 适合存储：个人编码偏好、团队约定、常用工具链配置

- 不适合存储：项目级规则（应放在 [AGENTS.md](http://agents.md/) 或 checked-in docs 中）

- Codex changelog 中出现 memory extensions、context-window lineage headers、state DB 等相关变更，表明底层工程在持续补强记忆和状态恢复能力

## 设计哲学

长任务不该靠单线程上下文硬扛，而要有**可回收、可注入、可审查的记忆层**。Codex Memories 是这一理念的产品化实现。

## 来源引用

- [摘要：GPT5.5 + Codex 如何跑一整夜，编程的下一步，不是辅助编程，是可托管执行单元](summaries/摘要：GPT5.5 + Codex 如何跑一整夜，编程的下一步，不是辅助编程，是可托管执行单元.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyMzY1NTM0Mw%3D%3D&mid=2247515158&idx=1&sn=a656396814f65b8053981d852d11bb54&chksm=c0ba44de9a9054cf724edaed2a5cda4d44ea80568c1c43a3b3d2de3699534f4295bfaf69ba91#rd)）
