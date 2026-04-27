---
title: HermesClaw
type: entity
tags:
- OpenClaw
- 多Agent协作
- Agent 协作模式
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/bc3b7bf5b33441c1968efa8cfa388ac6
notion_id: bc3b7bf5-b334-41c1-968e-fa8cfa388ac6
---

## 定义

HermesClaw 是一个面向微信场景的双 Agent 统一代理层，用来协调 Hermes Agent 与 [OpenClaw](entities/OpenClaw.md) 在同一账号下共存与切换。

## 关键要点

- 通过唯一的 iLink 轮询器与多个本地代理服务器实现统一入口

- 支持 `/hermes`、`/openclaw`、`/both` 等模式切换

- 以轻量代理方式转发原始 iLink 消息，不直接处理媒体内容

- 重点价值在于把消息通道与不同 Agent 大脑解耦，降低双系统共存的复杂度

## 关联概念

- [iLink 协议](concepts/iLink 协议.md)

- [OpenClaw](entities/OpenClaw.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Njk0Nw%3D%3D&mid=2247492713&idx=1&sn=697d58329dc78edaa065853085f14870&chksm=e9b942103b8b34109e2b7033053b11da342a126ea251fb119534dab8fadc86f8969f2a181ca7#rd)｜[摘要：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki](summaries/摘要：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki.md)｜源文章：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki
