---
title: 摘要：Today we're releasing Laguna XS.2, Poolside's first open-weight model.
type: summary
tags:
- 代码生成
- 模型部署
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b688169ace1fa0bb866d663
notion_url: https://www.notion.so/Tizer/43df6443c9db4e0ea0c2d495ef06a261
notion_id: 43df6443-c9db-4e0e-a0c2-d495ef06a261
---

## 一句话摘要

Poolside 发布首个开源权重模型 Laguna XS.2——33B 总参数 / 3B 激活参数的 MoE 编码模型，专为 agentic coding 和长时域任务设计，单 GPU 可运行，Apache 2.0 开源。

## 关键洞察

- **极致效率的 MoE 架构**：33B 总参数但每 token 仅激活 3B，配合 Sliding Window Attention 和 FP8 KV Cache，实现单 GPU 本地运行，大幅降低 Agent 工作流的基础设施成本

- **全栈自研训练管线**：预训练（30T tokens，Muon 优化器）→ 后训练 → Agent RL 三阶段流水线，其中 Agent RL 采用异步离策略架构在真实代码沙箱中训练

- **Data Automixing 创新**：通过 surrogate regressors 拟合数据集比例与下游评估的关系，自动化大规模预训练的数据配比优化

- **开源 + 生态首日覆盖**：Apache 2.0 开源权重，首日支持 Transformers、vLLM、TRT-LLM、MLX、Ollama，并在 OpenRouter 和 Baseten 上线

- **双产品入口**：同步发布 pool（终端轻量 coding agent CLI）和 Shimmer（云端 Agent 开发环境），共享同一 agent harness（ACP 环境）

## 提取的概念

- [Laguna XS.2](entities/Laguna XS.2.md)

- [Poolside](entities/Poolside.md)

- [Agent RL](concepts/Agent RL.md)

- [Data Automixing](concepts/Data Automixing.md)

- [Shimmer](entities/Shimmer.md)

## 原始文章信息

- **作者**：@poolsideai

- **来源**：X 书签

- **发布时间**：2026-04-28

- **原文链接**：[https://x.com/poolsideai/status/2049144111626670282](https://x.com/poolsideai/status/2049144111626670282)

- **博客详情**：[Laguna XS.2 and M.1: A Deeper Dive](https://poolside.ai/blog/laguna-a-deeper-dive)

## 个人评注

- **与 OpenClaw 的关联**：Poolside 的 agent harness 思路与 OpenClaw 的执行环境设计有相似之处——都强调在沙箱中让 Agent 执行真实任务并从结果中学习。Laguna XS.2 的 Agent RL 训练方式可作为 OpenClaw 未来 RL 训练策略的参考

- **本地部署价值**：3B 激活参数 + 单 GPU 运行 = 可集成到 HITL 内容管线中作为本地 coding agent，避免 API 调用成本

- **MoE 小模型趋势**：继 DeepSeek 之后又一个证明 MoE 在小参数激活量级也能实现强 agentic 能力的案例，值得在内容管线工具选型中关注
