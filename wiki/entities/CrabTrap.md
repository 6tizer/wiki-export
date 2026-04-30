---
title: CrabTrap
type: entity
tags:
- 安全/隐私
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ab9748537ba5457a9634017a4b4626be
notion_id: ab974853-7ba5-457a-9634-017a4b4626be
---

## 定义

CrabTrap 是 Brex 开源的 Agent 安全基础设施，形态是一个位于传输层的 HTTP/HTTPS 代理。它拦截 AI Agent 的全部出站网络请求，并结合静态规则与 `LLM-as-judge` 对请求是否符合策略做裁决。

## 关键要点

- 不依赖特定 SDK、模型供应商或工具协议，核心控制点是网络出口而不是单个工具调用

- 通过 `HTTP_PROXY` / `HTTPS_PROXY` 接管请求路径，并可配合 iptables 强制 Agent 只能经由代理出网

- 对高频确定性流量使用静态规则，对长尾请求使用自然语言策略 + LLM 裁决

- 内置 policy builder 与历史流量回放评测，使策略可以从真实流量中归纳并在上线前验证

- 它同时也是审计与观测层，可帮助发现无效调用、权限过宽和工具设计噪音

## 来源引用

- [摘要：CrabTrap: an LLM-as-a-judge HTTP proxy to secure agents in production](summaries/摘要：CrabTrap- an LLM-as-a-judge HTTP proxy to secure agents in production.md)（[原文](https://x.com/pedroh96/status/2046604993982009825)）

## 关联概念

- [LLM-as-judge](concepts/LLM-as-judge.md)

- [Agent Harness](concepts/Agent Harness.md)

- [OpenClaw](entities/OpenClaw.md)
