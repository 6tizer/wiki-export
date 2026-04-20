---
title: wx-cli
type: entity
tags:
- 开发工具
- 安全/隐私
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b8327e387e754c8596de9abeb3b0bf55
notion_id: b8327e38-7e75-4c85-96de-9abeb3b0bf55
---

## 定义

wx-cli 是一个面向本地微信数据的命令行工具，用于查询、检索、导出和监听个人微信本地数据库中的聊天、联系人、朋友圈与收藏等信息。

## 关键要点

- 它以命令行界面为主入口，覆盖会话查询、历史搜索、未读监控、朋友圈检索、联系人与收藏管理等常见场景。

- 工具通过常驻 daemon 缓存已解密数据库，降低重复解密成本，使本地查询和增量监听更接近实时使用体验。

- 项目强调完全本地处理，数据不上传云端，适合对隐私和可控性要求较高的个人知识整理流程。

- 它还提供与 agent 工具链的衔接方式，可通过 skills CLI 安装到 Claude Code、Cursor、Codex 等环境中。

## 关联概念

- [SQLCipher 4](concepts/SQLCipher 4.md)
