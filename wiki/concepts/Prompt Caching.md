---
title: Prompt Caching
type: concept
tags:
- 上下文管理
- 推理优化
status: 审核中
confidence: high
last_compiled: '2026-05-01'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f929311550e4404c85b3714806d540cb
notion_id: f9293115-50e4-404c-85b3-714806d540cb
---

## 定义

Prompt Caching 是通过复用对话前缀缓存来降低重复上下文成本、提升 Agent 交互效率的运行机制。

## 关键要点

- 对长上下文编程 Agent 的成本结构影响很大

- 前缀顺序稳定与静态内容固定是高命中率关键

- 会影响模型切换、工具顺序和系统提示设计

- 适合固定工作流中的重复提示场景

- 价值不只在节省 Token，也在于降低系统抖动

- 在 Agent 产品里，它常与结构化任务和长期运行场景一同出现

## 来源引用

- [摘要：深度使用半年，我总结了 Claude Code 的架构、治理与工程实践](summaries/摘要：深度使用半年，我总结了 Claude Code 的架构、治理与工程实践.md)｜X书签文章｜原文链接：[https://x.com/HiTw93/status/2032091246588518683](https://x.com/HiTw93/status/2032091246588518683)

- [摘要：Claude Code 的七层记忆体系：从亚毫秒级缓存到「梦境」式整合](summaries/摘要：Claude Code 的七层记忆体系：从亚毫秒级缓存到「梦境」式整合.md)（X书签文章，[原文](https://x.com/troyhua/status/2039052328070734102)）

- [原文链接](https://x.com/jxnlco/status/2044469127696556153)｜《Sandboxes are coming to the Agents SDK》｜源文章：OpenAI Agents SDK 沙盒：让 AI Agent 真正「留下工作成果」

- OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了（[原文](https://x.com/AYi_AInotes/status/2041021296377737696)）

- [摘要：可算有解决Claude降智和偷Token的神配置了](summaries/摘要：可算有解决Claude降智和偷Token的神配置了.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247506380&idx=1&sn=61a5e32ac2ce7477db9d8a1c3dce0f0d&chksm=cfe3fce924f5a8acb06b6a4eedb9d5a179eb1b89f9c1bb98dbba32ad1a0562593dec78b87ee4#rd)）

## 关联概念

- [In Distribution](concepts/In Distribution.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Sandbox Agents](concepts/Sandbox Agents.md)

- [Claude Code](entities/Claude Code.md)

- [上下文压缩](concepts/上下文压缩.md)

- [思考预算](concepts/思考预算.md)
