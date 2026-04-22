---
title: 摘要：aiPool：用 TEE 打造无需信任的 AI Agent 代币发射台
type: summary
tags:
- Crypto/DeFi
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, 自动化
source_article_url: ''
notion_url: https://www.notion.so/f584c3b20555403ba78821244c79a1c6
notion_id: f584c3b2-0555-403b-a788-21244c79a1c6
---

## 一句话摘要

aiPool 通过将 AI Agent 部署在 TEE（可信执行环境）中，实现了无需信任的代币发射流程——私钥由 AI 独立掌控，任何人包括开发者都无法访问。

## 关键洞察

- TEE（可信执行环境）是处理器内硬件隔离安全区域，运行代码连宿主机操作系统都无法读取，可解决链上 Agent「有没有后门」的信任问题

- aiPool 由 Phala Network dstack SDK（基于 Intel TDX）提供底层支撑，私钥一旦生成永久不可访问，从根本上消除 Rug Pull 可能

- 首次发射约 10% 代币分发失败，但开发者无法介入只能等待 Agent 重试——这是 TEE 设计的「诚实代价」

- 同类项目还有 [Spore.fun](http://spore.fun/)（进化叙事）、[Gods.fun](http://gods.fun/)（社区治理），均基于 Phala Network TEE 基础设施

- 关键问题：技术层面信任已建立，但操作健壮性和用户教育仍需追赶

## 提取的概念

- TEE（可信执行环境）

- Phala Network

- dstack SDK

- Agent 钱包自主性

## 原始文章信息

- **作者**：@0xwitchy（0xWitch）

- **来源**：X 书签

- **发布日期**：2024-12-25

- **链接**：[https://x.com/0xwitchy/status/1871765740988277088](https://x.com/0xwitchy/status/1871765740988277088)

## 个人评注

TEE 方案对于 OpenClaw 的安全性设计有参考价值——特别是「Agent 持有钱包」这一设计模式。HITL 工作流中，如何平衡自主性和人工干预是类似的核心张力。
