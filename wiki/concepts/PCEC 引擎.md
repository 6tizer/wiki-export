---
title: PCEC 引擎
type: concept
tags:
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ef31474394864f5c9045c9d740c65bdf
notion_id: ef314743-9486-4f5c-9045-c9d740c65bdf
---

## 定义

PCEC 引擎是 Helix 用来处理运行时故障的六阶段修复流水线，由 Perceive、Construct、Evaluate、Commit、Verify 与 Gene Map 组成。

## 关键要点

- Perceive 负责识别错误类型、平台与上下文

- Construct 生成候选修复策略，如退避重试、刷新 token、调整参数或拆分请求

- Evaluate 根据成功率、成本与安全性给策略打分

- Commit 与 Verify 分别负责执行最优修复和验证结果

- Gene Map 负责把本次经验写回记忆层，形成下一次的快速召回

## 来源引用

- [原文链接](https://x.com/dapanji_eth/status/2044088577773154722)｜《AI Agents Have No Memory for Failure. So We Gave Them One.》｜来源条目：Helix：给 AI Agent 装上「免疫系统」，让它记住每一次失败
