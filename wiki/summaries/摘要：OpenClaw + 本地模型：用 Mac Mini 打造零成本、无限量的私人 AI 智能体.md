---
title: 摘要：OpenClaw + 本地模型：用 Mac Mini 打造零成本、无限量的私人 AI 智能体
type: summary
tags:
- OpenClaw
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, LLM, Agent, 自动化
source_article_url: ''
notion_url: https://www.notion.so/518c22574da54f70b93f32a05257d932
notion_id: 518c2257-4da5-4f70-b93f-32a05257d932
---

## 一句话摘要

用 Qwen 3.5 + LM Studio 在 Mac Mini 上跑本地模型，配合「混合模型策略」可将 OpenClaw 的 API 账单降低约 90%，同时保留前沿智能的规划能力。

## 关键洞察

- **Qwen3.5-35B-A3B** 4-bit 量化后约 20GB，可跑在 32GB Mac Mini 上，性能对标 6-12 个月前的 Claude Sonnet

- **混合模型策略**：前沿模型做规划（10% 消耗），本地模型做执行（90% 消耗），账单降至 1/10

- Alex Finn 案例：3 台 Mac Studio 跑 Qwen 3.5 驱动完整 SaaS 工厂，月费从几千美元降至仅电费

- 本地模型工具推荐：LM Studio（图形界面，Mac 首选）、Ollama（命令行，开发者首选）

- 已知问题：模型切换丢失上下文、工具调用不稳定、首次响应慢（M4 32GB 测试"hello"耗时 2 分钟）

## 提取的概念

Qwen 3.5 · [LM Studio](entities/LM Studio.md) · [混合模型策略](concepts/混合模型策略.md) · [OpenClaw](entities/OpenClaw.md)

## 原始文章信息

- **作者**：Alex Finn

- **来源**：X书签

- **链接**：[https://x.com/AlexFinn/status/2027096146661998662](https://x.com/AlexFinn/status/2027096146661998662)

## 个人评注

混合模型策略对 Tizer 的 OpenClaw 工作流极具参考价值——将高频执行任务（如内容 pipeline 的格式化、批处理）迁移至本地 Qwen 3.5，可大幅降低 API 成本。Mac Mini 硬件门槛低，值得实验。
