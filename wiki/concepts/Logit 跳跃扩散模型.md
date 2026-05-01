---
title: Logit 跳跃扩散模型
type: concept
tags:
- 量化交易
- 商业/生态
status: 审核中
confidence: medium
last_compiled: '2026-05-01'
source_tags: 预测市场, Polymarket, 量化交易, 做市
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0eca5bb6c97a40a5bcc2fe47897ff9eb
notion_id: 0eca5bb6-c97a-40a5-bcc2-fe47897ff9eb
---

## 定义

Logit 跳跃扩散模型是把预测市场中 0 到 1 之间的概率价格先映射到 logit 空间，再用扩散项与跳跃项来刻画日常信息波动和突发新闻冲击的定价框架。

## 关键要点

- 通过 logit 变换消除概率边界带来的非线性问题

- 用扩散项表示持续波动，用跳跃项表示突发信息

- 适合构建预测市场的做市与风险管理模型

## 来源引用

- [原文链接](https://x.com/MrRyanChi/status/2033466480067747844)｜《预测市场的 Black-Scholes 时刻：Polymarket 做市量化定价框架全解析》｜源文章：预测市场的 Black-Scholes 时刻：Polymarket 做市量化定价框架全解析

## 关联概念

- [Polymarket](entities/Polymarket.md)

- 预测市场做市定价
