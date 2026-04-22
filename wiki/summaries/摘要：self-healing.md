---
title: 摘要：self-healing
type: summary
tags:
- 浏览器自动化
status: 已审核
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: https://www.notion.so/349701074b68813fa062c4dd147f8744
notion_url: https://www.notion.so/f5b802d91a084070b254b6ef4312fba4
notion_id: f5b802d9-1a08-4070-b254-b6ef4312fba4
---

## 一句话摘要

Browser Harness 是 Browser Use 开源的极简自愈式浏览器 harness，主张把 [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md) 能力直接暴露给 LLM，并允许 Agent 在执行过程中按需改写 helpers 代码补齐缺失能力。

## 关键洞察

- 项目刻意保持极薄抽象层，用约 592 行 Python 展示 thin harness 的设计取向。

- 相比先把工具预置完整，Browser Harness 更强调让 Agent 在运行中发现缺口、修改源码、继续任务。

- 通过 CDP 直连真实 Chrome，可以把浏览器操作下沉为更通用的执行能力，而不是封装成大量固定指令。

- 这条路线说明浏览器 Agent 的竞争点，正从“工具数量”转向“harness 是否可演化、可修复、可持续执行”。

## 提取的概念

- [Browser Harness](entities/Browser Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [Browser Use](entities/Browser Use.md)

## 原始文章信息

- 作者：@Gorden_Sun

- 来源：X书签

- 发布时间：2026-04-20

- 原文链接：[https://x.com/Gorden_Sun/status/2046228429662794153](https://x.com/Gorden_Sun/status/2046228429662794153)

## 个人评注

这类自愈式 harness 对 Tizer 的价值，在于把浏览器操作从一次性 skill 升级成可持续演化的执行层：缺少能力时可以局部补函数，而不是整套重写。若与 HITL 审核点结合，可把高风险点击或登录留给人工确认，把低风险的信息采集与页面操作交给 Agent 自动完成。
