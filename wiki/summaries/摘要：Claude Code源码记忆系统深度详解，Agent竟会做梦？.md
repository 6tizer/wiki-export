---
title: 摘要：Claude Code源码记忆系统深度详解，Agent竟会做梦？
type: summary
tags:
- 长期记忆
- 上下文管理
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: Claude Code, RAG/Memory, 深度分析
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a2764d9585344b97869c6a83b149a0ef
notion_id: a2764d95-8534-4b97-869c-6a83b149a0ef
---

**一句话摘要**：Claude Code 的记忆系统通过四类记忆、三重压缩与 AutoDream 模块构建了类人类睡眠整理机制，是提升 AI 产品质量的关键基础设施。

**关键洞察**

- 四类记忆：用户记忆、反馈记忆、项目记忆、参考记忆，各自承担不同语义层次

- 重要原则：不仅记录错误，也记录成功——避免 AI 变得过于保守

- 三重压缩机制确保在上下文窗口满载时仍能有效处理信息

- 记忆以 Markdown 文件存储，便于人工审查与修改（与 OpenClaw 记忆设计理念一致）

- AutoDream 在用户工作间隙自动触发，模拟人类睡眠巩固记忆

**提取的概念**：Claude Code Memory、Auto Dream、Compaction

**原始文章信息**

- 作者：傅盛

- 来源：微信

- 发布时间：2026-04-02

- 链接：[https://mp.weixin.qq.com/s?__biz=MjM5NjgzMzkwMQ==&mid=2653649883&idx=1&sn=8819b6c118d609ef7ee5f9b70051877b](https://mp.weixin.qq.com/s?__biz=MjM5NjgzMzkwMQ%3D%3D&mid=2653649883&idx=1&sn=8819b6c118d609ef7ee5f9b70051877b)

**个人评注**：本文是理解 Claude Code 记忆架构的最佳入门材料，其中"同时记录成功与失败"的原则和 AutoDream 机制值得直接借鉴到 OpenClaw 的 HITL 记忆迭代流程中。
