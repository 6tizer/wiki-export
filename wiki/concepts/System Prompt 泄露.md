---
title: System Prompt 泄露
type: concept
tags:
- 提示工程
- AI 产品
- Agent 安全
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/06aaff4bc4c94441a07ac789b529464c
notion_id: 06aaff4b-c4c9-4441-a07a-c789b529464c
---

## 定义

System Prompt 泄露是指通过提示注入、逆向分析或社区协作等方式，提取并公开 AI 产品原本隐藏的系统提示词、工具定义和模型配置。

## 关键要点

- 它让开发者能够直接观察商业级 AI 产品如何约束角色、工具和边界

- 常见提取路径包括提示注入、网络请求逆向和公开样本比对

- 它的价值不在于简单照抄，而在于学习提示结构、工作流设计和安全边界

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [提示注入](concepts/提示注入.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Computer Use](concepts/Computer Use.md)

- [红队演练](concepts/红队演练.md)

## 来源引用

- [摘要：Claude Opus 4.7 自我越狱：当 AI 开始审计自己的「笼子」](summaries/摘要：Claude Opus 4.7 自我越狱：当 AI 开始审计自己的「笼子」.md)（[原文](https://x.com/elder_plinius/status/2045682830383231474)）

- [摘要：134k Star 的宝藏仓库：AI 编程工具的 System Prompt 全被扒出来了](summaries/摘要：134k Star 的宝藏仓库：AI 编程工具的 System Prompt 全被扒出来了.md)（凡人小北，2026-03-05）
