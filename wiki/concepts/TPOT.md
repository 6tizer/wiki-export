---
title: TPOT
type: concept
tags:
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/06e9240bfc7c4c9b859f7904aceac986
notion_id: 06e9240b-fc7c-4c9b-859f-7904aceac986
---

## 定义

TPOT（Time Per Output Token）指相邻输出 Token 之间的延迟，用来衡量模型在推理阶段持续产出 Token 的速度，是文本、语音和 Agent 交互体验中的关键指标。

## 关键要点

- TPOT 越低，用户和上层 Agent 感知到的响应越流畅。

- 在多轮任务中，TPOT 会被反复累加，直接决定总任务时长。

- 网络通信、KV-Cache 迁移和解码阶段效率都会影响 TPOT。

- 它是连接底层基础设施与上层体感的重要桥梁指标。

## 来源引用

- [摘要：为了Token，阿里云竟然出了一个TPN？](summaries/摘要：为了Token，阿里云竟然出了一个TPN？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU1OTEwNDkwNw%3D%3D&mid=2247492725&idx=1&sn=05da9c55729b14a97d8fcbec7cadd3e2&chksm=fd6c11ebba90a0d90aec3ff46f46b00aea99a3b1e55e81bd81355a80b9e0f62dd360b6371d40#rd)）
