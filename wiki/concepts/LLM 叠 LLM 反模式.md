---
title: LLM 叠 LLM 反模式
type: concept
tags:
- 推理优化
status: 审核中
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2c66f293176a4ebc875dc75b85c18f03
notion_id: 2c66f293-176a-4ebc-875d-c75b85c18f03
---

## 定义

LLM 叠 LLM 反模式是指在已经有主模型负责判断的前提下，再额外加入小模型预处理同类任务，导致信息损耗与系统复杂度上升的一类设计误区。

## 关键要点

- 它常出现在“先让一个模型总结，再让另一个模型决策”的链路里。

- 如果主模型本来就具备判断能力，额外预处理往往会丢失细节并增加成本。

- 更优的做法通常是把原始结果交给主模型，只在必要时增加结构化过滤层。

## 来源引用

- [原文链接](https://x.com/YuLin807/status/2030996280051462609)｜《OpenClaw × SearxNG：零成本给你的 AI 助手装上「搜索外脑」》｜来源条目：OpenClaw × SearxNG：零成本给你的 AI 助手装上「搜索外脑」
