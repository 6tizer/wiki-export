---
title: Future AGI
type: entity
tags:
- 模型评测
- Agent 安全
- AI 产品
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7440e59f95de4fdea3d4f39579cb9380
notion_id: 7440e59f-95de-4fde-a3d4-f39579cb9380
---

## 定义

Future AGI 是一个开源的 AI Agent 全生命周期管理平台，提供从追踪、评估、模拟、护栏到优化的一体化闭环能力。项目采用 Apache 2.0 许可，支持完全自托管部署。

**别名**：future-agi

## 关键要点

- **六大支柱**：Simulate（多轮对话模拟）、Evaluate（50+ 评估指标）、Protect（18 内建扫描器 + 15 供应商适配器）、Monitor（OTel 追踪，50+ 框架）、Gateway（100+ 提供商，15 种路由策略）、Optimize（6 种提示优化算法）

- **性能基准**：Gateway 单节点 ~29k req/s，P99 延迟 ≤ 21ms（含 guardrails）

- **核心差异**：不仅做可观测性，还闭合反馈回路实现 Agent 自改进

- **框架集成**：支持 LangChain、LlamaIndex、CrewAI、DSPy、AutoGen、PydanticAI 等 50+ 框架

- **部署方式**：Cloud（SOC 2 Type II、HIPAA）、Docker、Kubernetes、Air-gapped 本地部署

- **仅需 3 行代码即可接入**现有 Agent

## 档案

- **类型**：开源平台

- **许可证**：Apache 2.0

- **GitHub**：[future-agi/future-agi](https://github.com/future-agi/future-agi)

- **Cloud**：[app.futureagi.com](http://app.futureagi.com/)

- **合规**：SOC 2 Type II、HIPAA

## 关联概念

- [Agent 可观测性](concepts/Agent 可观测性.md)

- [GEPA](concepts/GEPA.md)

- [Agent 模拟测试](concepts/Agent 模拟测试.md)

- [Agent Gateway](concepts/Agent Gateway.md)

- [Guardrails](concepts/Guardrails.md)

## 来源引用

- [摘要：Goodbye agents that silently hallucinate in production.](summaries/摘要：Goodbye agents that silently hallucinate in production.md)（[X Thread](https://x.com/hasantoxr/status/2047636566680760576)）
