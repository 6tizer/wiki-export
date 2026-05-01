---
title: Goodput
type: concept
tags:
- 推理优化
- 商业/生态
- 多Agent协作
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/031455d80ad74fe5ae17a7568263e9ba
notion_id: 031455d8-0ad7-4fe5-ae17-a7568263e9ba
---

## 定义

Goodput 指在既定时间内系统真正稳定、有效地产出的 Token 吞吐量，强调的不只是“快”，而是可用、可交付、不会被抖动和等待抵消的吞吐。

## 关键要点

- 不同于单纯吞吐量，Goodput 关注有效结果而非名义峰值。

- 在 Agent 或并发推理场景中，局部慢节点会拖累整体 Goodput。

- 网络抖动、资源等待和长尾延迟都会压低 Goodput。

- 它适合用来评估推理系统在真实业务中的承载效率。

## 来源引用

- [摘要：为了Token，阿里云竟然出了一个TPN？](summaries/摘要：为了Token，阿里云竟然出了一个TPN？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU1OTEwNDkwNw%3D%3D&mid=2247492725&idx=1&sn=05da9c55729b14a97d8fcbec7cadd3e2&chksm=fd6c11ebba90a0d90aec3ff46f46b00aea99a3b1e55e81bd81355a80b9e0f62dd360b6371d40#rd)）
