---
title: 摘要：DeepSeek-V4 Preview 正式发布并开源，开启低成本百万上下文时代
type: summary
tags:
- 模型部署
- AI 产品
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b688112a194dd0ce2da9473
notion_url: https://www.notion.so/Tizer/511b09d43deb4d1eb572b6b4a0f11ec7
notion_id: 511b09d4-3deb-4d1e-b572-b6b4a0f11ec7
---

## 一句话摘要

DeepSeek 正式发布并开源 V4 系列模型（V4-Pro 1.6T/49B、V4-Flash 284B/13B），以极低成本提供 1M 上下文窗口，性能对标顶级闭源模型。

## 关键洞察

- **V4-Pro（1.6T/49B 激活）** 性能对标世界顶级闭源模型，在编码和 Agent 任务上与 Claude Sonnet 4.5 和 Opus 4.6 竞争

- **V4-Flash（284B/13B 激活）** 定位快速、高效、经济的日常选择

- **1M 上下文窗口** 成为全线标配，基于 DeepSeek Sparse Attention（DSA）机制大幅降低内存和计算成本

- **开源开放权重**：模型权重完全开源，API 定价约为 Claude 的 1/17（输入）到 1/50（输出），极大降低生产环境使用门槛

- 社区评价：50k token 文档处理成本仅 $0.12（Claude 需 $8+），开源模型在生产环境中成为默认选择的拐点

## 提取的概念

- [DeepSeek V4](entities/DeepSeek V4.md)

- [MoE 架构](concepts/MoE 架构.md)

- [DeepSeek Sparse Attention](concepts/DeepSeek Sparse Attention.md)

## 原始文章信息

- **作者**：@deepseek_ai

- **来源**：X（Twitter）

- **发布时间**：2026-04-24

- **原文链接**：[https://x.com/deepseek_ai/status/2047516922263285776](https://x.com/deepseek_ai/status/2047516922263285776)

- **技术报告**：[HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf)

- **模型权重**：[HuggingFace Collection](https://huggingface.co/collections/deepseek-ai/deepseek-v4)

## 个人评注

DeepSeek V4 的开源策略对 OpenClaw 生态直接利好——1M 上下文 + 极低 API 成本意味着 Agent 长会话和大代码库处理不再需要复杂的 RAG 架构。社区中已有用户报告在 OpenClaw 中使用 V4 进行 Agent 任务，尤其是多文件重构场景表现出色。V4-Flash 的 13B 激活参数也为端侧部署和自托管提供了更大可能。
