---
title: 摘要：OpenAI 刚发的 Workspace Agent，开源版来了
type: summary
tags:
- 多Agent协作
- Harness 工程
status: 已审核
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68812490affbe5b0209f5d
notion_url: https://www.notion.so/Tizer/79ab023452d34cbc9e40d52f7c891ba5
notion_id: 79ab0234-52d3-4cbc-9e40-d52f7c891ba5
---

## 一句话摘要

@stainlu 发布了 openclaw-managed-agents，一个开源自托管的 Workspace Agent 平台，支持任意模型后端、会话级 Docker 沙箱隔离、凭证隔离和子 Agent 全链路可观测。

## 关键洞察

- 该项目定位为 OpenAI Workspace Agents 的开源替代，核心卖点是模型无关（Claude / GPT / Gemini / Kimi / DeepSeek 均可接入），避免被单一供应商锁定

- 每个会话运行在独立 Docker 容器中，实现会话级沙箱隔离，一个崩溃不影响其他会话——这是多租户 Agent 系统的正确架构选择

- 凭证隔离确保每个终端用户的认证信息互不可见，适合 SaaS 多租户场景

- 子 Agent 调用全程可观测（不是黑盒），评论区指出这才是多 Agent 框架的真正难点——大多数框架只给输出不给 trace

- 采用了 Pi Pattern（由 @badlogicgames 提出），用于子 Agent 编排和可观测性

- 自带 Telegram 适配器，降低了搭建 Telegram/Discord AI 机器人的门槛

## 提取的概念

- [openclaw-managed-agents](entities/openclaw-managed-agents.md)

- [Workspace Agents](entities/Workspace Agents.md)

- [Agent 可观测性](concepts/Agent 可观测性.md)

## 原始文章信息

- 作者：@xiaohu（转发 @stainlu）

- 来源：X书签

- 发布时间：2026-04-24

- 原文链接：[查看原文](https://x.com/xiaohu/status/2047521587122106376)

- 项目地址：[GitHub](https://github.com/stainlu/openclaw-managed-agents)

## 个人评注

这个项目对 Tizer 的工作流有直接参考价值：它展示了如何将 Workspace Agent 模式从封闭平台解放出来，在自有基础设施上运行。会话级沙箱 + 凭证隔离 + 子 Agent 可观测的三件套，正是 OpenClaw 在企业化落地时需要补齐的能力。Pi Pattern 的采用也值得深入研究，看是否能应用到 OpenClaw 的多 Agent 协作链路中。
