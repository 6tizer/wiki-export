---
title: Tauri
type: entity
tags:
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/67ee605069134ec59e7ef245939c13af
notion_id: 67ee6050-6913-4ec5-9e7e-f245939c13af
---

## 定义

Tauri 是一个使用系统原生 WebView 与 Rust 后端来构建桌面应用的跨平台框架，适合把已有 Rust Agent 栈直接封装成轻量桌面产品。

## 关键要点

- 使用系统自带 WebView 渲染前端，不依赖完整 Chromium 运行时

- 后端可以直接复用 Rust 业务代码与 crate

- 相比 Electron，打包体积更小，更适合轻量桌面 Agent

- 适合把 CLI 或 Agent 能力封装成可交互的 GUI 应用

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493188&idx=1&sn=66389b773862fc773f0712f7d2e884fb&chksm=c06ffb810cbba31126091a32a582a8cafbbbf6742accadd74d558846320d3c94d89814c83d7a#rd)｜《从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态》｜来源条目：[摘要：从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态](summaries/摘要：从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态.md)

## 关联概念

- [Hermes Desktop](entities/Hermes Desktop.md)

- [SkillHub](entities/SkillHub.md)
