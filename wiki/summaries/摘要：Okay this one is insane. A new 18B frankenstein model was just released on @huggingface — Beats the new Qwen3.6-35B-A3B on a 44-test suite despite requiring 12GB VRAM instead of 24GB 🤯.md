---
title: 摘要：Okay this one is insane. A new 18B frankenstein model was just released
  on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring
  12GB VRAM instead of 24GB 🤯
type: summary
tags:
- LLM
- Coding Agent
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b6881318cbcf5d3c1340309
notion_url: https://www.notion.so/181738b436da4e6aac963520f6cc1092
notion_id: 181738b4-36da-4e6a-ac96-3520f6cc1092
---

## 一句话摘要

这是一篇关于 **Qwopus-GLM-18B-Merged-GGUF** 的速报：它以 18B 合并模型、12GB VRAM 可运行和基准测试压过 Qwen3.6-35B-A3B 为卖点迅速走红，但社区实测也暴露出输出失真、循环思考等明显不稳定性。

## 关键洞察

- 这条信息最吸引人的点是 **18B 规模 + 12GB VRAM + 单张 RTX 3060 可跑**，把高性能本地模型的门槛继续往消费级硬件下拉

- 模型卖点来自 **把 Opus 4.6 与 GLM-5.1 的推理能力拼接进同一模型**，体现了模型合并路线在本地推理圈的吸引力

- 帖子强调它在 44 项测试里超过 Qwen3.6-35B-A3B，并兼顾 **tool calling** 与 **agentic reasoning**，说明目标并不只是聊天，而是本地 Agent 工作负载

- 但回复区很快出现大量负反馈，包括乱码、无意义输出、thinking loop 与上下文稳定性问题，作者本人也承认这是一个高度实验性的模型

- 因而这条信息更像是 **本地模型工程探索的风向标**，而不是已经可直接进入生产工作流的稳定答案

## 提取的概念

- [Qwopus-GLM-18B-Merged-GGUF](entities/Qwopus-GLM-18B-Merged-GGUF.md)

- [模型合并](concepts/模型合并.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [GGUF](concepts/GGUF.md)

- [Tool Calling](concepts/Tool Calling.md)

- [Agentic Reasoning](concepts/Agentic Reasoning.md)

## 原始文章信息

- 作者：@leftcurvedev_

- 来源：X书签

- 发布时间：2026/04/18

- 原文链接：[https://x.com/leftcurvedev_/status/2045449352827580602](https://x.com/leftcurvedev_/status/2045449352827580602)

## 个人评注

这条内容对 Tizer 的价值不在于“马上采用这个模型”，而在于它提醒我们：**消费级显卡上的本地 Agent 模型正在快速逼近可用阈值，但 benchmark 胜利不等于真实工作流稳定**。对于 OpenClaw、HITL 和内容生产链路而言，这类模型适合继续观察其工具调用、长上下文稳定性和本地部署成本，而不宜仅凭单条 benchmark 宣传就进入主流程。
