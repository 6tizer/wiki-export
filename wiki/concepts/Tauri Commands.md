---
title: Tauri Commands
type: concept
tags:
- 前端开发
- 链上协议
status: 审核中
confidence: high
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/67fd54938cbf4ac7b68f122b56933ae0
notion_id: 67fd5493-8cbf-4ac7-b68f-122b56933ae0
---

## 定义

Tauri Commands 是前端通过 `invoke()` 调用 Rust 函数的桥接机制，用来把桌面界面与本地 Rust 能力安全连接起来。

## 关键要点

- 前端以命令形式调用后端函数

- 返回值可以保持类型安全

- 适合暴露聊天、会话、配置、技能安装等本地能力

- 让 UI 与 Agent 核心可以在同一进程内协作

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493188&idx=1&sn=66389b773862fc773f0712f7d2e884fb&chksm=c06ffb810cbba31126091a32a582a8cafbbbf6742accadd74d558846320d3c94d89814c83d7a#rd)｜《从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态》｜来源条目：[摘要：从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态](summaries/摘要：从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态.md)

## 关联概念

- [Hermes Desktop](entities/Hermes Desktop.md)

- [SkillHub](entities/SkillHub.md)
