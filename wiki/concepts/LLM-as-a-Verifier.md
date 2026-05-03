---
title: LLM-as-a-Verifier
type: concept
tags:
- Harness 工程
- 模型评测
- 推理优化
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3f2178dcdbe74939ae785fbfb825514b
notion_id: 3f2178dc-dbe7-4939-ae78-5fbfb825514b
---

## 定义

LLM-as-a-Verifier 是一种把大模型从“给整体印象分的裁判”转成“对候选轨迹逐项核验的验证器”的方法。它不只判断答案看起来像不像对，而是通过更细粒度的验证过程，从多次候选执行中筛出更可靠的结果。

## 关键要点

- 它解决的核心问题不是 Agent 完全不会做，而是 Agent 往往不知道哪一次尝试才是真的做对了。

- 相比 LLM-as-a-Judge 的粗粒度离散打分，这种方法更强调验证阶段的分布式、细粒度与可重复比较。

- 文章将 repeated verification、评分 token 粒度提升、评估标准分解视为三个关键扩展方向。

- 它适用于 Terminal-Bench、SWE-Bench Verified 一类长时序编程任务，也体现出与 Agent Harness 解耦的通用性。

## 来源引用

- [摘要：超越Claude Mythos和GPT-5.5！斯坦福推出Agent验证框架「LLM-as-a-Verifier」](summaries/摘要：超越Claude Mythos和GPT-5.5！斯坦福推出Agent验证框架「LLM-as-a-Verifier」.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651030107&idx=2&sn=dcf949e41eb246cd78463ec2ac79eb17&chksm=85f6580c4d8619e4dbb67c7144f147a8bc41f01f639924649cbbb134ea5daa9c1e2bdebb2928#rd)）

## 关联概念

- [LLM-as-judge](concepts/LLM-as-judge.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

- [SWE-Bench Verified](entities/SWE-Bench Verified.md)

- [验证计算扩展](concepts/验证计算扩展.md)

- [评估标准分解](concepts/评估标准分解.md)
