---
title: x-tweet-fetcher
type: entity
tags:
- OpenClaw
- 社交媒体
- 浏览器自动化
status: 审核中
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/94e3b386cdba4ef08881308d13aef4e6
notion_id: 94e3b386-cdba-4ef0-8881-308d13aef4e6
---

## 定义

x-tweet-fetcher 是一个 OpenClaw Skill，让 AI Agent 无需登录、无需 API Key 即可抓取 X（推特）平台的推文内容。由 @YuLin807（QingYue）开发，采用三层后端自动降级机制。

**GitHub**：ythx-101/x-tweet-fetcher | ⭐ 294 Stars | License: MIT | Python

## 核心功能

- 拆取普通推文全文 + 互动数据

- 完整抓取 X 长文（Article）

- 展开引用推文链

- 爬取评论回复线程

- 批量抓取用户时间线

- X-Tracker：监控推文互动数据增长，检测「爆点」时机

## 三层后端自动降级

1. **FxTwitter API（首选）**：免费开放的推文嵌入接口

1. **Nitter（中间层）**：X 的开源前端镜像，可自搭私有实例

1. **Playwright 浏览器（兆底层）**：真实渲染页面抓取

## 应用场景

结合 OpenClaw 的推文分析 + KOL 内容监控 + 社交媒体运营工作流。

## 来源引用

- [摘要：x-tweet-fetcher：给 OpenClaw 装上「顺风耳」，零登录抓推文](summaries/摘要：x-tweet-fetcher：给 OpenClaw 装上「顺风耳」，零登录抓推文.md)

- [摘要：x-tweet-fetcher：让 AI Agent 免登录抓取推文，还能顺手找到论文作者的 Twitter](summaries/摘要：x-tweet-fetcher：让 AI Agent 免登录抓取推文，还能顺手找到论文作者的 Twitter.md)（X书签文章）
