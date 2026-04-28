---
title: API 故障转移路由
type: concept
tags:
- 模型部署
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/da5f8fbf8a7e482ba895ec3e328dda4f
notion_id: da5f8fbf-8a7e-482b-a895-ec3e328dda4f
---

## 定义

API 故障转移路由是指在本地部署代理服务，拦截 Agent CLI 工具发出的 API 请求，当主供应商出现宕机、额度耗尽或超时等故障时，自动将请求转发至备选供应商队列中的下一家，实现无感知的服务连续性保障。

## 关键要点

- 本地代理服务拦截请求后进行 API 格式转换，使不同供应商接口对 Agent 工具透明

- 供应商队列按优先级排序，依次尝试；每个供应商有健康状态监控

- 熔断保护机制：对持续故障的供应商临时移出路由池，避免反复超时

- 典型场景：长时间无人值守任务（如睡前批量编码），通过故障转移避免因单点故障导致任务中断

- 代表实现：CC Switch 的本地路由服务

## 关联概念

- [CC Switch](entities/CC Switch.md)

- [Agent 模型热切换](concepts/Agent 模型热切换.md)

## 来源引用

- [摘要：这个51K星标的开源神器，让任何Agent都能一键切换所有模型。](summaries/摘要：这个51K星标的开源神器，让任何Agent都能一键切换所有模型。.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681944&idx=1&sn=e3f6218daedb4dbfc9931b6a3adcbc8c&chksm=f16914fa8815127eb4dc837b85b4005493b1572de01a24a2ae5d1a9a48a47169742d7150ac69#rd)）
