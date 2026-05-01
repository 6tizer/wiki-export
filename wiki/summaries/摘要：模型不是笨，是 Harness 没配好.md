---
title: 摘要：模型不是笨，是 Harness 没配好
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881e185a2e15fde44545c
notion_url: https://www.notion.so/Tizer/7cfc66cb5f224215840c19da521d8af8
notion_id: 7cfc66cb-5f22-4215-840c-19da521d8af8
---

## 一句话摘要

这篇文章提出 **Harness Engineering** 的核心判断：多步 Agent 之所以经常中途崩溃，问题通常不在模型本身，而在于缺少对输出、状态、验收与故障恢复的系统级约束。

## 关键洞察

- Agent 从 Prompt Engineering、Context Engineering 进一步演进到 Harness Engineering，重点从“怎么问”与“喂什么”转向“如何把系统拴牢”。

- 文章给出四个最关键的工程支点：**Schema 校验**、**显式外部状态**、**独立 Evaluator**、**局部失败恢复**。

- 当上下文占用过高时，模型会出现“上下文焦虑症”，表现为跳步、敷衍收尾、输出质量突然下降，因此需要 **上下文压缩** 与干净实例重启机制。

- 真正可靠的验收不能依赖模型自评，而要依赖可执行检查，例如测试、编译、页面渲染结果或结构化验证。

- 一个一天内可落地的最小 Harness，就已经能显著提升长任务成功率：状态文件、重试机制、结构校验、工具返回截断。

## 提取的概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [Context Engineering](concepts/Context Engineering.md)

- [上下文压缩](concepts/上下文压缩.md)

- [显式外部状态](concepts/显式外部状态.md)

- [Schema 校验](concepts/Schema 校验.md)

- [独立 Evaluator](concepts/独立 Evaluator.md)

- [局部失败恢复](concepts/局部失败恢复.md)

## 原始文章信息

- 作者：@dotey

- 来源：X书签

- 发布时间：2026-04-16

- 源页面：Harness Engineering：让 AI 智能体不再翻车的工程方法论

- 推文链接：[https://x.com/dotey/status/2044660793153655205](https://x.com/dotey/status/2044660793153655205)

- 原文链接：[https://blog.ltbase.dev/posts/agents/harness-engineering.html](https://blog.ltbase.dev/posts/agents/harness-engineering.html)

## 个人评注

这篇文章和 Tizer 当前的工作流高度相关。对于 OpenClaw、HITL 和内容编译流水线来说，真正影响稳定性的往往不是模型智力，而是任务状态是否外置、关键输出是否可验证、失败是否可以局部恢复。把这些约束补齐，往往比继续堆 Prompt 更直接。
