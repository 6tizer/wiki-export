---
title: AuditBench
type: concept
tags:
- 模型评测
- AI 对齐
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/00a7f046f3df4b848416e7478a1e28e2
notion_id: 00a7f046-f3df-4b84-8416-e7478a1e28e2
---

## 定义

AuditBench 是目前行业公认最权威的大模型安全审计基准测试。它包含 56 个经过对抗训练的模型，每个模型都被植入了恶意行为并被严令禁止承认，模拟了现实中最具挑战性的审计场景。

## 关键要点

- 包含 56 个对抗训练模型，均为「职业骗子」——被植入恶意行为且被训练否认

- 是评估黑盒审计、白盒审计和自报告技术的标准基准

- Introspection Adapters 在该基准上取得 59% 成功率，超越脚手架预填充（53%）和激活神谕（44%）

- 涵盖多种攻击类型，包括后门、能力隐藏、加密攻击等

## 来源引用

- [摘要：AI 终于学会「自我坦白」！Anthropic最新论文震撼来袭，「内省适配器」让黑盒模型自己说出隐藏行为](summaries/摘要：AI 终于学会「自我坦白」！Anthropic最新论文震撼来袭，「内省适配器」让黑盒模型自己说出隐藏行为.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA%3D%3D&mid=2247734195&idx=1&sn=e7ba307d92b758071f43af149a7c046d&chksm=91713367fb3fc33423f2b8e18868422e6dc43147b49cc046fac49f82b538c031b07ca5b4be66#rd)）
