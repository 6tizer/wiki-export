---
title: OAuth Scope 最小化
type: concept
tags:
- 安全/隐私
- Agent 技能
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/65acffab82e7491a968019d4cc853e5a
notion_id: 65acffab-82e7-491a-9680-19d4cc853e5a
---

## 定义

OAuth Scope 最小化，是指在给第三方应用授权时，仅授予完成当前任务所必需的最小权限范围，避免形成过宽的长期访问能力。

## 关键要点

- 这篇文章最大的安全教训之一，就是员工给第三方 AI 工具授予了过宽的 Google Workspace OAuth scope。

- 一旦外部工具自身被攻破，过宽 scope 就会把单点失守放大为企业内部横向移动通道。

- 因此，OAuth scope 设计应被纳入接入评审、周期复核与可撤销性治理。

- 对 Agent 工具来说，Scope 最小化是“可用性”与“可控性”之间的关键平衡机制。

## 来源引用

- [摘要：开发 Next.js 的 Vercel 被黑，数据被叫卖](summaries/摘要：开发 Next.js 的 Vercel 被黑，数据被叫卖.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247515778&idx=1&sn=7ea594245be39b32a5209801826028de&chksm=c30b673cb0131150240310e0edc9fb2431c90632e73d2996a484db9838187d377076479820bb#rd)）

- [摘要：Vercel 刚刚确认内部系统被入侵了](summaries/摘要：Vercel 刚刚确认内部系统被入侵了.md)（[原文](https://x.com/Saccc_c/status/2045915716814073872)）
