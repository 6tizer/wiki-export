---
title: Agent Traces
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/43fe87516eb0469d8a5367fe4cd16dc2
notion_id: 43fe8751-6eb0-469d-8a53-67fe4cd16dc2
---

## 定义

Agent Traces 指 Agent 执行过程中沉淀的输入、工具调用、中间状态、输出结果、评分与人工反馈等可复盘记录，是模型学习、Harness 优化与 Context 整理共享的数据燃料。

## 关键要点

- traces 既是故障诊断材料，也是后续评测、训练和经验提取的数据来源

- 高质量 traces 需要覆盖任务输入、工具调用、关键状态、结果与人工反馈

- 在 Harness 优化里，完整 traces 往往比压缩摘要更有诊断价值

- 在 Context learning 里，traces 可以被整理成记忆、技能或团队规则

- 如果缺少 traces，所谓持续学习很容易退化成拍脑袋改 prompt

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Meta-Harness](concepts/Meta-Harness.md)

- [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [Agent Handoff](concepts/Agent Handoff.md)

- [会话记忆](concepts/会话记忆.md)

- [Sandbox Agents](concepts/Sandbox Agents.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523832&idx=1&sn=8a7013894ddc0668c0f1c9f935599450&chksm=c1b17f5bd2d0ca49ee848d1dc13c14fb122c8f551ba00b307b566dfa7edc4c20a52573051f79#rd)｜《字节最火的开源Agent项目，如何思考Agent的自我进化？》｜来源文章：字节最火的开源Agent项目，如何思考Agent的自我进化？

- [摘要：OpenAI Agents SDK：三个原语，搭出你的多 Agent 系统](summaries/摘要：OpenAI Agents SDK：三个原语，搭出你的多 Agent 系统.md)（[原文](https://x.com/_vmlops/status/2045533747857240290)）
