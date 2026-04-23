---
title: 摘要：Foundry Hosted Agents：每个 Agent 都需要自己的“电脑”
type: summary
tags:
- Agent 框架
- 安全/隐私
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881919824d12de1181605
notion_url: https://www.notion.so/8536787cd82d4420ab2a42c89fd9f2b5
notion_id: 8536787c-d82d-4420-ab2a-42c89fd9f2b5
---

## 一句话摘要

微软在 Foundry 中推出 Hosted agents，核心不是再造一个 Agent 框架，而是把 **独立沙箱、持久状态、身份与治理** 这些原本零散拼装的运行时能力，打包成面向企业级 Agent 的基础设施底座。

## 关键洞察

- **“每个 Agent 一台电脑”本质上是在重新定义 Agent 的运行时单元**：不是共享工具调用，而是给每个 Agent 一个独立、可隔离、可治理的执行环境。

- **持久状态是长时任务能否落地的分水岭**：没有状态保留，Agent 很难稳定完成跨步骤、跨会话的编码、运维与研究任务。

- **身份与治理被提升为基础设施能力**：当 Agent 开始长期运行并触达企业系统时，身份、权限边界与审计链路不能再依赖临时补丁。

- **云厂商竞争点正在从“能不能跑 Agent”转向“能不能托管 Agent 运行时”**：隔离、可恢复性、审计、可扩展性正在成为新的平台能力。

- **这类托管运行时会推动多 Agent 系统从 demo 走向生产**：因为真正阻碍上线的往往不是模型，而是状态管理、权限控制与环境隔离。

## 提取的概念

- [Foundry Agent Service](entities/Foundry Agent Service.md)

- [AI 沙箱](concepts/AI 沙箱.md)

- [持久状态](concepts/持久状态.md)

- [Agent 身份基础设施](concepts/Agent 身份基础设施.md)

## 原始文章信息

- 作者：@satyanadella

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[https://x.com/satyanadella/status/2047033636923568440](https://x.com/satyanadella/status/2047033636923568440)

- 源文章页面：微软 Foundry Hosted Agents：每个 AI Agent 都有自己的「专属电脑」

## 个人评注

这条信息对 Tizer 的工作流价值很高，因为它把 Agent 的竞争焦点从“提示词和编排”推进到了 **运行时基础设施**。对 OpenClaw、HITL 和内容流水线而言，未来真正可规模化的，不只是更聪明的 Agent，而是具备边界、记忆、身份和可审计性的 Agent 执行环境。
