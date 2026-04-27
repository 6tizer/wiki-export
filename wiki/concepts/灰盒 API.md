---
title: 灰盒 API
type: concept
tags:
- 安全/隐私
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/88159ac9dac542428f4ca1b8da35e895
notion_id: 88159ac9-dac5-4242-8f4c-a1b8da35e895
---

## 定义

灰盒 API 指外部调用者虽然看不到模型完整内部参数与权重，但能获取比纯文本输出更多的中间信号，例如 top-k logits、logprobs 或部分轨迹信息的接口形态。

## 关键要点

- 灰盒接口常用于调试、评测、可解释性分析与解码控制。

- 论文指出，这类接口暴露的少量概率分布就可能携带任务无关的敏感信息。

- 因此灰盒 API 不应被默认视为“安全的有限开放”。

## 来源引用

- [摘要：苹果新论文发出惊人一问：What do your logits know?](summaries/摘要：苹果新论文发出惊人一问：What do your logits know.md)

## 关联概念

- [Top-k Logits](concepts/Top-k Logits.md)

- [信息瓶颈原则](concepts/信息瓶颈原则.md)

- [探针](concepts/探针.md)
