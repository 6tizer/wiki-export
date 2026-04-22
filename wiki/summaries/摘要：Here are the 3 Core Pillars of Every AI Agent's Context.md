---
title: 摘要：Here are the 3 Core Pillars of Every AI Agent's Context
type: summary
tags:
- Agent 技能
- 记忆系统
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b6881b2b1d2f938d0bef4d5
notion_url: https://www.notion.so/93a6313e04af4b21bf67fd1d6d189560
notion_id: 93a6313e-04af-4b21-bf67-fd1d6d189560
---

## 一句话摘要

这篇文章把 AI Agent 的上下文能力拆成三层：MCP 负责连接外部工具，RAG 负责检索外部知识，Agent Skills 负责沉淀可复用指令与操作模板。

## 关键洞察

- MCP 解决的是“怎么连工具”的标准化问题，本质是把外部服务接入从一次次写定制 API 变成统一协议接入。

- RAG 解决的是“模型不知道但又必须回答”的知识缺口问题，让 Agent 先检索、再生成，而不是直接幻觉式作答。

- Agent Skills 解决的是“重复把同类操作写进 Prompt”的低效问题，把高频操作知识封装成按需加载的能力单元。

- 这三者分别对应 Agent 的工具层、知识层和能力层，适合拿来做架构分层时的最小认知框架。

- 对 Agent 设计者来说，先区分“连接”“检索”“复用”三类问题，再选择基础设施，会比把所有问题都混成 Prompt Engineering 更清晰。

## 提取的概念

- [MCP 协议](concepts/MCP 协议.md)

- [RAG](concepts/RAG.md)

- [Agent Skills](concepts/Agent Skills.md)

## 原始文章信息

- 作者：@Ai_Vaidehi

- 来源：X书签

- 发布时间：2026-04-17

- 原文链接：[https://x.com/Ai_Vaidehi/status/2045050337149513974](https://x.com/Ai_Vaidehi/status/2045050337149513974)

- 源文章页面：MCP、RAG、Skills：每个 AI Agent 都绕不开的三大上下文支柱

## 个人评注

这篇内容适合作为 Tizer 工作流里的“Agent 基础构件速记卡”：在做 OpenClaw、HITL 或内容管线设计时，可以用它快速区分协议层、知识层和能力层，避免把 MCP、RAG、Skills 混成同一类基础设施。
