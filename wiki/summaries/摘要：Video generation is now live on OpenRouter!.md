---
title: 摘要：Video generation is now live on OpenRouter!
type: summary
tags:
- 视频/3D
- AI 产品
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881159826d7f5472b5a40
notion_url: https://www.notion.so/Tizer/3620e3237ded4165aa6232e74b91a3ff
notion_id: 3620e323-7ded-4165-aa62-32e74b91a3ff
---

## 一句话摘要

OpenRouter 正式上线视频生成能力，把多家视频模型纳入统一 API，通过异步任务、归一化参数、能力发现与透传参数来降低接入门槛。

## 关键洞察

- 首批支持文生视频与图生视频，覆盖 Seedance、Veo、Wan、Sora 等 7 个模型。

- 视频生成被纳入与文本、图像、音频、embeddings、reranker 并列的统一接口层。

- 为应对不同厂商请求结构、参数命名与计费单位不一致的问题，OpenRouter 采用统一封装策略。

- 视频生成采用异步 job 模式，更适合分钟级完成的长耗时生成任务。

- 统一接口之外仍保留模型特有能力的透传空间，兼顾标准化与灵活性。

## 提取的概念

- [OpenRouter](entities/OpenRouter.md)

- [统一视频生成 API](concepts/统一视频生成 API.md)

- [异步作业式生成](concepts/异步作业式生成.md)

- [归一化参数](concepts/归一化参数.md)

- [能力发现](concepts/能力发现.md)

- [透传参数](concepts/透传参数.md)

## 原始文章信息

- 作者：@OpenRouter

- 来源：X书签

- 发布时间：2026-04-15

- 原文链接：[https://x.com/OpenRouter/status/2044472220462801053](https://x.com/OpenRouter/status/2044472220462801053)

## 个人评注

这类统一视频接口很适合接入 Tizer 的内容生产流水线。上层 Agent 只需要表达任务目标，底层再按成本、时长、能力边界做模型路由与回退，后续也方便接入 HITL 审核、批量实验和多模型对比。
