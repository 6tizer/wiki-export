---
title: '摘要：CrabTrap: an LLM-as-a-judge HTTP proxy to secure agents in production'
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b68810c8a1bd0f45c6a63e8
notion_url: https://www.notion.so/Tizer/234b53ba20df4e46a56b842eb1b910cf
notion_id: 234b53ba-20df-4e46-a56b-842eb1b910cf
---

## 一句话摘要

CrabTrap 通过在传输层拦截 AI Agent 的全部 HTTP/HTTPS 出站请求，并用“静态规则 + LLM-as-judge”双阶段裁决，把原本分散在工具、模型和人工审批里的安全控制收束成一层可审计、可回放、可迭代的生产级代理安全基础设施。

## 关键洞察

- 通过设置 `HTTP_PROXY` 和 `HTTPS_PROXY`，CrabTrap 能在不改 SDK、框架或工具协议的前提下接管 Agent 的所有出站网络请求。

- 安全判定采用两阶段：高频、确定性的请求走静态规则；长尾、模糊请求交给 LLM-as-judge 做策略裁决。

- 团队不是先凭空写策略，而是先观察历史流量，再让 policy builder 从真实调用样本中归纳自然语言策略。

- 在策略正式生效前，可以用历史审计日志做回放评测，提前看到新旧策略的放行/拒绝差异。

- CrabTrap 不只是拦截器，也是观测层：请求日志会暴露 Agent 的无效调用、噪音请求和权限设计缺陷，反过来帮助收缩工具面。

## 提取的概念

- [CrabTrap](entities/CrabTrap.md)

- [LLM-as-judge](concepts/LLM-as-judge.md)

- [Agent Harness](concepts/Agent Harness.md)

- [TLS 拦截](concepts/TLS 拦截.md)

- [流量归纳策略](concepts/流量归纳策略.md)

- [策略回放评测](concepts/策略回放评测.md)

## 原始文章信息

- 作者：@pedroh96

- 来源：X书签

- 发布时间：2026-04-21

- 原文链接：[https://x.com/pedroh96/status/2046604993982009825](https://x.com/pedroh96/status/2046604993982009825)

- 源文章页面：CrabTrap：用 LLM 当裁判，给 AI Agent 的 HTTP 流量上一把锁

## 个人评注

这篇文章很适合作为 Tizer 工作流里的“Agent 生产安全层”样板：如果 OpenClaw/Harness 类系统开始触达真实 API、OAuth、社媒账号或资金操作，仅靠 prompt 约束、tool scope 或零散审批并不够，还需要独立的网络出口控制、审计回放与策略迭代闭环。

CrabTrap 给出的启发是：把“安全策略”从单个 Agent 内部逻辑里抽出来，做成一层可观测、可调优、可逐步收紧的基础设施；但它的边界也很清楚——响应侧内容、WebSocket 等通道以及代理本身的信任集中问题，仍需要和 HITL、最小权限、沙箱一起配合。
