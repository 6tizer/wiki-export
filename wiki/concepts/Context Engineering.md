---
title: Context Engineering
type: concept
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/93e2a94f25804bffb88cda69cf6e2e95
notion_id: 93e2a94f-2580-4bff-b88c-da69cf6e2e95
---

## 定义

Context Engineering（上下文工程）是由 Anthropic 于 2025 年正式提出的概念，核心观点是：与其让用户手动写 prompt 来控制 AI，不如**系统性地管理 AI 在每次交互中能「看到」的信息**——让失忆的强力同事每次坐下来时，桌上已经摆好了所有需要的材料。

## 关键要点

- 需要管理的「材料」包括：项目架构和技术栈（Memory Bank）、当前任务需求（Delta Spec）、相关模块代码、历史经验记录、团队编码规范

- 与 SDD 的区别：SDD 解决「这一次怎么跟 AI 说清楚」，Context Engineering 解决「怎么让 AI 每次都自动拿到对的信息」

- 被比喻为「内功」，而具体的 SDD 框架是「招式」

- 是从 Vibe Coding 到系统化 AI 协作的关键进化方向

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Prompt Engineering](concepts/Prompt Engineering.md)

- [Agent Skills](concepts/Agent Skills.md)

- [OpenClaw](entities/OpenClaw.md)

- [显式外部状态](concepts/显式外部状态.md)

- [Thought Signatures](concepts/Thought Signatures.md)

- [三省六部式多 Agent 架构](concepts/三省六部式多 Agent 架构.md)

- [AI Knowledge Layer](concepts/AI Knowledge Layer.md)

- [Knowledge Base Layer](concepts/Knowledge Base Layer.md)

- [Brand Foundation](concepts/Brand Foundation.md)

- [llm-wikid](entities/llm-wikid.md)

- [Agent Loop](concepts/Agent Loop.md)

- [Tool Calling](concepts/Tool Calling.md)

- [Agent Loop](concepts/Agent Loop.md)

- [工具描述](concepts/工具描述.md)

- [上下文窗口](concepts/上下文窗口.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

- [前馈控制](concepts/前馈控制.md)

- [反馈控制](concepts/反馈控制.md)

- [GSD](entities/GSD.md)

- [Spec-driven 开发](concepts/Spec-driven 开发.md)

- [Prompt Thinning](concepts/Prompt Thinning.md)

- [记忆后端](concepts/记忆后端.md)

- [上下文基底](concepts/上下文基底.md)

- [ALIVE](entities/ALIVE.md)

- [Agent 持续学习三层框架](concepts/Agent 持续学习三层框架.md)

- [Agent Traces](concepts/Agent Traces.md)

- [上下文压缩](concepts/上下文压缩.md)

- [Schema 校验](concepts/Schema 校验.md)

- [独立 Evaluator](concepts/独立 Evaluator.md)

- [局部失败恢复](concepts/局部失败恢复.md)

- [Claude Code](entities/Claude Code.md)

- [InsForge](entities/InsForge.md)

- [Supabase](entities/Supabase.md)

- [Backend Context Engineering](concepts/Backend Context Engineering.md)

- [Progressive Disclosure](concepts/Progressive Disclosure.md)

- [叶子节点策略](concepts/叶子节点策略.md)

- [可验证性设计](concepts/可验证性设计.md)

## 来源引用

- [摘要：别问 Claude 能为你做什么，问你能为 Claude 做什么：Anthropic 内部的 Vibe Coding 方法论](summaries/摘要：别问 Claude 能为你做什么，问你能为 Claude 做什么：Anthropic 内部的 Vibe Coding 方法论.md)（[原文](https://x.com/GoSailGlobal/status/2046785975582667071)）

- [摘要：汤道生：人工智能正式进入 Harness 时代](summaries/摘要：汤道生：人工智能正式进入 Harness 时代.md)

- [摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？](summaries/摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？.md)

- [摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析](summaries/摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析.md) — 介绍 Context Engineering 的定义和与 SDD 的关系

- [原文链接](https://x.com/maid_crypto/status/2031315920875041121)｜《Harness Engineering：当 AI Agent 遇上七十年前的控制论》｜来源条目：Harness Engineering：当 AI Agent 遇上七十年前的控制论

- [摘要：三省六部幻觉：为什么“虚拟公司”式多Agent架构在工程上不成立](summaries/摘要：三省六部幻觉：为什么“虚拟公司”式多Agent架构在工程上不成立.md)

- [摘要：AI Knowledge Layer (and why your agents are useless without it)](summaries/摘要：AI Knowledge Layer (and why your agents are useless without it).md)

- 《Chat Bot 加一个循环，就进化成了 Agent》｜X书签文章｜原文链接：[https://x.com/LawrenceW_Zen/status/2042236281988812919](https://x.com/LawrenceW_Zen/status/2042236281988812919)｜来源条目：[摘要：Chat Bot 加一个循环，就进化成了 Agent](summaries/摘要：Chat Bot 加一个循环，就进化成了 Agent.md)

- [原文链接](https://x.com/LawrenceW_Zen/status/2043580374501249175)｜《While 循环谁都会写，上下文工程才是真功夫》｜来源条目：[摘要：While 循环谁都会写，上下文工程才是真功夫](summaries/摘要：While 循环谁都会写，上下文工程才是真功夫.md)

- [原文链接](https://x.com/Khazix0918/status/2044258725536690270)｜《一文带你看懂，火爆全网的Harness Engineering到底是个啥。》｜来源条目：[摘要：一文带你看懂，火爆全网的Harness Engineering到底是个啥。](summaries/摘要：一文带你看懂，火爆全网的Harness Engineering到底是个啥。.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0MjcxOTM2Nw%3D%3D&mid=2247502908&idx=1&sn=781cf89e36526cf2ced56337406ae43c&chksm=c2ee5c17dbde042bf7dbe3e5b84da84512262606a3d3b9259740ab2613aab4fcde99397b23c2#rd)｜《GSD框架解析：解决AI编程工具Context Rot的工程化方案》｜源文章：GSD框架解析：解决AI编程工具Context Rot的工程化方案

- [原文链接](https://x.com/witcheer/status/2044456778843238689)｜《I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.》｜来源条目：摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.

- 摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.（[原文](https://x.com/witcheer/status/2044456778843238689)）

- [原文链接](https://blog.ltbase.dev/posts/agents/harness-engineering.html)｜《模型不是笨，是 Harness 没配好》｜来源条目：[摘要：模型不是笨，是 Harness 没配好](summaries/摘要：模型不是笨，是 Harness 没配好.md)

- [摘要：How to cut Claude Code costs by 3x (using Karpathy's context engineering principles)](summaries/摘要：How to cut Claude Code costs by 3x (using Karpathy's context engineering principles).md)（[原文](https://x.com/_avichawla/status/2046500537584218438)）

- [摘要：Keep your Claude Code context clean with Subagents](summaries/摘要：Keep your Claude Code context clean with Subagents.md)（[原文](https://x.com/dani_avila7/status/2048486242321662189)）

- [摘要：Karpathy AI Ascent 2026：从 Vibe Coding 到 Agentic Engineering](summaries/摘要：Karpathy AI Ascent 2026：从 Vibe Coding 到 Agentic Engineering.md)（[原文](https://x.com/Av1dlive/status/2049561210593685876)）
