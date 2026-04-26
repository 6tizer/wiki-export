---
title: 嵌入式 Python
type: concept
tags:
- 量化交易
status: 草稿
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/db832382be014de7a690f76deba1d237
notion_id: db832382-be01-4de7-a690-f76deba1d237
---

## 定义

嵌入式 Python 指的是把 Python 解释器直接嵌入原生应用内部，通过 C API 或类似桥接方式调用 Python 生态，从而在不牺牲原生交互性能的前提下获得强大的脚本与计算能力。

## 关键要点

- 它常用于“原生 UI + Python 计算引擎”的混合架构，兼顾桌面体验与科学计算生态。

- 相比把计算放到独立服务里，这种方式可以减少网络序列化和跨进程传输开销。

- 在金融产品中，它特别适合承接估值、风险、回测等高复杂度分析模块。

- FinceptTerminal 用它把 Qt/C++ 前端与 Python 金融分析能力连接起来，体现了一种实用的工程折中。

## 来源引用

- [摘要：GitHub 本周霸榜第一，FinceptTerminal 你将拥一个24H为你工作的金融分析专家!](summaries/摘要：GitHub 本周霸榜第一，FinceptTerminal 你将拥一个24H为你工作的金融分析专家!.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI5MDEwNTYxNw%3D%3D&mid=2649429819&idx=1&sn=4f91da024fe00ee1607dde286158bc6b&chksm=f579bd128a479acb5eace6a310f875856b655a37af7edfe7773fb74ef862fe97b662f40c859c#rd)）

## 关联概念

- [Ollama](entities/Ollama.md)

- [LM Studio](entities/LM Studio.md)
