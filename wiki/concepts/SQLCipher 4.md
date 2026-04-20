---
title: SQLCipher 4
type: concept
tags:
- 安全/隐私
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/2f2ec34dd80c41df8116a36323f31d61
notion_id: 2f2ec34d-d80c-41df-8116-a36323f31d61
---

## 定义

SQLCipher 4 是 SQLite 的加密扩展版本，用于对本地数据库文件进行透明加密，常见于聊天记录等敏感数据的落盘存储。

## 关键要点

- 它在保持 SQLite 使用方式基本一致的同时，引入数据库级加密保护。

- 对使用者来说，真正的门槛不在“能否读表”，而在“能否拿到密钥并安全解密”。

- 在 AI 自动化场景里，SQLCipher 4 往往意味着数据接入前还要先解决权限与合规问题。

## 关联概念

- [wechat-cli](entities/wechat-cli.md)

- [Graphify](entities/Graphify.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [暗知识编译](concepts/暗知识编译.md)

## 来源引用

- [原文链接](https://x.com/eternityspring/status/2030669435728708005)｜《wechat-decrypt + OpenClaw：让 AI 帮你把微信群消息变成每日日报》｜来源条目：wechat-decrypt + OpenClaw：让 AI 帮你把微信群消息变成每日日报

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI2MzA5NjA4MQ%3D%3D&mid=2665365507&idx=1&sn=8efb2e3bb093dcbda21aed892627d696&chksm=f0cdf306ccc0b7fcbef97f62e290b698001da1676e7ee11075b3dbb2b100e3c12bea51b047c6#rd)｜《Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki》｜源文章：Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki

- [摘要：从命令行查询本地微信数据](summaries/摘要：从命令行查询本地微信数据.md)（[原文](https://x.com/jakevin7/status/2044983033418461386)）
