---
title: 摘要：I tested the same prompt on both Grok 4.3 and GPT 5.5
type: summary
tags:
- 模型评测
status: 已审核
confidence: low
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68817cbd9aeab0473e32ab
notion_url: https://www.notion.so/Tizer/72900864dd314337920c3496ff46ab71
notion_id: 72900864-dd31-4337-920c-3496ff46ab71
---

## 一句话摘要

一条病毒式传播的推文对比了 Grok 4.3 和 GPT 5.5 在歧义提示词「Count to 10 starting from 11」上的不同表现，引发了关于 LLM 语义理解与推理能力的广泛讨论。

## 关键洞察

- Grok 4.3 将「count to 10 starting from 11」理解为倒数（11→10），认为从 11 数到 10 是唯一合乎逻辑的方向

- GPT 5.5 将其理解为从 11 开始向上数 10 个数（11→20），这是更常见的自然语言解读

- 该提示词本身具有**语义歧义**：「count to 10」既可理解为「数到 10 这个数字」，也可理解为「数 10 个数」

- 评论区多数用户认为两种回答都可以接受，问题出在提示词本身的模糊性

- 多位用户测试了 Claude、Gemini、DeepSeek 等其他模型，结果各异，说明不同模型的语义消歧策略不同

## 提取的概念

（本文内容过浅，无实质性技术概念可提取，跳过概念抽取）

## 原始文章信息

- **作者**：@XFreeze

- **来源**：X（Twitter）书签

- **发布时间**：2026-04-24

- **原文链接**：[https://x.com/XFreeze/status/2047717800949563691](https://x.com/XFreeze/status/2047717800949563691)

## 个人评注

这是一条典型的「LLM 整活」推文，核心价值不在技术深度而在传播效果。对 Tizer 的内容管线而言，此类病毒式传播素材可作为社交媒体热度指标参考，但不具备知识沉淀价值。唯一可借鉴的点是：在设计 OpenClaw 的 prompt 模板时，需注意歧义消解——确保指令的语义单一性，避免模型因不同消歧策略产生不一致输出。
