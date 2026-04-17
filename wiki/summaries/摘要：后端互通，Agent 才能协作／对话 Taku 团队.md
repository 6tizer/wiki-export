---
title: 摘要：后端互通，Agent 才能协作／对话 Taku 团队
type: summary
tags:
- 工作流
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/68674b0903ff4d9ebf6ea728b0e9a438
notion_id: 68674b09-03ff-4d9e-bf6e-a728b0e9a438
---

**一句话摘要**：Taku 通过三层 Harness（Runtime + 统一後端通讯协议 + 跨应用 context 共享），实现不同生成物之间的自主协作，解决 Claude Code 项目隔离设计对普通用户的限制。

**关键洞察**

- Agent Harness 共识：模型是 CPU，上下文窗口是内存， Agent Harness 就是操作系统

- Taku 三层架构：**Runtime**（生成即运行）+ **统一後端通讯协议**（不同工具后端写通）+ **跨应用 context 共享**（一处积累全应用自动同步）

- 关键洞察：开发者需要项目隔离，普通用户需要工具自动协作：同一件事，两群人的需求正好相反

- 概念验证：将纯量化脚本和 AI Hedge Fund（Multi-agent）由主 Agent 一句话串联起来

- 代码本身不再稀缺，稀缺的是代码背后承载的専业知识——能分发这个就能分发能力

**提取的概念**

- Taku（多应用後端互通 Harness 平台）

- Agent Harness（包裹在 AI 模型外面的软件基础设施层）

**原始文章信息**

- 作者：赛博禦心 | 来源：微信公众号 | 发布时间：2026-03-22

- 链接：[https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247514554](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247514554)

**个人评注**

与 Tizer 的工作流密切相关：将内容 pipeline 里的不同工具（量化工具、内容工具）自动协作起来，正是 Taku 在解决的问题。
