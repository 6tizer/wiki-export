---
title: Contextbase
type: concept
tags:
- 上下文管理
- 长期记忆
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2196020793f04aa7a345e3428bbe101a
notion_id: 21960207-93f0-4aa7-a345-e3428bbe101a
---

## 定义

Contextbase 是 Applied Compute 提出的概念，指由 AC Context Engine 持续编译而成的企业级知识库。它将企业内部文档、工单历史、agent 运行轨迹等非结构化数据提炼为结构化的事实和操作流程，形成一个「活的知识体」。Agent 在执行任务时通过 API 按需检索 Contextbase，而非每次从头理解企业环境。

## 关键要点

- 核心思路：将推理时的上下文负担转移到离线编译阶段

- 持续更新：专职 agent 不断合并新数据，提取事实，解决冲突

- 效果：挂载后可在不降低准确率的前提下大幅降低推理预算（低推理档即可达中推理档水平）

- 可类比为企业级 agent 的「长期记忆」或「机构知识」

## 来源引用

- [摘要：Applied Compute 发布 AC Context Engine 企业 agent 上下文引擎](summaries/摘要：Applied Compute 发布 AC Context Engine 企业 agent 上下文引擎.md)（[原文](https://x.com/0xLogicrw/status/2050436151757165031)）
