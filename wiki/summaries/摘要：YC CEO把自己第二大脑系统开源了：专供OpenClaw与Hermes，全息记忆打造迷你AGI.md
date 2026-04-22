---
title: 摘要：YC CEO把自己第二大脑系统开源了：专供OpenClaw与Hermes，全息记忆打造迷你AGI
type: summary
tags:
- 记忆系统
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: https://www.notion.so/342701074b688189a2b2e043d95c53fe
notion_url: https://www.notion.so/5daab5eb88114b2d897331ab20ff6c5d
notion_id: 5daab5eb-8811-4b2d-8973-31ab20ff6c5d
---

### 一句话摘要

GBrain 是 Garry Tan 开源的 Agent 记忆底座，它把个人知识、日历、会议、邮件与社交信号持续汇入可检索知识库，并以“先读后写 + 周期维护”的方式，让 OpenClaw / Hermes 一类 Agent 获得可累积的长期记忆。

### 关键洞察

- GBrain 的核心不是单次问答，而是“信号进入 → 读取上下文 → 生成回答 → 回写新信息 → 同步索引”的记忆复利循环。

- 它采用“已整理事实 + 时间线”的双层页面结构，把当前结论和原始证据分开管理，兼顾可读性与可追溯性。

- 检索侧使用多查询扩展、向量搜索、关键词搜索与 RRF 融合排名，并配合分块去重，提升复杂知识库里的召回质量。

- 基础设施上默认用 PGLite 本地启动，先降低部署门槛，再在规模扩大后迁移到 Supabase。

- 它既可以作为独立 CLI 使用，也可以通过 MCP Server 接入 Claude Code、Cursor 等客户端，成为跨工具的共享知识后端。

### 提取的概念

- [GBrain](entities/GBrain.md)

- [PGLite](entities/PGLite.md)

- [多查询扩展](concepts/多查询扩展.md)

- [混合搜索](concepts/混合搜索.md)

- [梦境思考](concepts/梦境思考.md)

- [MCP Server](concepts/MCP Server.md)

### 原始文章信息

- 作者：AI寒武纪

- 来源：微信

- 发布时间：2026-04-11 20:26

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA%3D%3D&mid=2247513949&idx=1&sn=30e8a61a4f2fb0fb68f42b1df8aff848&chksm=cfebe5d1daec91e5ef252c1ba6b40bdc55584fad6f608c184c95d4e5706e90d2b926a4c523b0#rd)

### 个人评注

这篇文章对 Tizer 当前的工作流有直接启发：如果 OpenClaw 侧继续积累 HITL 过程、内容线索和人物上下文，就需要一个既能持续写回、又能做周期整理的长期记忆层。GBrain 提供的“知识底座 + 梦境维护 + MCP 接入”组合，很适合作为未来内容管道、关系管理和 Agent 协同的参考架构。
