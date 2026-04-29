---
title: 摘要：holaOS — 开源 Agent Computer
type: summary
tags:
- Harness 工程
- AI 产品
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/351701074b688111a534ce465efcacb1
notion_url: https://www.notion.so/Tizer/d2304244852749e180d181c2cc695c87
notion_id: d2304244-8527-49e1-80d1-81c2cc695c87
---

## 一句话摘要

holaOS 是一个开源的 Agent Computer，通过 Environment Engineering 方法论将计算机重新定义为人类与 AI Agent 共享的持久工作环境，超越传统 Agent Harness 的 session 限制。

## 关键洞察

- **环境 > Harness**：Harness Engineering 让单次 run 可运维，Environment Engineering 让工作本身持久、可检查、可移植、跨 run 一致——环境定义系统的能力上限

- **委托而非自动化**：核心目标不是替代人类，而是释放人类注意力用于意图、判断和审查，模型负责执行工作而非每次重建工作空间

- **共享操作上下文**：Agent 不在工作空间外部注入上下文，而是与人类共处同一环境——浏览器、文件、应用、凭证均为环境表面（environment surfaces）

- **长周期连续性**：数字工作天然碎片化且跨越长时间线（tabs、SaaS、文件、脚本），传统 Agent 在 run 结束后丢失连续性，holaOS 通过持久环境解决这一问题

- **开源社区驱动**：MIT 协议，GitHub 3400+ Stars，提供 Registry（可复用工作空间）+ App SDK + BYOK 模式

## 提取的概念

- [holaOS](entities/holaOS.md) — 开源 Agent Computer 产品

- [Environment Engineering](concepts/Environment Engineering.md) — 环境工程方法论

- [Harness Engineering](concepts/Harness Engineering.md) — 作为对比的 harness 工程方法论

- [Agent OS](concepts/Agent OS.md) — Agent 操作系统概念

## 原始文章信息

- **作者**：Jeffrey Li (@JeliPenguin)

- **来源**：X 推文线程

- **发布日期**：2026-04-28

- **链接**：[https://x.com/JeliPenguin/status/2049147344315388281](https://x.com/JeliPenguin/status/2049147344315388281)

- **GitHub**：[https://github.com/holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS)

## 个人评注

holaOS 的 Environment Engineering 理念与 OpenClaw 的工作流有交叉：都在探索如何让 Agent 在持久环境中高效工作，而非每次从零重建上下文。holaOS 强调的「文件是环境表面而非附件」「Memory 不是 Prompt Stuffing」等观点，对 OpenClaw 的记忆机制设计（如 Dreaming）有参考价值。其 Workspace 模型和 Registry 机制也为 Agent 协作提供了可复用的基础设施思路。
