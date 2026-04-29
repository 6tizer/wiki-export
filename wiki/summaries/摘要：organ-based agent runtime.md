---
title: 摘要：organ-based agent runtime
type: summary
tags:
- 长期记忆
- AI 产品
status: 已审核
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b68814291f0db16cbfbfe1b
notion_url: https://www.notion.so/Tizer/af452db88ac1474980c60fd80196a070
notion_id: af452db8-8ac1-4749-80c6-0fd80196a070
---

## 一句话摘要

Large Memory Model（LMM）是一种全新 AI 架构，与 LLM 相反——不依赖 prompt 检索，而是自动捕获用户上下文并在合适时刻主动浮现信息，由哈佛出身的 Engramme 团队开发。

## 关键洞察

- **LMM 与 LLM 是对偶架构**：LLM 将文本压缩为权重、被动回答 prompt；LMM 捕获用户所见所闻，主动在正确时刻浮现信息

- **核心关键词是 persistent memory**：赋予每个应用持久化的上下文记忆能力，解决 AI 的「阿喀琉斯之踵」

- **不走 RAG / 向量搜索路线**：LMM 声称是一种全新范式，专为人类记忆工作方式设计

- **强学术背景团队**：创始团队拥有 160+ Nature/ICLR 论文，关闭哈佛实验室全职创业，目前处于 Beta 阶段

## 提取的概念

- [Large Memory Model](concepts/Large Memory Model.md)

- [Engramme](entities/Engramme.md)

## 原始文章信息

- **作者**：@svpino（转发 @EngrammeHQ）

- **来源**：X书签

- **发布时间**：2026-04-28

- **原文链接**：[https://x.com/svpino/status/2049214583404187987](https://x.com/svpino/status/2049214583404187987)

## 个人评注

LMM 的「无 prompt 主动浮现」范式如果成立，可能对 OpenClaw 的记忆层设计有借鉴意义——当前 OpenClaw Dreaming 依赖定时批处理来整合记忆，而 LMM 提出了一种更接近人类记忆的实时浮现机制。值得关注其 Beta 后的技术细节披露，特别是如何在不依赖向量检索的前提下实现高效的上下文匹配。
