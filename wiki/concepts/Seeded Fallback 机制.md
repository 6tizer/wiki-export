---
title: Seeded Fallback 机制
type: concept
tags:
- 开发工具
- 工作流
status: 草稿
confidence: medium
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/cee00408fe98494f991ec7d46df7c9ee
notion_id: cee00408-fe98-494f-991e-c7d46df7c9ee
---

## 定义

Seeded Fallback 机制是一种离线优先的降级策略，在远程目录或服务不可用时回退到内置精选数据，保障核心浏览与安装流程不中断。

## 关键要点

- 远程成功时优先使用在线数据

- 在线数据不足时与内置数据混合返回

- 网络失败时切换到本地 seeded 数据

- 通过数据来源枚举标记 Remote、Seeded、Mixed 三种状态

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493188&idx=1&sn=66389b773862fc773f0712f7d2e884fb&chksm=c06ffb810cbba31126091a32a582a8cafbbbf6742accadd74d558846320d3c94d89814c83d7a#rd)｜《从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态》｜来源条目：[摘要：从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态](summaries/摘要：从 CLI 到桌面 App，再到技能市场：我们给我的 Rust Hermes Agent 造了一个完整的生态.md)

## 关联概念

- [SkillHub](entities/SkillHub.md)

- [Hermes Desktop](entities/Hermes Desktop.md)
