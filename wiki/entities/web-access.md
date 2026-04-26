---
title: web-access
type: entity
tags:
- 浏览器自动化
- 多Agent协作
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/4991007ef13142f2ace24f483faa1703
notion_id: 4991007e-f131-42f2-ace2-4f483faa1703
---

## 定义

web-access 是一个围绕 Agent 联网场景设计的开源 Skill，面向 Claude Code、Codex 等 AI 编程助手，将网页访问从“搜索/抓取”升级为“真实浏览器执行”。

## 核心要点

- 将 WebSearch、WebFetch、Jina、curl、CDP 等能力封装成目标导向的使用方法

- 通过 [Chrome DevTools MCP](entities/Chrome DevTools MCP.md) 与 [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md) 连接真实浏览器，会复用现有登录态

- 遇到动态渲染、登录墙、反爬场景时，可从轻量抓取升级到浏览器模式

- 支持多子 Agent 并行调研，适合竞品分析、社媒监控、GitHub 周报等任务

## 来源引用

- 《这个 Skill 太硬了，刚开源就斩获 2.8K 星标！Agent 联网能力拉满！》｜文章链接：[https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA==&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd](https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA%3D%3D&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd)

## 关联概念

- [MCP 协议](concepts/MCP 协议.md)

- [Chrome DevTools MCP](entities/Chrome DevTools MCP.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)
