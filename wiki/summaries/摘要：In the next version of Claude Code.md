---
title: 摘要：In the next version of Claude Code
type: summary
tags:
- Agent 协作模式
- CLI 工具
status: 已审核
confidence: low
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b688177844edc0d03d54b3d
notion_url: https://www.notion.so/Tizer/f861c62e5e9c467ca99bc0a950538508
notion_id: f861c62e-5e9c-467c-a99b-c0a950538508
---

## 一句话摘要

Claude Code 即将把 npm 包的底层实现切到 Bun，并从 v2.1.113 起默认分发原生二进制，因此 CLI 启动更快、运行时不再依赖 Node.js。

## 关键洞察

- 安装命令保持不变，但底层交付方式从 JavaScript 构建切换为原生二进制。

- 这一变化的直接价值是更快的冷启动和更少的环境依赖，尤其适合频繁调用的终端型 Agent 工具。

- 官方同时保留了回退路径：如果仍需要旧的 JS 构建，可以固定到更早版本。

- 由于原文信息较短，这条摘要更适合作为产品变更速记，而不是完整深度分析。

## 提取的概念

- [Claude Code](entities/Claude Code.md)

## 原始文章信息

- 作者：@bunjavascript

- 来源：X书签

- 发布时间：2026-04-18

- 原文链接：[https://x.com/bunjavascript/status/2045300183479865602](https://x.com/bunjavascript/status/2045300183479865602)

- 源文章页面：Claude Code 用上了自家的 Bun：v2.1.113 彻底告别 Node.js 运行时

## 个人评注

这类发布说明虽然很短，但对 Tizer 的工作流有明确启发：如果后续需要把终端 Agent 工具链做成更轻量的可分发产品，二进制交付会比依赖 Node.js 运行时更适合 HITL + 自动化混合场景。
