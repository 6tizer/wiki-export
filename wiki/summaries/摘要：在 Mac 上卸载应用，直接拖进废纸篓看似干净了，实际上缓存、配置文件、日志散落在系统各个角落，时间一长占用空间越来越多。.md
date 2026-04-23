---
title: 摘要：在 Mac 上卸载应用，直接拖进废纸篓看似干净了，实际上缓存、配置文件、日志散落在系统各个角落，时间一长占用空间越来越多。
type: summary
tags:
- 开发工具
status: 已审核
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b68818ba998c7f3806cb538
notion_url: https://www.notion.so/41b8ae3059444d4c9ce1510f40a7c37e
notion_id: 41b8ae30-5944-4d4c-9ce1-510f40a7c37e
---

## 一句话摘要

这篇内容介绍了 PureMac 这款面向 macOS 的开源清理工具，强调它不仅能卸载应用，还能扫描并清理残留文件与多类系统缓存。

## 关键洞察

- macOS 中把应用直接拖进废纸篓，往往只删除了主程序，缓存、配置、日志、启动项等残留文件仍会保留。

- PureMac 的核心卖点是“深度卸载”，通过多层匹配扫描应用关联文件，尽量减少卸载残留。

- 除了应用卸载，它还覆盖已删除应用残留检测、系统缓存、邮件附件、大文件、Xcode 缓存、Homebrew 缓存等清理场景。

- 工具强调免费、开源、无需数据收集，并在执行删除前提供确认提示，降低误删风险。

- 这类工具的价值主要在于长期维护本地开发环境的整洁度，适合频繁安装、试用、卸载软件的 macOS 用户。

## 提取的概念

- [PureMac](entities/PureMac.md)

## 原始文章信息

- 作者：@GitHub_Daily

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[https://x.com/GitHub_Daily/status/2046854092455362739](https://x.com/GitHub_Daily/status/2046854092455362739)

## 个人评注

对 Tizer 的工作流来说，这类工具不属于 AI Agent 栈本身，但很适合作为本地开发环境维护工具：当日常频繁安装 Claude Code、Codex、Homebrew 包或各类实验性桌面工具时，PureMac 这类清理能力可以减少残留堆积，保持机器环境可控。
