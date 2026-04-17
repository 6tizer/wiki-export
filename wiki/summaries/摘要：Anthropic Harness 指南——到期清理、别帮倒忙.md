---
title: 摘要：Anthropic Harness 指南——到期清理、别帮倒忙
type: summary
tags:
- 工作流
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/0a1aad4eaac84846bf991737efd65db4
notion_id: 0a1aad4e-aac8-4846-bf99-1737efd65db4
---

**一句话摘要**：Anthropic Harness 架构应该带着到期日，随模型能力提升定期审查并拆除已成为 dead weight 的脚手架，让 Claude 自己做它能做的事。

**关键洞察**

- **核心观点**：Harness 编码的是「Claude 自己做不到什么」的假设，但这些假设会随 Claude 变强而过时

- **三条原则**：用 Claude 已经会用的工具（bash + 文本编辑器）；定期问自己「能停掉什么」；必要的边界还是要设

- **Dead Weight 案例**：Opus 4.6 上线后，为 Sonnet 4.5 “上下文焦虑”而搭建的 context 重置机制成了没用的屌车，拆掉后成本省 37%

- **渐进式推露**：Skill YAML 头部预加载小量 token，Claude 连同去取全文（不需要事先把所有指令全部塞入 system prompt）

- **Subagent 实效**：Opus 4.6 用 subagent 在 BrowseComp 上再多 2.8%；self-managed compaction Opus 4.6 达 84%

**提取的概念**

- Harness 工程

- Dead Weight 原则

- 渐进式推露（progressive disclosure）

**原始文章信息**

- 作者：AGI Hunt

- 来源：微信公众号

- 发布时间：2026-04-04

- 链接：[https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ==&mid=2453482336](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453482336)

**个人评注**：与 Tizer 的 HITL + OpenClaw 工作流直接相关。Dead Weight 原则可直接用于审查现有 OpenClaw Harness，判断哪些组件已随模型升级而变得冗余。Build to delete。
