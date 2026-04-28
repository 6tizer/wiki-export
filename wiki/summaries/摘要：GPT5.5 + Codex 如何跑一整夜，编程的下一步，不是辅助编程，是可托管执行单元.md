---
title: 摘要：GPT5.5 + Codex 如何跑一整夜，编程的下一步，不是辅助编程，是可托管执行单元
type: summary
tags:
- Harness 工程
- 代码生成
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/350701074b68815cade6c41921c060e0
notion_url: https://www.notion.so/Tizer/0c9b2478aa08443ba8bd7cdc0c236405
notion_id: 0c9b2478-aa08-443b-a8bd-7cdc0c236405
---

## 一句话摘要

GPT-5.5 + Codex 标志着 AI 编程从「辅助编程」进入「可托管执行单元」时代——核心不再是模型智能，而是能否让 Agent 连续跑数小时后交付可验收的结果，以及围绕长跑构建的治理基础设施（状态机、证据链、熔断器、恢复包）。

## 关键洞察

- **从辅助到托管的范式转变**：GPT-5.5 在 Codex 中的核心变化不是「更聪明」而是「更能被托管」——能自主规划、执行、验证、迭代，连续运行数小时完成闭环（build → visual review → build more）

- **长跑不靠 prompt 靠工程**：OpenAI 官方 25 小时实验表明，支撑长跑的不是一句神奇 prompt，而是四个 Markdown 文件（[Prompt.md](http://prompt.md/)、[Plan.md](http://plan.md/)、[Implement.md](http://implement.md/)、[Documentation.md](http://documentation.md/)）构成的项目记忆和验收标准

- **社区长跑工作流涌现**：oh-my-codex（workflow layer + persistent completion loop）、superpowers（agentic skills framework + subagent-driven-development）、gsd-2（spec-driven development）、ProofLoop（define done → sleep → wake to verified results）等项目都在给模型外面加流程

- **长跑的真正瓶颈是治理而非智能**：用户反馈 Codex 长跑中频繁需要人工 approval、卡在长驻进程、Extra High reasoning 反而过于谨慎不敢推进等问题，说明越长跑越像状态机、权限、恢复和审计系统

- **人类角色演变**：高级人类从「逐行指导者」变成「经理 + 架构师 + 验收者」的混合体，如 OpenAI 的 Noam Brown 所言——manager 用了 GPT-5.5 后比任何时候都更像一个有效 IC

## 提取的概念

- [Agentic Coding](concepts/Agentic Coding.md)

- [Codex](entities/Codex.md)

- [可托管执行单元](concepts/可托管执行单元.md)

- [oh-my-codex](entities/oh-my-codex.md)

- [superpowers 框架](entities/superpowers 框架.md)

- [Codex Memories](concepts/Codex Memories.md)

## 原始文章信息

- **作者**：AI进修生

- **来源**：微信公众号

- **发布时间**：2026-04-27

- **原文链接**：[GPT5.5 + Codex 如何跑一整夜](https://mp.weixin.qq.com/s?__biz=MzkyMzY1NTM0Mw%3D%3D&mid=2247515158&idx=1&sn=a656396814f65b8053981d852d11bb54&chksm=c0ba44de9a9054cf724edaed2a5cda4d44ea80568c1c43a3b3d2de3699534f4295bfaf69ba91#rd)

## 个人评注

这篇文章的核心论点与 Tizer 的 OpenClaw Harness 工程方向高度契合：Agent 长跑需要的不是更聪明的模型，而是更完善的执行环境——状态机、熔断器、恢复包、人类审阅点。文中提到的四个 Markdown 文件（[Prompt.md](http://prompt.md/) / [Plan.md](http://plan.md/) / [Implement.md](http://implement.md/) / [Documentation.md](http://documentation.md/)）本质上就是一套轻量级 Harness 协议，可以参考用于 OpenClaw 的任务托管机制设计。社区涌现的 oh-my-codex、superpowers 等项目也印证了 Harness 层是 Agentic Coding 的下一个核心战场。
