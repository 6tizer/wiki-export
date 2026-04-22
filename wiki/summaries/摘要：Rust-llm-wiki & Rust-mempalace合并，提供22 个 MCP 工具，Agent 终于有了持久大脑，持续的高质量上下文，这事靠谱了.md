---
title: 摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了
type: summary
tags:
- 记忆系统
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: https://www.notion.so/345701074b688118b1afd547825d68c9
notion_url: https://www.notion.so/2085f04b747a467ba2d10df6b5befbb9
notion_id: 2085f04b-747a-467b-a2d1-0df6b5befbb9
---

## 一句话摘要

这篇文章记录了作者如何把 llm-wiki 与 rust-mempalace 从两个各自独立的 Rust 项目，整合成一个面向 Agent 的统一记忆底座：既保留知识生命周期管理，又补上 FTS5 检索、时序知识图谱和 MCP 工具出口。

## 关键洞察

- llm-wiki 负责知识生命周期与断言/晋级/衰减治理，MemPalace 负责高质量检索、图谱与即时唤醒，两者形成互补。

- 这次迭代的关键不是“功能堆叠”，而是通过 bridge crate 把写路径与读路径真正打通。

- 原先的 BM25 stub 被 SQLite FTS5 替代后，搜索质量从 demo 级实现升级为可用底座。

- 统一 MCP Server 把 Wiki 与 MemPalace 的 22 个工具合并成一个 Agent 可直接调用的入口。

- ingest-llm 开始同时抽取 claims、entities 和 relationships，使知识图谱具备自动生长能力。

## 提取的概念

- [llm-wiki](entities/llm-wiki.md)

- [MemPalace](entities/MemPalace.md)

- [wiki-mempalace-bridge](entities/wiki-mempalace-bridge.md)

- [FTS5 全文检索](concepts/FTS5 全文检索.md)

- [时序知识图谱](concepts/时序知识图谱.md)

- [wake-up 协议](concepts/wake-up 协议.md)

- [MCP 协议](concepts/MCP 协议.md)

## 原始文章信息

- 作者：老码小张

- 来源：微信

- 发布时间：2026-04-17 23:04

- 原文链接：[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)

## 个人评注

这类“生命周期治理 + 检索/图谱 + 工具协议”的分层设计，很适合 Tizer 当前的内容编译流：上层负责把文章编译成稳定 wiki，下层负责让 Agent 在后续写作、检索和自动化里持续调取高质量上下文。
