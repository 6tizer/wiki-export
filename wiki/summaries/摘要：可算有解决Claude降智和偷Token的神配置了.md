---
title: 摘要：可算有解决Claude降智和偷Token的神配置了
type: summary
tags:
- Coding Agent
- 工作流
status: 已审核
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881cbbc75e54aaa9a8315
notion_url: https://www.notion.so/7a7b10306f4247c29891642cb2ec266c
notion_id: 7a7b1030-6f42-47c2-9891-642cb2ec266c
---

## 一句话摘要

这篇文章围绕 Claude Code 在实际使用中的“降智”和 Token 消耗问题，整理出一套以固定思考档位、关闭自适应思考、控制上下文窗口和利用缓存为核心的调优思路。

## 关键洞察

- 通过在 `~/.claude/settings.json` 中固定 `effortLevel`、关闭自适应思考并设置 `MAX_THINKING_TOKENS`，可以减少模型动态降档带来的不稳定感

- 关闭 1M 上下文并尽早触发上下文压缩，核心目标是用更可控的上下文规模换取更稳定的性能与成本

- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` 可能会缩短缓存有效期，导致长对话反而更耗额度

- 节省 Token 不只是靠配置，还包括使用习惯优化，例如任务未切换且缓存未过期时避免频繁新开对话

- 可用读改比、思考深度和中断频率等观测指标判断 Claude Code 是否出现明显降质

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [自适应思考](concepts/自适应思考.md)

- [思考预算](concepts/思考预算.md)

- [上下文压缩](concepts/上下文压缩.md)

- [提示词缓存](concepts/提示词缓存.md)

- [读改比](concepts/读改比.md)

- [思考深度](concepts/思考深度.md)

## 原始文章信息

- 作者：卡尔的AI沃茨

- 来源：微信

- 发布时间：2026-04-16T00:23:00.000+08:00

- 原文链接：[微信文章](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247506380&idx=1&sn=61a5e32ac2ce7477db9d8a1c3dce0f0d&chksm=cfe3fce924f5a8acb06b6a4eedb9d5a179eb1b89f9c1bb98dbba32ad1a0562593dec78b87ee4#rd)

## 个人评注

- 对 Tizer 的启发是，编程 Agent 进入稳定生产后，配置治理、缓存策略和上下文压缩要和工作流设计一起看，不能只盯模型本身

- 如果后续要在 OpenClaw 或内容流水线里引入长时运行的 Coding Agent，这篇文章提供了一个“性能观测 + 成本控制 + 使用习惯”三位一体的调优框架
