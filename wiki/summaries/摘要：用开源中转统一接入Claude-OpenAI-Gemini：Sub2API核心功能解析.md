---
title: 摘要：用开源中转统一接入Claude/OpenAI/Gemini：Sub2API核心功能解析
type: summary
tags:
- 商业/生态
status: 已审核
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: https://www.notion.so/346701074b688125bcf0cb1e68040d65
notion_url: https://www.notion.so/Tizer/b064198052a64026b3b990d54ed8e85a
notion_id: b0641980-52a6-4026-b3b9-90d54ed8e85a
---

## 一句话摘要

Sub2API 是一个面向 Claude、OpenAI、Gemini 等服务的开源统一中转层，试图把账号接入、密钥分发、计费、调度、并发与支付能力收敛到同一套可运营后台中。

## 关键洞察

- 它解决的不是单一模型接入问题，而是多服务、多账号、多密钥带来的工程碎片化。

- 文章强调 Token 级精确计费、粘性会话、并发控制与速率限制，说明其定位更接近“可运营的 API 基础设施”。

- 内置 EasyPay、支付宝、微信与 Stripe，意味着它不仅适合个人自用，也瞄准团队分发和商业化场景。

- 支持一键脚本、Docker Compose 与源码编译，技术栈为 Go + Vue 3 + PostgreSQL + Redis，部署路径比较完整。

- 当前覆盖 Claude、OpenAI、Gemini、Antigravity、Codex，Sora 暂不可用。

## 提取的概念

- [Sub2API](entities/Sub2API.md)

- [API Key 分发](concepts/API Key 分发.md)

- [Token 级精确计费](concepts/Token 级精确计费.md)

- [智能调度](concepts/智能调度.md)

- [粘性会话](concepts/粘性会话.md)

- [并发控制](concepts/并发控制.md)

- [速率限制](concepts/速率限制.md)

- [AI 支付集成](concepts/AI 支付集成.md)

## 原始文章信息

- 作者：小华同学ai

- 来源：微信

- 发布时间：2026-04-18 18:34

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=Mzk0MjcxOTM2Nw%3D%3D&mid=2247502925&idx=1&sn=c5f44b38c0c75259cd2c498915216ee2&chksm=c299a356e1d1244e5ffda156d54336f50b545a4015f3df40854f080b1caedf90457af895153b#rd)

## 个人评注

这类“中转 + 调度 + 计费 + 支付”的组合，对 Tizer 的内容与工具工作流有启发：如果后续要统一多模型调用、内部工具权限和成本归因，Sub2API 这类方案更像基础设施层，而不是单点工具。
