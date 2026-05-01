---
title: RTK
type: entity
tags:
- CLI 工具
- 内容自动化
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2ad671e004bf47b1977783e708f3bf22
notion_id: 2ad671e0-04bf-47b1-9777-83e708f3bf22
---

## 定义

RTK（Rust Token Killer）是一个面向 AI 编程场景的轻量级 Rust CLI 工具，作用是在终端输出进入 Claude Code、Cursor 等助手之前先完成清洗、压缩与重组，从而显著降低 Token 消耗。

## 关键要点

- 采用单二进制、零依赖、跨平台形态，便于快速安装和移除

- 面向高噪声命令输出，重点优化目录浏览、文件阅读、Git 状态、测试日志等场景

- 核心机制包括智能过滤、分组聚合、智能截断与去重合并

- 价值不只在省钱，也在于提升有效上下文密度并延长长会话可用时间

## 来源引用

- 这个开源工具太猛了！让 Claude Code 成本爆降 89%（[原文](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ%3D%3D&mid=2247484861&idx=1&sn=53c1d6917185609b0f7342e8a06958cf&chksm=e9dd96a4a2b2e8e3b8f6566016312d36df186b16e1f374bd1dd87659ad8b5d9649bbdc1cd05f#rd)）

- [摘要：rtk：给 AI 编码工具装上「信息压缩阀」，Token 消耗最高降 90%](summaries/摘要：rtk：给 AI 编码工具装上「信息压缩阀」，Token 消耗最高降 90%.md)（[原文](https://x.com/laogui/status/2045677115341934867)）

- [摘要：The fastest and most efficient code intelligence engine for AI coding agents.](summaries/摘要：The fastest and most efficient code intelligence engine for AI coding agents.md)（[原文](https://x.com/DataChaz/status/2045784379155226971)）

## 关联概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [PreToolUse](concepts/PreToolUse.md)

- [上下文压缩](concepts/上下文压缩.md)

- [h5i](entities/h5i.md)

- [Context DAG](concepts/Context DAG.md)

- [Context Mode](concepts/Context Mode.md)
