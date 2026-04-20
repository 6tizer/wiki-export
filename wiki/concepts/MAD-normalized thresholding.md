---
title: MAD-normalized thresholding
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d020e27251174fa5b45391aded4b4e86
notion_id: d020e272-5117-4fa5-b453-91aded4b4e86
---

## 定义

MAD-normalized thresholding 是一种用中位绝对偏差进行标准化阈值设定的自适应压缩策略，用来根据任务难度和上下文长度动态调节 KV cache 的压缩强度。

## 关键要点

- 它把压缩阈值从固定规则改成基于分布的自适应规则。

- 更长的文档通常适合更轻的压缩，而更难的任务往往需要更激进的过滤。

- 这类阈值策略让 Latent Briefing 在不同任务形态下更容易兼顾成本与准确率。

## 来源引用

- [原文链接](https://x.com/RampLabs/status/2042672773747589588)｜源文章：Latent Briefing：让 AI Agent 直接共享记忆，省掉 31% 的 Token｜作者：@RampLabs｜发布日期：2026-04-10

## 关联概念

- [Latent Briefing](concepts/Latent Briefing.md)

- [Attention Matching](concepts/Attention Matching.md)

- [KV缓存压缩](concepts/KV缓存压缩.md)

- [Shared global mask](concepts/Shared global mask.md)
