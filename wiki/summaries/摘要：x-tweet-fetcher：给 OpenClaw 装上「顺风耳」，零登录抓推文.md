---
title: 摘要：x-tweet-fetcher：给 OpenClaw 装上「顺风耳」，零登录抓推文
type: summary
tags:
- 社交媒体
- 浏览器自动化
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, 自动化, Agent
source_article_url: ''
notion_url: https://www.notion.so/Tizer/8d29659cd3f44e7e9b08011f14f0ac63
notion_id: 8d29659c-d3f4-4e7e-9b08-011f14f0ac63
---

## 一句话摘要

x-tweet-fetcher 是 OpenClaw Skill，让 AI Agent 无需登录、无需 API Key 即可抓取 X 平台推文内容，采用 FxTwitter → Nitter → Playwright 三层后端自动降级机制。

## 关键洞察

- **零配置零成本**：不依赖 X 官方 API，利用社区基础设施（FxTwitter、Nitter）实现零成本推文抓取

- **三层自动降级**：FxTwitter（速度最快） → Nitter（灵活） → Playwright（兜底，资源消耗最大）

- **v2.0 新增 X-Tracker**：监控推文互动数据增长，检测「爆点」时机

- **已知问题**：Camoufox 依赖已 404，Nitter 公共实例不稳定，X 反爬机制持续收紧

- **应用场景**：结合 OpenClaw 的推文分析 + KOL 内容监控 + 社交媒体运营工作流

## 提取的概念

[x-tweet-fetcher](entities/x-tweet-fetcher.md) · OpenClaw

## 原始文章信息

- **作者**：YuLin807（QingYue）

- **来源**：X 书签

- **链接**：[https://x.com/YuLin807/status/2022664472243192225](https://x.com/YuLin807/status/2022664472243192225)

## 个人评注

对于 Tizer 的内容流水线，x-tweet-fetcher 是 OpenClaw 生态中用于监控 X 平台动态的实用 Skill，可以作为内容信息源的自动抓取工具。
