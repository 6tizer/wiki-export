---
title: Daemon + Chrome Extension 架构
type: concept
tags:
- 浏览器自动化
- 前端开发
status: 审核中
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/04ca18e0ab8640afb1e8f298431ab867
notion_id: 04ca18e0-ab86-40af-b1e8-f298431ab867
---

## 定义

Daemon + Chrome Extension 架构是一种把后台守护进程与浏览器扩展结合的自动化方案，用来在不依赖重型浏览器框架的情况下接管网页操作。

## 关键要点

- 守护进程负责命令调度与状态管理

- 扩展负责和浏览器页面建立轻量桥接

- 常用于降低安装门槛与运行开销

## 来源引用

- 《OpenCLI 1.0：告别 Playwright，国人开发的全平台浏览器自动化 CLI 正式起航》｜X书签｜原文链接：[https://x.com/jakevin7/status/2034640077557534857](https://x.com/jakevin7/status/2034640077557534857)｜来源条目：OpenCLI 1.0：告别 Playwright，国人开发的全平台浏览器自动化 CLI 正式起航
