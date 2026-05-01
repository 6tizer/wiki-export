---
title: 摘要：OpenClaw × SearxNG：零成本给你的 AI 助手装上「搜索外脑」
type: summary
tags:
- OpenClaw
- MCP 协议
- RAG/检索
- AI 产品
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, LLM, 自动化, Agent
source_article_url: ''
notion_url: https://www.notion.so/Tizer/04f87b8cda9f4eafb05cd94eeb1cdc31
notion_id: 04f87b8c-da9f-4eaf-b05c-d94eeb1cdc31
---

### 一句话摘要

这篇文章主张用 SearxNG 直接为 OpenClaw 提供原始搜索结果，而不是再套一层小模型总结，从而以更低成本获得更干净的联网检索能力。

### 关键洞察

- 搜索系统最重要的不是“先帮你总结”，而是把原始结果高质量地交给主模型判断。

- SearxNG + MCP 的组合说明，很多本地 Agent 能力可以通过标准接口低成本补齐。

- “LLM 叠 LLM”在检索链路里往往会带来细节损耗和不必要复杂度。

### 提取的概念

- [SearxNG](concepts/SearxNG.md)

- [Antigravity MCP](concepts/Antigravity MCP.md)

- [LLM 叠 LLM 反模式](concepts/LLM 叠 LLM 反模式.md)

### 原始文章信息

- 作者：@YuLin807（QingYue）

- 来源：X书签

- 发布时间：未明确给出

- 链接：[原文](https://x.com/YuLin807/status/2030996280051462609)

### 个人评注

- 对 Tizer 的知识工作流来说，这种“尽量保留原始信息，让主模型做判断”的设计原则值得直接吸收。
