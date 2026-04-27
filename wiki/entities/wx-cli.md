---
title: wx-cli
type: entity
tags:
- 开发工具
- Agent 技能
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/cb7b0c75f7924ab69f981e252524ef68
notion_id: cb7b0c75-f792-4ab6-9f98-1e252524ef68
---

## 定义

wx-cli 是 jackwener 发布的本地微信数据命令行工具，用于查询、检索、导出和监听个人微信本地数据库中的聊天、联系人、朋友圈与收藏等信息。

## 关键要点

- 它以 CLI 作为主要交互界面，覆盖会话查询、历史搜索、未读监控、朋友圈检索、联系人与收藏管理等高频场景。

- 工具采用常驻 daemon + 缓存复用的实现方式，首次解密后可复用数据库缓存，以提升后续查询与监听效率。

- 项目强调完全本地处理，数据不上传云端，更适合私有数据整理、个人知识管理与本地自动化流程。

- 它还通过 skills CLI 提供 agent 侧的一键接入方式，使聊天记录查询能力能进入 Claude Code、Cursor、Codex 等环境。

## 关联概念

- [SQLCipher 4](concepts/SQLCipher 4.md)

- [进程内存密钥扫描](concepts/进程内存密钥扫描.md)

- [skills CLI](entities/skills CLI.md)

## 来源引用

- [摘要：从命令行查询本地微信数据](summaries/摘要：从命令行查询本地微信数据.md)（[原文](https://x.com/jakevin7/status/2044983033418461386)）
