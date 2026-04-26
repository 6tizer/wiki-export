---
title: Durable Objects
type: entity
tags:
- 上下文管理
- 算力基础设施
status: 审核中
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/482a591b333a4d5597e0b771eba8bb9b
notion_id: 482a591b-333a-4d55-97e0-b771eba8bb9b
---

## 定义

Durable Objects 是 Cloudflare 提供的有状态边缘执行单元，用来为单个对象维持连接状态、会话上下文与请求转发逻辑。

## 关键要点

- 适合承载隧道连接、会话保持与状态隔离等需要“单点状态”的场景。

- 在 hostc 架构中，每个隧道由独立对象承载，有助于实现隔离与故障恢复。

- 它补足了传统无状态 Worker 在长连接和共享状态上的不足。

## 来源引用

- [摘要：hostc：轻量级内网穿透神器，一行命令获得公网 HTTPS 隧道！](summaries/摘要：hostc：轻量级内网穿透神器，一行命令获得公网 HTTPS 隧道！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484582&idx=1&sn=12136276fdabf532ee53c87f82f3099a&chksm=f5804d315efc5071a98c61a25dccd36154710d4012c08932729736c2dc84333992b80904ae75#rd)）
