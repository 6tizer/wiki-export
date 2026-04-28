---
title: AI 供应商锁定
type: concept
tags:
- 商业/生态
- Agent 安全
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/405d7de584e940e18ff1e5733bc2985f
notion_id: 405d7de5-84e9-40e1-8ff1-e5733bc2985f
---

## 定义

AI 供应商锁定（AI Vendor Lock-in）指企业将核心业务流程深度绑定在单一闭源 AI 服务商上，导致在服务商单方面变更政策（封号、涨价、降级模型）时缺乏应对能力，业务面临中断甚至崩溃风险。

## 关键要点

- 闭源 AI 服务商拥有单方面暂停/终止服务的权力，企业无法干预

- 组织级封禁可因单个账号触发安全规则而波及全公司，属于「连坐」机制

- 企业越依赖单一 AI 供应商，业务韧性（resilience）越低

- 缓解策略：多供应商冗余部署（如同时接入 Claude + Gemini + GPT）、本地部署开源模型作为兜底、API 层面做抽象适配

## 来源引用

- [摘要：9秒，公司没了！Claude「删库跑路」，Anthropic封杀110人公司，却还在扣钱](summaries/摘要：9秒，公司没了！Claude「删库跑路」，Anthropic封杀110人公司，却还在扣钱.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695870&idx=1&sn=90f71bfc3f6091269c543b91368b22ee&chksm=f0e8f6e20c4403138c01e736a3c07cd72c780fe55c94401be3d215aa64fd7e8e3adce1d273e2#rd)）
