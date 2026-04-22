---
title: Hermes Desktop
type: entity
tags:
- 开发工具
- Agent 框架
status: 草稿
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1fed3363b2874bf3916e7f32961caf81
notion_id: 1fed3363-b287-4bf3-916e-7f32961caf81
---

## 定义

Hermes Desktop 是 Hermes 工作流的原生 macOS 客户端，通过 SSH 直接连接远程主机上的 Hermes 工作流，不引入浏览器壳、网关 API 或本地文件同步层。

## 核心要点

- **原生 macOS 体验**：不是浏览器壳，而是面向桌面环境直接设计的客户端

- **SSH 直连**：通过 SSH 连接远程主机，减少中间层带来的额外复杂度

- **Single Source of Truth**：远程主机始终是唯一真理源，本地不维护镜像副本

- **零同步冲突**：不需要文件同步到本地，也不会产生镜像分叉和同步冲突

- **内置终端**：在同一应用中浏览会话并操作远程环境

- **开源**：项目以开源方式发布

## 来源引用

- [原文链接](https://x.com/billtheinvestor/status/2042946398124150891)｜X书签｜来源条目：Hermes Desktop：用原生 macOS 应用直连远程 AI 工作流，彻底告别浏览器壳

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493188&idx=1&sn=66389b773862fc773f0712f7d2e884fb&chksm=c06ffb810cbba31126091a32a582a8cafbbbf6742accadd74d558846320d3c94d89814c83d7a#rd)｜《从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态》｜来源条目：[摘要：从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态](summaries/摘要：从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态.md)

## 关联概念

- [SkillHub](entities/SkillHub.md)

- [Tauri](entities/Tauri.md)

- [Tauri Commands](concepts/Tauri Commands.md)

- [Seeded Fallback 机制](concepts/Seeded Fallback 机制.md)
