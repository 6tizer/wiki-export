---
title: 摘要：chrome-cdp-skill：让 AI Agent 直连你正在用的 Chrome，无需重新登录
type: summary
tags:
- Agent 技能
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, Cursor, 自动化
source_article_url: https://www.notion.so/335701074b6881e485e7c6ea42ebb25c
notion_url: https://www.notion.so/d807c346e09c448595dfe7af7475d1f0
notion_id: d807c346-e09c-4485-95df-e7af7475d1f0
---

## 一句话摘要

chrome-cdp-skill 的核心价值是让 Agent 不再从一个干净浏览器重新开始，而是直接接管用户当前已登录、已有上下文的 Chrome 会话。

## 关键洞察

- 通过 Chrome DevTools Protocol，它能复用当前 Tab、Cookie 和登录态。

- 这把“浏览器自动化”从脚本控制，推进到了“借用真实工作上下文”。

- 对 Claude Code、Cursor 这类工具来说，这种无缝接续比功能数量更重要。

- 安全风险也更直接，因为 Agent 拿到的是用户真实会话权限。

## 提取的概念

- [chrome-cdp-skill](entities/chrome-cdp-skill.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

## 原始文章信息

- 作者：TokenMore

- 来源：X书签

- 发布时间：未注明

- 链接：[原文](https://x.com/TokenMore/status/2032806514692599813)

## 个人评注

对 Tizer 来说，这类工具特别适合需要在“已登录、已定位”页面继续工作的自动化场景。但它也提醒一件事：上下文越真实，权限边界就越要收紧。
