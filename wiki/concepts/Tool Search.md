---
title: Tool Search
type: concept
tags:
- Agent 技能
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/55dd0ea251c04f56af408054843230a1
notion_id: 55dd0ea2-51c0-4f56-af40-8054843230a1
---

## 定义

Tool Search 是一种按任务意图在运行时检索并加载相关工具定义的机制，用来避免在一次任务开始时把所有工具说明一次性塞进模型上下文。

## 关键要点

- 它把“全量暴露工具”改成“按需加载工具”，核心目标是压缩无效 token 消耗。

- 它更强调按用户意图、任务动作或工作流阶段组织工具，而不是机械按 API 端点展开。

- 在 MCP 或大型工具集场景里，Tool Search 可以显著缓解 schema 膨胀问题。

- 这类机制的价值不只是省 token，还能提升工具选择质量与多工具系统的可维护性。

## 来源引用

- [摘要：Anthropic 最新博客：MCP 没死，它又来了](summaries/摘要：Anthropic 最新博客：MCP 没死，它又来了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453483055&idx=1&sn=aca9f531006d4ae5c50feb6d4cc5229e&chksm=86732b338b1b484418b20621dcb0a955f7260a88990b6194acc039e8dc4969bb5bf99c3b9f8e#rd)）

## 关联概念

- [MCP 协议](concepts/MCP 协议.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Anthropic](entities/Anthropic.md)

- [Claude Cowork](entities/Claude Cowork.md)
