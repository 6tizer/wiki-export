---
title: 摘要：等了五年，AI 终端 Warp 终于开源！OpenAI 赞助
type: summary
tags:
- CLI 工具
- 代码生成
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881ec8fd6ef3d21b6ae3c
notion_url: https://www.notion.so/Tizer/0958887420d446fab7d0749e019657b2
notion_id: 09588874-20d4-46fa-b7d0-749e019657b2
---

## 一句话摘要

Warp——用 Rust 编写的 AI 终端——在社区等待五年后正式开源（AGPL v3 + MIT 双许可），OpenAI 担任创始赞助商，开源首日 GitHub Stars 突破 35,000。

## 关键洞察

- **五年开源拉锯战**：2021 年社区在 GitHub discussion #400 请求开源，创始人 Zach Lloyd 因担心竞争对手 fork 商业版和「开源不可逆」而长期犹豫，直到 2026 年 4 月 28 日正式开源

- **开源时机的逻辑**：Lloyd 认为开发瓶颈已从「写代码」转移到「定义产品规格和验证行为」，AI Agent 使代码编写成本大幅降低，社区成员的想法可通过 prompting 直接变成原型

- **双许可策略**：主代码库 AGPL v3（防止闭源商业分发），UI 框架 WarpUI 用 MIT（允许社区自由复用），98% 代码为 Rust

- **Oz 云端 Agent 平台**：可同时运行 40 个并发 Agent，已在 Warp 内部编写 60% 的 PR，是社区贡献管理的核心基础设施

- **商业表现亮眼**：ARR 约 4800 万美元（同比增长 12 倍），近 100 万活跃开发者，累计融资 7300 万美元（Sequoia 领投），客户包括 OpenAI、Netflix、Salesforce

## 提取的概念

- [Warp](entities/Warp.md)

- [Oz](entities/Oz.md)

- [Open Agentic Development](concepts/Open Agentic Development.md)

- [Ghostty](entities/Ghostty.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

## 原始文章信息

- **作者**：AGI Hunt

- **来源**：微信公众号

- **发布时间**：2026-04-29

- **原文链接**：[微信文章](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453483197&idx=1&sn=c806fb90a6957dc03889b4e4f6353565&chksm=868e52b437295b86cd027481b982fc5bde25fabe57f952b8f9d155bae7e338a57d214c473c7b#rd)

## 个人评注

本文是目前对 Warp 开源事件最详尽的中文报道，涵盖创始人背景、五年社区博弈史、技术架构、Oz Agent 平台、商业数据和三款终端（iTerm2/Ghostty/Warp）对比。几个与 Tizer 工作流相关的观察：

1. **Open Agentic Development 范式**：用户提需求 → Agent 写原型 → 人工审核的循环，与 OpenClaw 的 HITL 理念高度一致。Warp 用 Oz 管理社区 PR 的做法，可作为 OpenClaw 开源社区治理的参考

1. **双许可策略**：AGPL + MIT 的组合保护核心代码同时释放 UI 框架，值得 OpenClaw 开源时借鉴

1. **终端对比视角**：文章对 iTerm2（瑞士军刀）、Ghostty（手术刀）、Warp（工具台）的定位比较有助于理解 CLI 工具的产品光谱
