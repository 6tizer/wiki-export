---
title: Mini-OpenClaw
type: entity
tags:
- OpenClaw
- 记忆系统
status: 审核中
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/88891505cb1c460a85797f603e8077aa
notion_id: 88891505-cb1c-460a-8579-7f603e8077aa
---

## 定义

Mini-OpenClaw 是一个本地运行、文件优先、强调可审计性的 AI Agent 工作台，重点解决长期记忆、安全审计与可回溯执行问题。

## 关键要点

- 把会话与证据本地化为 JSON 文件，强化可追溯性

- 通过 Pgvector、BM25 与 RRF 融合实现混合检索，提升长期记忆效果

- 引入 Guardian 前置审查与 Postgres 状态持久化，兼顾安全与连续执行

- 采用“技能即文档”的扩展思路，便于在线编辑能力与系统提示

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [Harness Engineering](concepts/Harness Engineering.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Njk0Nw%3D%3D&mid=2247492713&idx=1&sn=697d58329dc78edaa065853085f14870&chksm=e9b942103b8b34109e2b7033053b11da342a126ea251fb119534dab8fadc86f8969f2a181ca7#rd)｜《科研智能自动化平台PaperClaw；大模型会话知识库llmwiki》｜源文章：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki
