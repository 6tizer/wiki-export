---
title: Playbook 驱动策略
type: concept
tags:
- 内容自动化
- 上下文管理
- 长期记忆
status: 审核中
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ba6eef1171474272aa70404edcf192a7
notion_id: ba6eef11-7147-4272-aa70-404edcf192a7
---

## 定义

Playbook 驱动策略是一种让 AI Agent 通过可读写的策略文件（Playbook）自主学习和迭代工作方法的模式。Agent 在执行任务后复盘数据表现，将有效策略写入 Playbook，下次执行时读取最新规则，形成「采集→分析→更新规则→执行」的进化闭环。

## 关键要点

- Playbook 是 Agent 的策略手册，包含标题规则、内容公式、发布时机等可执行指导

- Agent 拥有对 Playbook 的读写权限，不仅执行策略也能修改策略

- 每次数据复盘后，Agent 自动追加新发现并标注版本号和数据支撑

- 与记忆系统配合：Playbook 管「怎么做」，[MEMORY.md](http://memory.md/) 管「发生过什么」

- 核心理念：从「人教 AI」到「AI 自己学」

## 来源引用

- [摘要：我用OpenClaw搭了11个AI Agent，它们学会了自我进化](summaries/摘要：我用OpenClaw搭了11个AI Agent，它们学会了自我进化.md)（孟健AI编程，2026-03-01）— 11 个平台 Agent 各自维护 Playbook，通过 Cron 定时复盘自动更新策略
