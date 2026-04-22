---
title: 摘要：Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强
type: summary
tags:
- Agent 编排
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: Agent, LLM, 自动化
source_article_url: https://www.notion.so/33f701074b68812cb2b1e4129d7d85c6
notion_url: https://www.notion.so/41fb2ff28f9045e3b458c497dbbeb4b8
notion_id: 41fb2ff2-8f90-45e3-b458-c497dbbeb4b8
---

## 一句话摘要

Better-Harness 把 Evals 当成 Agent 系统的反馈信号，通过持续优化 Harness 而不是频繁换模型，来系统性提升 Coding Agent 的表现与泛化能力。

## 关键洞察

- LangChain 用 **Agent = Model + Harness** 解释了为什么相同模型也会出现巨大性能差距。

- Evals 在这里扮演接近“梯度信号”的角色，用来暴露失败模式并指导下一轮优化。

- Optimization Set 与 Holdout Set 的拆分，是防止 Harness 过拟合已知任务的关键。

- 优化重点不只是 prompt，还包括工具描述、自我验证循环与上下文工程。

## 提取的概念

- [Better-Harness](entities/Better-Harness.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Evals](concepts/Evals.md)

- [Holdout Set](concepts/Holdout Set.md)

- [Terminal Bench 2](entities/Terminal Bench 2.md)

## 原始文章信息

- 作者：@berryxia

- 来源：X书签

- 发布时间：2026-04-09

- 链接：[https://x.com/berryxia/status/2042367800338260467](https://x.com/berryxia/status/2042367800338260467)

## 个人评注

这篇文章对 Tizer 的启发很直接：文章编译 Agent 的上限不只取决于模型，更取决于评测集、失败样本回放和编译流程本身。与其一味换模型，不如把“摘要是否忠实、概念是否去重、链接是否完整”做成可反复跑的 eval 闭环。
