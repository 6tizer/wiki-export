---
title: Laguna M.1
type: entity
tags:
- 代码生成
- 模型部署
- 商业/生态
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3a59618fe7eb4b6a8f1b609c133b4571
notion_id: 3a59618f-e7eb-4b6a-8f1b-609c133b4571
---

## 定义

Laguna M.1 是 Poolside 的旗舰编码 Agent 模型，采用 225B 总参数 / 23B 激活参数的 MoE 架构，专为复杂软件工程任务和 agentic coding 长时域工作流设计。支持 128K 上下文窗口和最多 8K 输出 token，FP8 量化推理。

**别名**：poolside/laguna-m.1

## 关键要点

- **架构**：225B MoE，每 token 激活 23B 参数，兼顾性能与推理效率

- **定位**：Poolside 最强模型，面向 agentic coding 和长时域任务

- **许可协议**：需遵守 Poolside End User License Agreement（非 Apache 2.0，区别于 Laguna XS.2）

- **能力**：工具调用 + 推理能力，128K 上下文窗口

- **分发渠道**：首发于 OpenRouter（限时免费），同步支持 Baseten

- **社区评价**：被认为在编码基准上可与 Claude Sonnet 4.6 竞争

## 与 Laguna XS.2 的区别

- M.1 是旗舰大模型（225B/23B），XS.2 是轻量高效模型（33B/3B）

- XS.2 采用 Apache 2.0 开源，M.1 使用 Poolside EULA

- XS.2 可单 GPU 运行，M.1 需要更多算力

## 来源引用

- [摘要：The first public foundation models from @poolsideai just dropped on OpenRouter!](summaries/摘要：The first public foundation models from @poolsideai just dropped on OpenRouter!.md)（[原文](https://x.com/OpenRouter/status/2049145538373947541)）

## 关联概念

- [Laguna XS.2](entities/Laguna XS.2.md)

- [Poolside](entities/Poolside.md)

- [OpenRouter](entities/OpenRouter.md)

- [Agentic Coding](concepts/Agentic Coding.md)
