---
title: 摘要：重构AI信息获取工作流——筛选5%信息差
type: summary
tags:
- 内容自动化
- RAG/检索
status: 已审核
confidence: medium
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3a225b15355543b19c8d8999706efe19
notion_id: 3a225b15-3555-43b1-9c8d-8999706efe19
---

## 一句话摘要

重构 AI 信息获取工作流：三桶信息源聚合（自媒体更新 + 全网热榜 + 聚合器），筛选未被 AI 捅到的 90% 中最有信息差的前 5%。

## 关键洞察

- **AI 搜索与手动刷重复度高**：AI 只能捅前 10%，且与平台推送高度重复

- **三桶聚合**：自媒体更新 → 全网热榜趋势 → 聚合器去重+双语翻译

- **11 个信息聚合站点**：WaytoAGI、[bestblogs.dev](http://bestblogs.dev/)、[techurls.com](http://techurls.com/)、[tophub.today](http://tophub.today/) 等

- **视频总结技巧**：口播用字幕提取，长视频用飞书 AI 录音豆边播边录

- 已开源：[github.com/LearnPrompt/ai-news-radar](http://github.com/LearnPrompt/ai-news-radar)

## 原始文章信息

- **作者**：卡尔的AI沃茨

- **发布时间**：2026-03-03

- **链接**：[原文](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247505087&idx=1&sn=2828d8ca950eb86e0155b91052cf9b08)

## 个人评注

信息聚合工作流对 Tizer 的 content pipeline 有直接参考价值。三桶聚合策略可应用于微信文章数据库的信息源扩展。
