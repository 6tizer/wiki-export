---
title: 摘要：Opus 4.7 is the first model that punishes bad prompting. here's how to correct
  it. (FULL GUIDE)
type: summary
tags:
- Coding Agent
- LLM
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: LLM, Claude, 提示词, Prompt工程
source_article_url: https://www.notion.so/348701074b6881fc9c44e4b65a80b8ce
notion_url: https://www.notion.so/a993347f2138481ab9ca4301d9b23ed5
notion_id: a993347f-2138-481a-b9ca-4301d9b23ed5
---

## 一句话摘要

Claude Opus 4.7 并不是对 4.6 的线性升级，而是通过移除采样兜底、改为自适应思考、默认提高 effort 等机制，把模糊提示词的成本直接转化为更高的费用与更不稳定的输出。

## 关键洞察

- 4.7 禁用了 temperature、top_p、top_k 等常见采样调节手段，过去用参数去“缝补”模糊提示词的做法在这一代模型上直接失效。

- 扩展思考预算被自适应思考取代后，模型会在提示不清时自行消耗更多推理资源，模糊性被直接计入成本。

- Claude Code 在 4.7 上把默认 effort 抬到 xhigh，使得含糊任务的基础开销进一步上升。

- task budget 与更字面化的指令遵循一起，迫使用户在目标、约束、停止条件和成功标准上写得更明确，否则预算会先耗在“猜意图”上。

- 文章的核心判断是：4.7 实际上重定价了 prompting 习惯，受益者将是目标清晰、约束明确、能写结构化提示的人。

## 提取的概念

- [Claude Opus 4.7](entities/Claude Opus 4.7.md)

- [自适应思考](concepts/自适应思考.md)

- [任务预算](concepts/任务预算.md)

- [指令遵循](concepts/指令遵循.md)

- [歧义税](concepts/歧义税.md)

## 原始文章信息

- 作者：@the_smart_ape

- 来源：X书签

- 发布时间：2026-04-17

- 原文链接：[https://x.com/the_smart_ape/status/2045070676063649908](https://x.com/the_smart_ape/status/2045070676063649908)

## 个人评注

这篇文章对 Tizer 的工作流很有参考价值：如果后续要把 Claude Opus 4.7 接进内容编译、Agent 批处理或 Coding Agent 链路，prompt 需要前置写清任务边界、输出格式、预算和停止条件，否则成本会上升而且结果更不稳定。
