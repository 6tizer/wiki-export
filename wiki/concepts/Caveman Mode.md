---
title: Caveman Mode
type: concept
tags:
- Coding Agent
- Agent 技能
status: 审核中
confidence: high
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d28d860bff704645b3b513a2de1fe859
notion_id: d28d860b-ff70-4645-b3b5-13a2de1fe859
---

## 定义

Caveman Mode 是一种面向 **Claude Code** 等 Coding Agent 的输出压缩配置方式，通过预先约束回答风格，尽量去掉铺垫、解释性废话和冗余礼貌语，把回复压缩为更短的代码与结论，从而降低 token 消耗并提升交互速度。

## 核心要点

- 主要优化的是 **输出 token**，不是模型推理能力本身

- 常见实现方式是把规则写入项目级的 [CLAUDE.md](concepts/CLAUDE.md.md)，让代理在会话开始时自动读取

- 适合已经理解上下文、只需要快速实现代码的执行阶段

- 不适合首次学习陌生框架、需要权衡解释或需要团队共享上下文的场景

## 典型触发方式

- 在 [CLAUDE.md](concepts/CLAUDE.md.md) 顶部加入简短规则，如“少解释、少铺垫、代码优先”

- 通过 repo / skill / plugin 的方式，把该风格做成可复用的项目配置

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

## 来源引用

- [原文链接](https://x.com/zaimiri/status/2044769304923529383)｜《How to Set Up Claude Code: Caveman Mode (Save 75% off)》｜来源页：Caveman Mode：让 Claude 像原始人一样说话，节省 75% Token 费用

- [摘要：The fastest and most efficient code intelligence engine for AI coding agents.](summaries/摘要：The fastest and most efficient code intelligence engine for AI coding agents.md)（[原文](https://x.com/DataChaz/status/2045784379155226971)）
