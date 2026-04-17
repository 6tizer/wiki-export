---
title: 摘要：用 werss-cli 将公众号历史文章重新保存到本地，再用 graphify 把 100 多篇文章变成知识图谱
type: summary
tags:
- 知识管理
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: https://www.notion.so/345701074b688150a193ef0f45b75bf6
notion_url: https://www.notion.so/4911a15ef4524185a09ca8b1a9c8938e
notion_id: 4911a15e-f452-4185-a09c-a8b1a9c8938e
---

## 一句话摘要

这篇文章介绍了一个从微信公众号历史文章出发，经由 werss-cli 批量本地化，再用 Graphify 编译成知识图谱与 Agent 可抓取 Wiki 的个人知识工程流程。

## 关键洞察

- 微信公众号中的历史文章虽然分散，但只要先导出为 Markdown，就能重新成为可加工的知识原料。

- werss-cli 通过调用 WeRSS 接口，把公众号文章按日期同步到本地目录，解决了历史内容难以沉淀的问题。

- Graphify 不只是图谱展示工具，还能完成实体关系提取、聚类分析、查询与 Wiki 构建，适合作为 AI 原生知识工作流的一层编译器。

- `--wiki` 模式说明知识图谱和 Wiki 可以协同存在，前者负责结构洞察，后者负责被 Agent 稳定抓取和遍历。

- 这条链路本质上是在把封闭平台内容转换为可归档、可索引、可追问的长期知识资产。

## 提取的概念

- [we-mp-rss](entities/we-mp-rss.md)

- [werss-cli](entities/werss-cli.md)

- [Graphify](entities/Graphify.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Agent 可抓取 Wiki](concepts/Agent 可抓取 Wiki.md)

## 原始文章信息

- 作者：逻辑仓管AI运营社

- 来源：微信

- 发布时间：2026/04/13 17:03

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzA3OTEwNjUwMw%3D%3D&mid=2451582189&idx=1&sn=5f669d3b8e480a52044f20c318c907f5&chksm=8989bab920c529851a230e42f6a695b110e2da878b190d07b8792b21b3e41274d73bfc02c081#rd)

## 个人评注

这篇文章和 Tizer 当前的内容管线非常贴合：它验证了“原始内容先落地，再编译成结构化知识”的可行路径。对现有 Wiki Compiler 来说，公众号文章可以先沉淀为 raw 层素材，再继续向 summary、concept、知识图谱和 Agent 可抓取 Wiki 演进，适合作为 HITL 知识编译流程的上游入口。
