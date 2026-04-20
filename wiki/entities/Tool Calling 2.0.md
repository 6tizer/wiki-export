---
title: Tool Calling 2.0
type: entity
tags:
- LLM
- Agent 技能
status: 草稿
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0158c38ca6f14e6086ab57c982672b4c
notion_id: 0158c38c-a6f1-4e60-86ab-57c982672b4c
---

## 定义

Tool Calling 2.0 是 Anthropic 发布的一套重大工具调用更新，通过四大特性将 Agent 从「LLM as Router」推进到「LLM as Engine」，大幅降低 Token 消耗和延迟。

## 关键要点

- **Programmatic Tool Calling**：模型直接输出可执行代码（而非 JSON），在沙箱中用 for 循环和条件分支批量处理，减少 30%-50% Token

- **Dynamic Filtering**：在网页抓取和上下文之间插入代码过滤层，平均降低 24% Token

- **Tool Search**：延迟加载机制，只保留约 500 Token 的核心工具，其他按需加载，最高优化 80% 上下文

- **Tool Use Examples**：工具定义中加入 Few-Shot 示范，复杂参数准确率 72%→90%

- 安全挑战：代码执行沙箱隔离级别成为关键，调试难度呈指数级上升

## 来源引用

- [摘要：Anthropic Tool Calling 2.0——Agent 上下文消耗降80%](summaries/摘要：Anthropic Tool Calling 2.0——Agent 上下文消耗降80%.md)（[GoldenSpider.AI](http://goldenspider.ai/)，2026-02-27）— 从工程实操角度拆解四大特性

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw%3D%3D&mid=2247484183&idx=1&sn=19d63da8469d8144bc75d9b5d96eb2a5&chksm=cf51bf7f2bbc808c4595a0b312c5385bc05ec91b701c72f7c3c5849e96e54a8581348a50997b#rd)｜[摘要：Agent 的"手"长出来了，但为什么还是不可靠？](summaries/摘要：Agent 的手长出来了，但为什么还是不可靠？.md)

## 关联概念

- [MCP 协议](concepts/MCP 协议.md)

- [CLI-Anything](entities/CLI-Anything.md)

- [AutoSkill](concepts/AutoSkill.md)

- [SKILL.md](concepts/SKILL.md.md)
