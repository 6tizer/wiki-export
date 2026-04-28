---
title: Token Performance Network
type: concept
tags:
- LLM
- 开发工具
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6369c2ccb54e45d39835797b45e56721
notion_id: 6369c2cc-b54e-45d3-9835-797b45e56721
---

## 定义

Token Performance Network（TPN）是一种围绕 Token 产能与推理体验来设计和评估网络系统的基础设施思路，强调网络不再只服务带宽和链路指标，而要直接服务模型推理与 Agent 运行效率。

## 关键要点

- 以 Token 为统一度量单位，把网络优化目标与推理业务目标对齐。

- 关注超低时延、稳定吞吐与单位 Token 成本，而不只是传统网络性能参数。

- 适用于长时运行的 Agent 场景，因为多轮推理会放大单次延迟的影响。

- 体现出 AI Infra 从“训练优先”转向“推理优先、成本敏感”的演进。

## 来源引用

- [摘要：为了Token，阿里云竟然出了一个TPN？](summaries/摘要：为了Token，阿里云竟然出了一个TPN？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU1OTEwNDkwNw%3D%3D&mid=2247492725&idx=1&sn=05da9c55729b14a97d8fcbec7cadd3e2&chksm=fd6c11ebba90a0d90aec3ff46f46b00aea99a3b1e55e81bd81355a80b9e0f62dd360b6371d40#rd)）
