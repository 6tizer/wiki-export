---
title: CaMeL 信任边界
type: concept
tags:
- 安全/隐私
- Agent 技能
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ab7f8a165c2e486b9a40391be3fbfa48
notion_id: ab7f8a16-5c2e-486b-9a40-391be3fbfa48
---

## 定义

CaMeL 信任边界是一种将 Agent 运行时中的**可信控制**与**不可信数据**分层隔离的安全机制，用来降低提示注入和越权调用对执行链路的污染。

## 核心要点

- 将系统指令、真实用户意图、已批准能力视为可信控制层

- 将网页内容、工具输出、检索结果、文件内容、会话回忆等视为不可信数据层

- 敏感操作必须对照可信计划授权，而不是直接听从不可信内容中的指令

- 重点保护终端执行、文件修改、记忆写入、外部消息、浏览器副作用等高风险能力

## 来源引用

- [摘要：Hermes Agent 生态继续疯涨](summaries/摘要：Hermes Agent 生态继续疯涨.md)（[原文](https://x.com/GitTrend0x/status/2046526941038280756)）

- [摘要：Hermes Agent 生态继续狂飙，又卷出一大批全新进化体！](summaries/摘要：Hermes Agent 生态继续狂飙，又卷出一大批全新进化体！.md)（[原文](https://x.com/GitTrend0x/status/2045837379827896407)）

- [摘要：Hermes Agent 生态要炸了，这波进化速度把我整不会了！](summaries/摘要：Hermes Agent 生态要炸了，这波进化速度把我整不会了！.md)（[原文](https://x.com/NFTCPS/status/2046076635200553224)）

## 关联概念

- [hermes-agent-camel](entities/hermes-agent-camel.md)

- [Hermes Agent](entities/Hermes Agent.md)

- Prompt Injection
