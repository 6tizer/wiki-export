---
title: ClawJacked
type: concept
tags:
- OpenClaw
- 安全/隐私
status: 草稿
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/95ed9c8266fa4cba9e0bfd3ca84353aa
notion_id: 95ed9c82-66fa-4cba-9e0b-fd3ca84353aa
---

## 定义

ClawJacked 是 OpenClaw 的一个**高危安全漏洞**，由 Oasis Security 发现，允许任意网站通过提示注入手段**静默劫持用户的本地 OpenClaw Agent 实例**，从而在用户不知情的情况下执行恶意操作。

## 风险等级

高危。攻击者可利用此漏洞控制本地 Agent，访问用户文件、账号、执行命令等。

## 修复状态

已于 **OpenClaw 2026.2.26 版本**修复。建议用户升级到最新版本。

## 相关漏洞

- CVE-2026-25253：本地代理框架一键远程代码执行漏洞（另一个已修复的安全问题）

## 来源引用

- 摘要：OpenClaw 完全指南：把你的电脑变成一个 24/7 自主运转的 AI 员工
