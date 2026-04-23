---
title: Token 污染
type: concept
tags:
- 开发工具
- 安全/隐私
status: 审核中
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/44b39c823af54b8cb3b179ce982e7c01
notion_id: 44b39c82-3af5-4b8c-b3b1-79ce982e7c01
---

## 定义

Token 污染是指同一个接入凭证在多个旧环境、旧进程或并行部署中被重复占用，导致请求接管关系混乱、配置判断失真、排障成本飙升的运维问题。

## 关键要点

- 常见于 Bot、多环境部署和历史残留进程并存的场景

- 表面现象通常是“配置改了但始终不生效”

- 继续纠缠旧环境往往效率很低，直接更换新 token 更干净

- 需要结合进程清理与凭证轮换一起处理

## 来源引用

- [原文链接](https://x.com/AnchorNode/status/2044675901775126986)｜《兄弟们，昨天配了一个新的bot，在我的失误下，把两个机器人部署到同一个目录下面，成功把旧bot搞炸了》｜来源文章：Hermes + Telegram Bot + Codex：我花一整天踩坑，总结出这套调用链排查路径

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenRouter](entities/OpenRouter.md)
