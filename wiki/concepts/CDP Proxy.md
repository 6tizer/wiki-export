---
title: CDP Proxy
type: concept
tags:
- 浏览器自动化
- MCP 协议
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9b4d7d6f65f54492a26b76766b3b54a4
notion_id: 9b4d7d6f-65f5-4492-a26b-76766b3b54a4
---

## 定义

CDP Proxy 是对 Chrome DevTools Protocol 的一层 HTTP 封装，用来把原本基于 WebSocket 的浏览器调试操作转成更易调度的 HTTP API，便于 Agent 或脚本直接操控用户当前的 Chrome 会话。

## 关键要点

- 复用日常 Chrome，而不是新开隔离的无头浏览器实例

- 典型能力包括枚举标签页、执行 JavaScript、点击元素、截图等

- 对 Agent 而言，关键优势是天然继承登录态，适合处理公众号、小红书等有会话要求的页面

- 在 web-access 这类联网 Skill 中，它是浏览器执行层与上层决策层之间的重要桥梁

## 来源引用

- 《这个 Skill 太硬了，刚开源就斩获 2.8K 星标！Agent 联网能力拉满！》｜文章链接：[https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA==&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd](https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA%3D%3D&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd)

## 关联概念

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [Chrome DevTools MCP](entities/Chrome DevTools MCP.md)

- [MCP 协议](concepts/MCP 协议.md)
