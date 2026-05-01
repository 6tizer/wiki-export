---
title: Top-k Logits
type: concept
tags: []
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d95475c075a644f085fd1b18dfa7d6ce
notion_id: d95475c0-75a6-44f0-85fd-1b18dfa7d6ce
---

## 定义

Top-k Logits 指模型在输出下一个词之前，对概率最高的前 k 个候选 token 给出的原始得分集合。

## 关键要点

- 很多 API 会把 top-k logits 或 logprobs 作为调试与可解释性信息暴露给开发者。

- 这篇论文显示，少量 top-k logits 就足以泄露与任务无关的目标属性和背景细节。

- 因而它不只是调试信号，也可能成为灰盒攻击中的信息泄露接口。

## 来源引用

- [摘要：苹果新论文发出惊人一问：What do your logits know?](summaries/摘要：苹果新论文发出惊人一问：What do your logits know.md)

## 关联概念

- [信息瓶颈原则](concepts/信息瓶颈原则.md)

- [灰盒 API](concepts/灰盒 API.md)

- [探针](concepts/探针.md)

- [残差流](concepts/残差流.md)
