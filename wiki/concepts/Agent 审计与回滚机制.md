---
title: Agent 审计与回滚机制
type: concept
tags:
- Agent 安全
- Harness 工程
- 链上协议
status: 审核中
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/848b1286e5cd4951883c27264b992d0e
notion_id: 848b1286-e5cd-4951-883c-27264b992d0e
---

## 定义

Agent 审计与回滚机制，是指当 AI Agent 获得系统写权限后，为避免误操作、越权和批量事故而设计的日志记录、审批确认、权限边界与快速撤销能力。

## 关键要点

- Agent 从顾问变成执行者后，风险会从提示词层面上升到系统操作层面。

- 审计日志决定事后能不能定位问题，回滚能力决定事故能不能低成本恢复。

- 在高频批量修改场景里，权限边界与人工抽检往往比模型能力本身更关键。

- 没有这套机制，效率提升得越快，出错时的损失也越大。

## 来源引用

- [原文链接](https://x.com/AYi_AInotes/status/2042970104921542896)｜《Shopify刚放了个大招，绝大多数人估计半年后才会反应过来。》｜来源条目：Shopify AI Toolkit：把 AI Agent 变成你的电商运营团队

## 关联概念

- [MCP 协议](concepts/MCP 协议.md)

- [Claude Code](entities/Claude Code.md)
