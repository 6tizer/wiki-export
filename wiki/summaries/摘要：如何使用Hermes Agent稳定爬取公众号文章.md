---
title: 摘要：如何使用Hermes Agent稳定爬取公众号文章
type: summary
tags:
- 内容自动化
- 浏览器自动化
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, OpenClaw, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a306c2a938f54b8fbce5a804020fba21
notion_id: a306c2a9-38f5-4b8f-bce5-a804020fba21
---

## 一句话摘要

通过 Hermes Agent 封装 Browser Use 的 skill，可实现对微信公众号文章的稳定自动化爬取，并可选择本地的 Camoufox 作为云端方案的稳定替代。

## 关键洞察

- **Browser Use 免费提供给 Hermes 用户**：4月9日 Browser Use 官宣 Hermes Agent 用户可免费使用其云端浏览器，包含无限时长、免费 proxy 和持久化鉴权

- **Skill 封装流程只需十分钟**：通过自然语言指令 Hermes Agent，可在约 10 分钟内自动封装一个微信公众号爬取 skill

- **可拓展流程**：爬取完成后可直接将内容输出到飞书文档，实现端到端自动化内容流水线

- **双路备选**：云端方案用 Browser Use，本地方案用 Camoufox，可根据隐私/费用考虑自由切换

- **Draco-Skills-Collection 开源**：两种方案的 skill 均已开源到 GitHub 仓库，可直接引用

## 提取的概念

[Hermes Agent](entities/Hermes Agent.md)、[Browser Use](entities/Browser Use.md)、[Camoufox](entities/Camoufox.md)

## 原始文章信息

- **作者**：Draco正在VibeCoding

- **来源**：微信公众号

- **发布时间**：2026-04-11

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzI2NzM4MTQwMg==&mid=2247495578&idx=1&sn=2931b98771530120005eb632e8fb183c](https://mp.weixin.qq.com/s?__biz=MzI2NzM4MTQwMg%3D%3D&mid=2247495578&idx=1&sn=2931b98771530120005eb632e8fb183c)

## 个人评注

这篇文章直接关于 Tizer 正在使用的 Hermes Agent + 微信公众号爬取工作流。Browser Use 免费活动具有实际价値，可直接加入内容获取流水线。Camoufox 作为备用方案也应当了解，多一个选项以防备未来收费风险。
