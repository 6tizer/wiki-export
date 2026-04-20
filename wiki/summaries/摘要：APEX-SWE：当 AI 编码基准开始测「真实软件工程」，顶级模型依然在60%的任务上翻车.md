---
title: 摘要：APEX-SWE：当 AI 编码基准开始测「真实软件工程」，顶级模型依然在60%的任务上翻车
type: summary
tags:
- Coding Agent
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: LLM, Claude, GitHub, 开源
source_article_url: https://www.notion.so/348701074b6881bcbb99dc4bae132087
notion_url: https://www.notion.so/fa4e2356a3344a8e9c6475a70ed31918
notion_id: fa4e2356-a334-4a8e-9c64-75a70ed31918
---

## 一句话摘要

APEX-SWE 试图把 AI 编码能力评测从“会不会补代码”推进到“能不能完成真实软件工程交付”，而最新结果显示即使顶级模型在这类任务上的一次通过率仍只有四成左右。

## 关键洞察

- 传统基准如 HumanEval 与 SWE-bench 已出现不同程度的饱和与污染风险，越来越难准确反映前沿模型的真实工程能力。

- APEX-SWE 将任务拆为集成任务与可观测性任务，强调跨系统协作、工具调用、日志排障与生产环境推理，更接近真实开发场景。

- Claude Opus 4.7 在 Integration 维度排名第一，但总榜仍以 41.3% 略低于 GPT-5.3 Codex 的 41.5%，说明顶级模型距离稳定完成真实工程交付还有明显差距。

- 该基准目前只有 50 个任务，样本规模较小、配置公平性也存在争议，因此更适合作为方向性信号，而非终局裁判。

- 评测框架开源且支持多家模型提供商，意味着团队可以把它当作内部模型选型与回归测试的参考框架。

## 提取的概念

- [APEX-SWE](concepts/APEX-SWE.md)

- [SWE-bench](concepts/SWE-bench.md)

- [SWE-bench Pro](concepts/SWE-bench Pro.md)

- [HumanEval](concepts/HumanEval.md)

- [ARC-AGI-2](concepts/ARC-AGI-2.md)

- [Mercor](entities/Mercor.md)

## 原始文章信息

- 作者：@mercor_ai

- 来源：X书签

- 发布时间：2026-04-17

- 原文链接：[https://x.com/mercor_ai/status/2045254642385510894](https://x.com/mercor_ai/status/2045254642385510894)

## 个人评注

这篇材料对 Tizer 的意义，不在于某个模型暂时排第几，而在于它提醒我们：评估 Coding Agent 不能只看 demo 与函数级 benchmark，更要看跨工具链集成、环境操作、日志排障和端到端交付。像 APEX-SWE 这样的基准，适合作为后续构建内部评测流水线、比较 Claude / Codex / 其他模型在真实工作流中稳定性的参考。
