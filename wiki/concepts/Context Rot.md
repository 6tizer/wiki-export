---
title: Context Rot
type: concept
tags:
- 上下文管理
- 长期记忆
- Harness 工程
status: 审核中
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/77c0aba021164affaef357668d5026ce
notion_id: 77c0aba0-2116-4aff-aef3-57668d5026ce
---

## 定义

Context Rot 指随着上下文不断累积，模型在长对话或长任务中出现推理质量衰减、注意力漂移和执行稳定性下降的现象。

## 关键要点

- 本质是上下文窗口稀缺资源被噪声侵蚀

- 需要通过压缩、卸载和结构化记忆管理来缓解

- 是长时程 Agent 设计必须正视的问题

## 来源引用

- [摘要：Resolvers: The Routing Table for Intelligence](summaries/摘要：Resolvers- The Routing Table for Intelligence.md)（[原文](https://x.com/garrytan/status/2044479509874020852)）

- [摘要：这样用 Opus 4.7，才能发挥实力](summaries/摘要：这样用 Opus 4.7，才能发挥实力.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247515662&idx=1&sn=bfcc64cdceb913aef59f697c1ecbfa8d&chksm=c3914681eabbc4c3c559e95297d8d5b85aebabf0c4c93a5d517e6784d086e7b7ff3aa9abee9e#rd)）

- [摘要：万字干货：理解 Harness Engineering，看这一篇就够了](summaries/摘要：万字干货：理解 Harness Engineering，看这一篇就够了.md)

- [摘要：把 Claude Code 源码蒸馏成 Agent Skill — Harness Engineering 实践](summaries/摘要：把 Claude Code 源码蒸馏成 Agent Skill — Harness Engineering 实践.md)

- [摘要：Harness Engineering：当 AI Agent 遇上七十年前的控制论](summaries/摘要：Harness Engineering：当 AI Agent 遇上七十年前的控制论.md)

- [摘要：The Definitive Guide to Harness Engineering](summaries/摘要：The Definitive Guide to Harness Engineering.md)

- [摘要：Harness Engineering：决定 AI Agent 能跑 10 分钟还是 10 小时的那层系统](summaries/摘要：Harness Engineering：决定 AI Agent 能跑 10 分钟还是 10 小时的那层系统.md)（[原文](https://x.com/shao__meng/status/2031532690034606549)｜X书签文章）

- [摘要：什么才是真正的 Harness Engineering？](summaries/摘要：什么才是真正的 Harness Engineering？.md)

- [摘要：继续分享一些 harness engineering 实际经验](summaries/摘要：继续分享一些 harness engineering 实际经验.md)

- [摘要：用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条](summaries/摘要：用半年 Claude Code 踩坑，我验证了 OpenAI-Cursor-Anthropic 三篇 Harness Engineering 的每一条.md)

- [摘要：一文带你看懂，火爆全网的Harness Engineering到底是个啥。](summaries/摘要：一文带你看懂，火爆全网的Harness Engineering到底是个啥。.md)

- [摘要：Ralph Loop：更轻量的 Harness Engineering 循环框架](summaries/摘要：Ralph Loop：更轻量的 Harness Engineering 循环框架.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ%3D%3D&mid=2461159297&idx=1&sn=e1d1550d8c29f6c57f344e9bd7619931&chksm=8645d4fd11f0bef28663c05083551df88d222c61fd3c8390df4b43f46267e00d6b3a54bcfe38#rd)｜[摘要：Harrison Chase：你的 Agent Harness 就是你的记忆，一旦选了闭源，数据就不是你的了](summaries/摘要：Harrison Chase：你的 Agent Harness 就是你的记忆，一旦选了闭源，数据就不是你的了.md)｜源文章：Harrison Chase：你的 Agent Harness 就是你的记忆，一旦选了闭源，数据就不是你的了

- [原文链接](https://x.com/trq212/status/2044548257058328723)｜《Using Claude Code: Session Management & 1M Context》｜来源条目：[摘要：Using Claude Code: Session Management & 1M Context](summaries/摘要：Using Claude Code- Session Management & 1M Context.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0MjcxOTM2Nw%3D%3D&mid=2247502908&idx=1&sn=781cf89e36526cf2ced56337406ae43c&chksm=c2ee5c17dbde042bf7dbe3e5b84da84512262606a3d3b9259740ab2613aab4fcde99397b23c2#rd)｜[摘要：GSD框架解析：解决AI编程工具Context Rot的工程化方案](summaries/摘要：GSD框架解析：解决AI编程工具Context Rot的工程化方案.md)｜源文章：GSD框架解析：解决AI编程工具Context Rot的工程化方案

- [原文链接](https://x.com/AYi_AInotes/status/2044625894556230013)｜《说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！》｜来源条目：[摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！](summaries/摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！.md)

- [摘要：A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all.](summaries/摘要：A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all.md)（[原文](https://x.com/augmentcode/status/2047164534310494709)）

- [摘要：开源「洁癖.Skill」，让你的Agent越用越聪明。](summaries/摘要：开源「洁癖.Skill」，让你的Agent越用越聪明。.md)（[原文](https://x.com/Khazix0918/status/2049345300939391245)）

- [摘要：How Hermes Agent Solves Skill Drift and Context Rot as a Self-Improving Agent](summaries/摘要：How Hermes Agent Solves Skill Drift and Context Rot as a Self-Improving Agent.md)（[原文](https://x.com/mem0ai/status/2050351798142288050)）

- [摘要：精读 Cursor《Continually improving our agent harness》：一个 agent 产品团队的工程方法论全景](summaries/摘要：精读 Cursor《Continually improving our agent harness》：一个 agent 产品团队的工程方法论全景.md)（[原文](https://x.com/elliotchen100/status/2050757239364002193)）

## 关联概念

- [Resolver](concepts/Resolver.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Rewind](concepts/Rewind.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Claude Code](entities/Claude Code.md)

- [GSD](entities/GSD.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Schema Drift Detection](concepts/Schema Drift Detection.md)

- [Scope Reduction Detection](concepts/Scope Reduction Detection.md)

- [Prompt Thinning](concepts/Prompt Thinning.md)

- [AGENTS.md](concepts/AGENTS.md.md)
