---
title: 摘要：Hi, I'm RC. I previously built Kimi CLI at Moonshot AI.
type: summary
tags:
- Agent 协作模式
- AI 产品
status: 已审核
confidence: medium
last_compiled: '2026-04-28'
source_tags: Agent, LLM, Cursor, OpenClaw, 自动化, Crypto
source_article_url: https://www.notion.so/34f701074b6881c299cbf139689897c7
notion_url: https://www.notion.so/Tizer/33130dc067b74aea8a43d89b92e14e55
notion_id: 33130dc0-67b7-4aea-8a43-d89b92e14e55
---

## 一句话摘要

Slock 创始人 RC（前月之暗面 Kimi CLI 开发者）发布 Slock 平台大量新功能更新，展示了一个以 IM 界面为核心的 Human-Agent 协作平台的产品形态和社区反馈。

## 关键洞察

- Slock 定位为「Agent-first 协作平台」，借鉴 Slack/Discord 的频道+DM 界面，让人和 Agent 以队友身份协作，而非传统的工具调用模式

- 新功能包括搜索、线程收件箱、消息收藏、消息永久链接、置顶聊天、服务器邀请链接、统一配色系统等，功能迭代速度快

- Agent 运行在用户本地机器上（daemon 架构，与 OpenClaw 类似），平台本身负责消息路由和 UI 协作层

- 社区关注的核心问题集中在：安全/隐私模型（daemon 权限过高）、移动端支持、定时任务、多 runtime 切换、Hermes/OpenClaw 集成

- RC 建议团队角色配置：几个工程师 + 设计师 + PM + CEO 助理，不需要过长的 agent description，依赖外部记忆积累

## 提取的概念

- [Slock](entities/Slock.md)

- [Kimi CLI](entities/Kimi CLI.md)

- [Human-Agent 协作平台](concepts/Human-Agent 协作平台.md)

## 原始文章信息

- **作者**：@istdrc（RC，前月之暗面 Kimi CLI 开发者，Slock/botiverse 创始人）

- **来源**：X 书签

- **发布时间**：2026-04-05

- **链接**：[原文推文](https://x.com/istdrc/status/2040862482622026076)

## 个人评注

Slock 是 Human-Agent 协作平台赛道的典型代表，与 OpenClaw 在架构上有相似之处（本地 daemon + 远程消息路由），但 Slock 更侧重团队协作和 IM 体验。社区对安全模型和权限控制的担忧值得关注——这正是 Harness 工程中需要解决的信任边界问题。对 Tizer 的内容自动化流水线而言，Slock 的「多 Agent 协作 + 外部记忆」设计思路可以作为组织 Agent 协作模式的参考。
