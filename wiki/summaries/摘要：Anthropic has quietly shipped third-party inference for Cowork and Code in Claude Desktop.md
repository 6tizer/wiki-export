---
title: 摘要：Anthropic has quietly shipped third-party inference for Cowork and Code
  in Claude Desktop.
type: summary
tags:
- Coding Agent
- 商业/生态
status: 已审核
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881b6ad3bfbec9aeb0236
notion_url: https://www.notion.so/416f089fef374024abfaa48faa73622a
notion_id: 416f089f-ef37-4024-abfa-a48faa73622a
---

## 一句话摘要

Anthropic 正在把 Claude Desktop 悄悄推进到“前端体验与推理后端解耦”的新阶段：Cowork 和 Code 已可在第三方推理模式下接入 OpenRouter、LiteLLM 乃至本地模型。

## 关键洞察

- 入口位于 Claude Desktop 的 Developer 配置中，当前更像灰度放量或 A/B 测试，而不是已经全面公开的正式发布。

- 第三方推理并不只是“换模型”，而是把 Cowork / Code 的 agent 体验与具体推理提供方拆开，让 Anthropic 的产品层与外部模型层分离。

- 实测信息显示 OpenRouter 可直接作为 gateway 接入，LiteLLM 也可作为代理桥接本地模型或其他上游服务。

- 官方文档表明，这套模式主要面向企业合规、数据驻留与安全管控场景，但个人用户已经能在部分环境中提前体验。

- 一旦推理后端可插拔，Anthropic 的竞争重点就会更偏向桌面体验、技能/插件体系、工具链和工作流编排，而不只是模型独占。

## 提取的概念

- [Claude Cowork](entities/Claude Cowork.md)

- [Claude Code](entities/Claude Code.md)

- [OpenRouter](entities/OpenRouter.md)

- [LiteLLM](entities/LiteLLM.md)

- [第三方推理](concepts/第三方推理.md)

- [AI 模型网关](concepts/AI 模型网关.md)

## 原始文章信息

- 作者：@PawelHuryn

- 来源：X书签 / X 线程

- 发布时间：2026-04-22

- 原文链接：[https://x.com/PawelHuryn/status/2047039360856387944](https://x.com/PawelHuryn/status/2047039360856387944)

## 个人评注

- 对 Tizer 的工作流很有启发：前端可以继续使用 Anthropic 的 agent 交互与工具链，后端则保留 OpenRouter、网关代理和本地模型的弹性，这更适合做成本、可用性与合规之间的动态权衡。
