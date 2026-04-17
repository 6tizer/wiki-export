---
title: Chrome DevTools MCP
type: entity
tags:
- Agent 技能
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, 自动化, Cursor, LLM
source_article_url: ''
notion_url: https://www.notion.so/1eb287bd361242e8b2c2223fe1ba2a2e
notion_id: 1eb287bd-3612-42e8-b2c2-223fe1ba2a2e
---

## 定义

Chrome DevTools MCP 是 Google Chrome 官方提供的 MCP Server，让 AI 助手直接连接用户当前正在使用的 Chrome 浏览器会话。

## 核心要点

- 复用已有登录态、当前页面和浏览器上下文，而不是新开隔离实例

- 适合读取页面内容、执行脚本、分析网络请求和调试 UI

- 与持久连接方案相比，官方实现更偏通用调试能力

## 来源引用

- 《Chrome DevTools MCP：让 AI 助手直接操控你正在用的浏览器》— X书签，2026-03

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA%3D%3D&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd)｜《这个 Skill 太硬了，刚开源就斩获 2.8K 星标！Agent 联网能力拉满！》

## 关联概念

- [MCP 协议](concepts/MCP 协议.md)

- [chrome-cdp-skill](entities/chrome-cdp-skill.md)

- [web-access](entities/web-access.md)

- [CDP Proxy](concepts/CDP Proxy.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)
