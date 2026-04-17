---
title: 摘要：134k Star 的宝藏仓库：AI 编程工具的 System Prompt 全被扒出来了
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Cursor, Agent, LLM
source_article_url: ''
notion_url: https://www.notion.so/8ac22bdc691044e598a9f89ec9b1836b
notion_id: 8ac22bdc-6910-44e5-98a9-f89ec9b1836b
---

### 一句话摘要

一个高热度开源仓库把多款 AI 编程工具的 system prompt、工具定义和模型配置集中公开，价值不在照抄，而在于研究成熟产品的提示结构、安全边界和工作流设计。

### 关键洞察

- 该仓库覆盖 Cursor、Claude Code、Devin、v0、Perplexity 等多类产品，说明商业级提示工程已经具备可比较的“样板间”价值。

- 提取路径主要包括提示注入、逆向分析和社区协作，这同时暴露了 Agent 产品的安全薄弱面。

- 真正的竞争壁垒并不只是 prompt 文案本身，而是评测、反馈闭环和持续迭代机制。

### 提取的概念

- [System Prompt 泄露](concepts/System Prompt 泄露.md)

- [提示注入](concepts/提示注入.md)

- [AI 工具逆向分析](concepts/AI 工具逆向分析.md)

### 原始文章信息

- 作者：凡人小北（@frxiaobei）

- 来源：X书签

- 发布时间：2026-03-05

- 链接：[原文](https://x.com/frxiaobei/status/2029561950322168284)

### 个人评注

- 这类材料很适合拆成 Tizer 的 Agent 设计模式样本库，用来反向校准 HITL、工具权限和 system prompt 的边界设计。
