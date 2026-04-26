---
title: 浏览器 Session 复用
type: concept
tags:
- 浏览器自动化
- 上下文管理
- Agent 安全
status: 审核中
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/23759397d9a543c787ae0aad7b129b4a
notion_id: 23759397-d9a5-43c7-87ae-0aad7b129b4a
---

## 定义

浏览器 Session 复用是让自动化工具直接继承用户当前浏览器登录状态与会话上下文的能力，从而减少单独管理 Cookie、Token 和登录流程的复杂度。

## 关键要点

- 降低受保护网站接入门槛

- 让 Agent 能在已登录上下文中继续操作或读取信息

- 但也提高了权限边界与会话安全设计的重要性

## 来源引用

- [摘要：opencli-rs：用 Rust 重写的网站抓取神器，AI Agent 时代的万能信息接口](summaries/摘要：opencli-rs：用 Rust 重写的网站抓取神器，AI Agent 时代的万能信息接口.md)｜X书签文章｜原文链接：[https://x.com/nash_su/status/2039107988263412099](https://x.com/nash_su/status/2039107988263412099)
