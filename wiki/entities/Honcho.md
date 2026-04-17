---
title: Honcho
type: entity
tags:
- 记忆系统
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ac2c803026e548fc8c297c012ca94c5a
notion_id: ac2c8030-26e5-48fc-8c29-7c012ca94c5a
---

## 定义

Honcho 是 Hermes 生态推荐的长期记忆后端，用于为 Agent 提供用户级隔离、会话历史管理与语义检索能力。

## 核心要点

- 在本文语境里，Honcho 对应 Hermes 的长期记忆层，承接用户偏好、项目历史与嵌入检索。

- 它与上下文窗口、SQLite / LMDB 一起构成分层记忆体系，分别覆盖会话级、短期和长期记忆。

- 社区存在 `honcho-self-hosted` 方案，说明它既可作为官方推荐后端，也可走本地化、自托管部署路径。

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5ODM0MDIyNg%3D%3D&mid=2247484011&idx=1&sn=588c8c9f5f8a8e56cb1d32c5ba91947a&chksm=976d338b09e0fcd9565bdfc1728262bd18a93f1408aecb26a19ba94a31968423d172955f1a51#rd)｜《Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比》｜源文章：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenClaw](entities/OpenClaw.md)
