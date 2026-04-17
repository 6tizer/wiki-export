---
title: Context Rot
type: concept
tags:
- 记忆系统
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/77c0aba021164affaef357668d5026ce
notion_id: 77c0aba0-2116-4aff-aef3-57668d5026ce
---

## 定义

Context Rot 指随着上下文不断累积，模型在长对话或长任务中出现推理质量衰减、注意力漂移和执行稳定性下降的现象。

## 关键要点

- 本质是上下文窗口稀缺资源被噪声侵蚀

- 需要通过压缩、卸载和结构化记忆管理来缓解

- 是长时程 Agent 设计必须正视的问题

## 来源引用

- 《Harness Engineering：决定 AI Agent 能跑 10 分钟还是 10 小时的那层系统》｜X书签文章｜原文链接：[https://x.com/shao__meng/status/2031532690034606549](https://x.com/shao__meng/status/2031532690034606549)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ%3D%3D&mid=2461159297&idx=1&sn=e1d1550d8c29f6c57f344e9bd7619931&chksm=8645d4fd11f0bef28663c05083551df88d222c61fd3c8390df4b43f46267e00d6b3a54bcfe38#rd)｜《Harrison Chase：你的 Agent Harness 就是你的记忆，一旦选了闭源，数据就不是你的了》｜源文章：Harrison Chase：你的 Agent Harness 就是你的记忆，一旦选了闭源，数据就不是你的了

- [原文链接](https://x.com/trq212/status/2044548257058328723)｜《Using Claude Code: Session Management & 1M Context》｜来源条目：[摘要：Using Claude Code: Session Management & 1M Context](summaries/摘要：Using Claude Code- Session Management & 1M Context.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0MjcxOTM2Nw%3D%3D&mid=2247502908&idx=1&sn=781cf89e36526cf2ced56337406ae43c&chksm=c2ee5c17dbde042bf7dbe3e5b84da84512262606a3d3b9259740ab2613aab4fcde99397b23c2#rd)｜《GSD框架解析：解决AI编程工具Context Rot的工程化方案》｜源文章：GSD框架解析：解决AI编程工具Context Rot的工程化方案

- [原文链接](https://x.com/AYi_AInotes/status/2044625894556230013)｜《说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！》｜来源条目：[摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！](summaries/摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！.md)

## 关联概念

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
