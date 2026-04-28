---
title: andrej-karpathy-skills
type: entity
tags:
- 代码生成
- 提示工程
- IDE 集成
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2ef12e54151f4b3ab38e4f1445bdc5dd
notion_id: 2ef12e54-151f-4b3a-b38e-4f1445bdc5dd
---

## 定义

**andrej-karpathy-skills** 是一个开源 Claude Code 插件（GitHub: [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)），由开发者 forrestchang 根据 AI 大神 Andrej Karpathy 对 LLM 编程陷阱的观察整理而成，通过一个 `CLAUDE.md` 文件将四条编程原则强制注入 Claude Code 的行为准则。

## 核心原则

1. **思考先行（Think Before Coding）**：明确假设、展示权衡、困惑时主动提问而非猜测

1. **简洁至上（Simplicity First）**：用最少代码解决问题，不过度设计，不添加未被要求的"灵活性"

1. **精准改动（Surgical Changes）**：只改必须改的，不"顺便"重构无关代码，每行改动可追溯到用户需求

1. **目标驱动（Goal-Driven Execution）**：将命令式任务转化为可验证的成功标准，LLM 循环执行直到满足标准

## 使用方式

- **插件方式**：在 Claude Code 中通过 `/plugin install andrej-karpathy-skills@karpathy-skills` 安装

- [**CLAUDE.md**](http://claude.md/)** 方式**：直接下载 `CLAUDE.md` 文件放入项目根目录，按项目生效

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [claude-mem](entities/claude-mem.md)

- [Evolver](entities/Evolver.md)

- [GenericAgent](entities/GenericAgent.md)

- [Claude Code](entities/Claude Code.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [Think Before Coding](concepts/Think Before Coding.md)

- [Simplicity First](concepts/Simplicity First.md)

- [Surgical Changes](concepts/Surgical Changes.md)

- [Goal-Driven Execution](concepts/Goal-Driven Execution.md)

## 来源引用

- [摘要：The Ultimate Open-Source Dev Stack](summaries/摘要：The Ultimate Open-Source Dev Stack.md)（[原文](https://x.com/AlphaSignalAI/status/2047014600713842728)）

- [摘要：TOP FIVE GITHUB REPOSITORIES THIS WEEK](summaries/摘要：TOP FIVE GITHUB REPOSITORIES THIS WEEK.md)（[原文](https://x.com/RoundtableSpace/status/2045906520672461309)）

- [摘要：11.4K Star！基于 AI 大神 Karpathy 的编程经验开源的 Claude Code 技能插件。](summaries/摘要：11.4K Star！基于 AI 大神 Karpathy 的编程经验开源的 Claude Code 技能插件。.md)（开源星探，2026-04-11）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzU3NTg5MjU1Mw%3D%3D&mid=2247496984&idx=1&sn=98f3a18047c1908f1b961052640e85a9&chksm=fc1c6bb03b47cbb0ba7d773e7d7e2f214a2492c4f081e9d9750d237912643aabf4e8b6628c58#rd)｜《一个 [CLAUDE.md](http://claude.md/) 文件竟然拿下 1.7 万 star，它到底写了什么》｜来源条目：[摘要：一个 CLAUDE.md 文件竟然拿下 1.7 万 star，它到底写了什么](summaries/摘要：一个 CLAUDE.md 文件竟然拿下 1.7 万 star，它到底写了什么.md)

- [原文链接](https://x.com/axiaisacat/status/2044260023161831620)｜《Looking for a managed agents platform?》｜来源条目：[摘要：Looking for a managed agents platform?](summaries/摘要：Looking for a managed agents platform.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI0ODk2NDIyMQ%3D%3D&mid=2247502836&idx=1&sn=bc1037b3490abbe4c22277672f9f0191&chksm=e86fcdd39fd3d2961bc8025efd7d093f04b7608ae7887433e37539f88532a95a6bfee7812824#rd)｜《就一个 skills，凭啥 4w Star？》｜来源条目：[摘要：就一个 skills，凭啥 4w Star？](summaries/摘要：就一个 skills，凭啥 4w Star？.md)
