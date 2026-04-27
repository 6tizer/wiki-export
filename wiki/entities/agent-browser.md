---
title: agent-browser
type: entity
tags:
- 浏览器自动化
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/65349b24a2ff4d7cb9f989dee4004290
notion_id: 65349b24-a2ff-4d7c-b9f9-89dee4004290
---

## 定义

agent-browser 是一个面向 AI Agent 设计的浏览器自动化 CLI 工具，核心目标不是服务传统脚本开发，而是让 Agent 在执行过程中边观察页面边完成操作。

## 关键要点

- 面向 Agent 而不是面向人工编写脚本的浏览器自动化工具。

- 使用 Rust 编写，直接连接 Chrome DevTools Protocol。

- 不依赖 Node 或 Playwright 运行时。

- 通过 snapshot 机制为可交互元素分配短引用，降低后续操作的定位成本。

## 来源引用

- [摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.](summaries/摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.md)（[原文](https://x.com/PawelHuryn/status/2048170309396926577)）

- [摘要：agent-browser：为AI Agent 写的浏览器CLI](summaries/摘要：agent-browser：为AI Agent 写的浏览器CLI.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwNzU5MzY4OQ%3D%3D&mid=2247486082&idx=1&sn=68860cb626f874e6753331df42a06452&chksm=96b464c960e585a7580e8b47dab3d5957471c51e820dc9014909b4afcba510e60109f7838c82#rd)）
