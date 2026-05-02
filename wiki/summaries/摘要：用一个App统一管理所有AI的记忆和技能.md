---
title: 摘要：用一个App统一管理所有AI的记忆和技能
type: summary
tags:
- 多Agent协作
- 长期记忆
- CLI 工具
status: 已审核
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: https://www.notion.so/354701074b688167a775f8861f89bc7e
notion_url: https://www.notion.so/Tizer/67a62b5bd2dc4fe4b1fca13081ea8cbc
notion_id: 67a62b5b-d2dc-4fe4-b1fc-a13081ea8cbc
---

## 一句话摘要

Clawdi 是一个开源的跨框架 AI 智能体统一管理平台，将分散在 OpenClaw、Claude Code、Hermes、Codex 等不同框架中的记忆、会话和技能集中打通，实现跨设备跨框架共享同步。

## 关键洞察

- **跨框架记忆共享**：解决多 AI 工具并行使用时记忆/技能/API 密钥割裂的痛点，切换框架无需从零配置

- **500+ 应用集成**：覆盖 Gmail、Slack、Notion、HubSpot 等主流工具，还支持浏览器自动化和多渠道消息（Telegram、WhatsApp）

- **社区技能市场**：用户可共享和安装预制技能，类似插件商店模式

- **TEE 加密执行**：云端托管版（Clawdi Cloud）采用可信执行环境保障安全，提供 24/7 托管服务

- **BYOA 模式**：除原生支持的框架外，允许接入任意自定义 Agent 框架，避免厂商锁定

## 提取的概念

- [Clawdi](entities/Clawdi.md)（entity）：跨框架 AI 智能体管理平台

- [TEE 可信执行环境](concepts/TEE 可信执行环境.md)（concept）：云端版采用的安全机制

- [BYOA 模式](concepts/BYOA 模式.md)（concept）：自带 Agent 框架接入模式

## 原始文章信息

- **作者**：成天放屁

- **来源**：微信公众号

- **发布时间**：2026-05-02

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzI5MTEwMDgyMA%3D%3D&mid=2247484252&idx=1&sn=170e13385d8b9279d9635415b3bd4c1e&chksm=ed55f24b6cf7d8cdcffcb566a0fea0d5c7099bfd12cda305d4304211ada2618d72fd82c575d7#rd)

## 个人评注

这类「统一管理层」产品对 Tizer 的多 Agent 工作流有直接参考价值。当前 OpenClaw 生态中记忆和技能的跨实例共享仍是痛点，Clawdi 的 BYOA + 统一记忆层思路值得关注——如果能与 OpenClaw 的 Dreaming 记忆机制对接，可能实现更完整的上下文持久化方案。另外社区技能市场的模式也与 OpenClaw Skills 生态有交叉，可关注其社区运营策略。
