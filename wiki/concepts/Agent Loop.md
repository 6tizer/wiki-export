---
title: Agent Loop
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2996f64eed314ac9a42ed2213d9b2a45
notion_id: 2996f64e-ed31-4ac9-a42e-d2213d9b2a45
---

## 定义

Agent Loop 是让 LLM 在“思考 → 请求工具 → 接收结果 → 再次决策”之间持续循环，直到任务完成的执行框架，是 Chat Bot 升级为 Agent 的最小骨架。

## 关键要点

- 本质上是一个持续运行的 while 循环，而不是复杂神秘的框架

- LLM 负责判断下一步要回复用户还是调用工具，执行器负责真正跑工具并回填结果

- 只有把工具结果重新塞回上下文，模型才能继续做条件判断和多步推进

- Agent 的自主性并不来自模型“会执行”，而来自循环让模型可以连续决策

## 关联概念

- [Prompt Engineering](concepts/Prompt Engineering.md)

- [Context Engineering](concepts/Context Engineering.md)

- [工具描述](concepts/工具描述.md)

- [上下文窗口](concepts/上下文窗口.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

- Agent Teams

- [Verification Loop](concepts/Verification Loop.md)

- [四步 PRD 对齐法](concepts/四步 PRD 对齐法.md)

- [内核可编程性](concepts/内核可编程性.md)

- [OpenCode](entities/OpenCode.md)

- [Claude Agent SDK](entities/Claude Agent SDK.md)

- [Codex](entities/Codex.md)

- [GenericAgent](entities/GenericAgent.md)

- [最小原子工具集](concepts/最小原子工具集.md)

## 来源引用

- [摘要：刚刚！Generic Agent 中文教程发布！比Hermes省10倍Token](summaries/摘要：刚刚！Generic Agent 中文教程发布！比Hermes省10倍Token.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722227&idx=1&sn=91cdeb9ed199ea27bf816d8f58822044&chksm=e9e6f905566630299ab381060e0037338ce5baf7cf72c2c15b502fae874a19d1aaf2acb5d20c#rd)）

- [摘要：Chat Bot 加一个循环，就进化成了 Agent](summaries/摘要：Chat Bot 加一个循环，就进化成了 Agent.md)｜X书签文章｜原文链接：[https://x.com/LawrenceW_Zen/status/2042236281988812919](https://x.com/LawrenceW_Zen/status/2042236281988812919)｜源文章：Chat Bot 加一个循环，就进化成了 Agent

- [原文链接](https://x.com/LawrenceW_Zen/status/2043580374501249175)｜《While 循环谁都会写，上下文工程才是真功夫》｜来源条目：[摘要：While 循环谁都会写，上下文工程才是真功夫](summaries/摘要：While 循环谁都会写，上下文工程才是真功夫.md)

- [原文链接](https://x.com/hylarucoder/status/2044041420475138514)｜《继续分享一些 harness engineering 实际经验》｜来源条目：[摘要：继续分享一些 harness engineering 实际经验](summaries/摘要：继续分享一些 harness engineering 实际经验.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzY0MDAzNzk3MA%3D%3D&mid=2247484430&idx=1&sn=a8cd136df0161ab4a5fe53b3a6a65990&chksm=f1c76fc519e5fdfca727bfdba977647d756e2865da0de591baae80902002af1c8c1d324b1a9e#rd)｜《136K Stars 的 OpenCode 凭什么碾压 Claude Code SDK？TUI 界面都能被插件替换，Claude Code 一个像素都动不了》｜来源条目：[摘要：136K Stars 的 OpenCode 凭什么碾压 Claude Code SDK？TUI 界面都能被插件替换，Claude Code 一个像素都动不了](summaries/摘要：136K Stars 的 OpenCode 凭什么碾压 Claude Code SDK？TUI 界面都能被插件替换，Claude Code 一个像素都动不了.md)
