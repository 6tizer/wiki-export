---
title: AC Context Engine
type: entity
tags:
- 上下文管理
- RAG/检索
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6ea1721810cf4a5ba473448d355b9206
notion_id: 6ea17218-10cf-4a5b-a473-448d355b9206
---

## 定义

AC Context Engine 是 Applied Compute 发布的企业级 agent 上下文引擎。它将内部文档、工单历史、agent 运行轨迹等数据源持续编译为一个活的知识库 Contextbase，agent 执行任务时通过 API 按需检索，无需每次从头理解企业环境。

别名：Context Engine（Applied Compute 产品，区别于 OpenClaw Context Engine）

## 关键要点

- 对接 S3、Google Drive、GitHub 等数据源，也接收 agent 运行轨迹

- 一组专职 agent 持续合并新数据与已有知识库，提取事实和操作流程，解决冲突

- 挂载 Contextbase 后可显著降低推理预算：GPT-5.4 低推理档从 44.5% 提升至 52.4%（APEX-Agents 基准）

- 推理档位越低提升越大：低推理 +7.9%、中推理 +3.7%、极高推理反降 0.7%

- 中推理基线上 GPT-5.4 从 44.2% → 51.7%（相对 +16.9%），GPT-5.4-mini 从 33.4% → 38.7%（相对 +15.8%）

## 来源引用

- [摘要：Applied Compute 发布 AC Context Engine 企业 agent 上下文引擎](summaries/摘要：Applied Compute 发布 AC Context Engine 企业 agent 上下文引擎.md)（[原文](https://x.com/0xLogicrw/status/2050436151757165031)）
