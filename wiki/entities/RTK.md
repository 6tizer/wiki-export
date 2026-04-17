---
title: RTK
type: entity
tags:
- Coding Agent
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/2ad671e004bf47b1977783e708f3bf22
notion_id: 2ad671e0-04bf-47b1-9777-83e708f3bf22
---

## 定义

RTK（Rust Token Killer）是一个面向 AI 编程场景的轻量级 Rust CLI 工具，作用是在终端输出进入 Claude Code、Cursor 等助手之前先完成清洗、压缩与重组，从而显著降低 Token 消耗。

## 关键要点

- 采用单二进制、零依赖、跨平台形态，便于快速安装和移除

- 面向高噪声命令输出，重点优化目录浏览、文件阅读、Git 状态、测试日志等场景

- 核心机制包括智能过滤、分组聚合、智能截断与去重合并

- 价值不只在省钱，也在于提升有效上下文密度并延长长会话可用时间

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ%3D%3D&mid=2247484861&idx=1&sn=53c1d6917185609b0f7342e8a06958cf&chksm=e9dd96a4a2b2e8e3b8f6566016312d36df186b16e1f374bd1dd87659ad8b5d9649bbdc1cd05f#rd)｜《这个开源工具太猛了！让 Claude Code 成本爆降 89%》｜源文章：这个开源工具太猛了！让 Claude Code 成本爆降 89%

## 关联概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [上下文压缩](concepts/上下文压缩.md)
