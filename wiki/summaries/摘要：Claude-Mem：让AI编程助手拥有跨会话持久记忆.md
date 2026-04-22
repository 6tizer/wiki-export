---
title: 摘要：Claude-Mem：让AI编程助手拥有跨会话持久记忆
type: summary
tags:
- 记忆系统
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b6881b7ad09e91f9c5da131
notion_url: https://www.notion.so/d0cfa90dccfb49c4b619b5b5cbebdd50
notion_id: d0cfa90d-ccfb-49c4-b619-b5b5cbebdd50
---

## 一句话摘要

claude-mem 通过生命周期 Hook 自动采集 Claude Code 会话中的工具调用、代码改动与决策过程，再借助 SQLite + Chroma 的混合检索与分层调用机制，把短暂对话沉淀为可跨会话复用的持久记忆。

## 关键洞察

- 它把 AI 编程助手的“失忆问题”拆成采集、压缩、存储、检索四个连续环节，形成完整闭环。

- Hook 机制是整个系统的入口：会话开始时注入历史记忆，工具调用后沉淀观察，会话结束时再压缩归档。

- SQLite FTS5 负责高效关键词检索，Chroma 负责语义检索，两者结合构成更稳健的混合检索层。

- `search → timeline → get_observations` 的三层检索工作流，本质上是一种渐进式披露策略：先粗筛，再补上下文，最后精读详情，显著节省 Token。

- 在此之上，Knowledge Corpus 进一步把“找回过去”扩展为“围绕一组历史记录做主题问答与知识复用”，让记忆系统开始具备知识库属性。

## 提取的概念

- [claude-mem](entities/claude-mem.md)

- [Claude Code](entities/Claude Code.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)

- [混合检索](concepts/混合检索.md)

- [ChromaDB](entities/ChromaDB.md)

- [渐进式披露](concepts/渐进式披露.md)

- [三层检索工作流](concepts/三层检索工作流.md)

## 原始文章信息

- 作者：Agent工程化

- 来源：微信

- 发布时间：2026-04-20 12:29

- 原文链接：[Claude-Mem：让AI编程助手拥有跨会话持久记忆](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518172&idx=1&sn=867250666fc5c9f4a7ca9c84f243b970&chksm=cf5ea8e68aca9ab2d4c501de00f8682baffb9866b120a678223699ba9024ea0b302de2a35158#rd)

- 源文章页：Claude-Mem：让AI编程助手拥有跨会话持久记忆

## 个人评注

这篇文章对 Tizer 当前的工作流很有启发：如果把 Hook 采集、混合检索和三层调用思路移植到 OpenClaw / HITL / 内容流水线里，很多原本散落在聊天、代码和临时笔记里的“上下文碎片”都可以沉淀成可回放、可追溯、可复用的长期记忆层。对持续迭代的 Coding Agent 来说，这比单纯加大上下文窗口更接近真正可运营的工程化方案。
