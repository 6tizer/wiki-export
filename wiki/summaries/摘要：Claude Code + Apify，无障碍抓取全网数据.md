---
title: 摘要：Claude Code + Apify，无障碍抓取全网数据
type: summary
tags:
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: LLM, Agent
source_article_url: ''
notion_url: https://www.notion.so/82d60cbcb2fe403bb19fc401483d9cab
notion_id: 82d60cbc-b2fe-403b-b19f-c401483d9cab
---

**一句话摘要**：Claude Code 内置 WebSearch 工具无法处理 JS 渲染页面与大规模数据采集，Apify 通过 Agent Skills 和 MCP Server 两种方案有效补充。

**关键洞察**

- Claude Code Plan 模式抓取 JS 渲染页面时频繁报 Fetch error

- Apify Agent Skills：预制爬虫技能包，结构化输出，开箱即用

- Apify MCP Server：允许直接调用多种爬虫工具，更灵活

- 两种方案互补：Skills 适合标准场景，MCP 适合定制场景

- 已有概念词条：Apify Agent Skills

**提取的概念**：Apify MCP Server、Web Scraping 技能组合、[Apify Agent Skills](concepts/Apify Agent Skills.md)

**原始文章信息**

- 作者：机器学习实验室

- 来源：微信公众号

- 链接：[https://mp.weixin.qq.com/s?__biz=MzI4ODY2NjYzMQ==&mid=2247502078](https://mp.weixin.qq.com/s?__biz=MzI4ODY2NjYzMQ%3D%3D&mid=2247502078)

**个人评注**：直接补充了已有 Apify Agent Skills 词条的应用场景；对 Tizer content pipeline 的数据采集层有实践指导意义。
