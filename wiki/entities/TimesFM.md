---
title: TimesFM
type: entity
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/2e5aa05579f84e7e97b2cc3cdbff2844
notion_id: 2e5aa055-79f8-4e7e-97b2-cc3cdbff2844
---

## 定义

TimesFM 是 Google 开源的时间序列预测基础模型，面向历史数值序列输入后的未来走势预测与区间估计，强调 zero-shot 可用性与工程落地能力。

## 核心要点

- 属于预训练好的时间序列预测底座模型，可直接用于业务销量、流量、负载、需求等场景的 baseline 验证。

- 2.5 版本将参数量从 500M 压缩到 200M，并把上下文窗口扩展到 16k。

- 新版本移除了 frequency indicator，使接口更简洁。

- 官方仓库陆续补充了 XReg 协变量支持、Transformers 版本、LoRA 微调示例与测试，工程化成熟度更高。

## 来源引用

- 摘要：😱 谷歌偷偷开源了时序预测底座TimesFM 2.5，参数降到200M，上下文飙到16k。（[原文](https://x.com/oragnes/status/2046130320316207431)）
