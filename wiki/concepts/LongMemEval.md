---
title: LongMemEval
type: concept
tags:
- 知识管理
- 长期记忆
- RAG/检索
status: 审核中
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/71edb3b746004acfbb8c05ff8f142e98
notion_id: 71edb3b7-4600-4acf-bb8c-05ff8f142e98
---

## 定义

LongMemEval 是用于评估 AI 记忆系统长程召回能力的公开基准，通常用 R@5 等指标衡量系统能否从长期上下文中找回正确记忆。

## 关键要点

- 用来比较不同记忆系统的长期记忆检索效果，而不只是看演示体验。

- 文中提到 MemPalace 在 raw mode 下的 LongMemEval R@5 达到 **96.6%**。

- 文中还提到在加入 Haiku rerank 后，最高成绩可到 **100%（500/500）**。

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s/1rY6qMBqSELEm83MbhDzLA)｜源文章：96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247505903&idx=1&sn=d9f6ab8c463b8d5e883f51ffcf133c45&chksm=c121bbb7f887f2a99a0cc4e1ce630437181d622f5c30a1064e566c02e77a5f7082ea79d11ab1#rd)｜源文章：[摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！](summaries/摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！.md)

## 关联概念

- [MemPalace](entities/MemPalace.md)

- [AAAK 方言](concepts/AAAK 方言.md)

- [MCP 协议](concepts/MCP 协议.md)

- [ChromaDB](entities/ChromaDB.md)
