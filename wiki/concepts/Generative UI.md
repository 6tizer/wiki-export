---
title: Generative UI
type: concept
tags:
- 前端开发
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/14dea533298948f7b4626c178d5ef869
notion_id: 14dea533-2989-48f7-b462-6c178d5ef869
---

## 定义

Generative UI 是一种由 AI 根据对话上下文实时生成可交互用户界面的技术范式，使对话框从纯文本交互容器进化为承载任意 UI 的交互容器。

## 关键要点

- 核心理念：界面不再是预先设计好的路径，而是 AI 根据当下语境实时构建的

- 千问 App 演示「一句话点 40 杯奶茶」是典型案例

- Google 发布 A2UI（Agent-to-UI）协议，Vercel AI SDK 3.0 加入 streamUI 支持

- 实践经验：组件越少 LLM 生成准确率越高（从 15 种砍到 6 种，错误率从 ~20% 降到接近 0）

- 为 LLM 设计数据结构原则：扁平优于嵌套、枚举优于自由文本、少字段优于多字段

- 交互闭环是关键：表单提交后回到对话流，而非对话的终点

## 关联概念

- [Cursor Canvas](concepts/Cursor Canvas.md)

- [Docs Canvas Skill](concepts/Docs Canvas Skill.md)

- [持久化工件](concepts/持久化工件.md)

## 来源引用

- [摘要：从千问点奶茶说起——Generative UI 协议架构实践](summaries/摘要：从千问点奶茶说起——Generative UI 协议架构实践.md)（老码小张，2026-02-28）

- [摘要：Cursor can now respond by creating interactive canvases to visually represent information.](summaries/摘要：Cursor can now respond by creating interactive canvases to visually represent information.md)（@cursor_ai，2026-04-15）

- [摘要：最近刷屏的Flipbook，想把互联网彻底变成实时生成的无限世界](summaries/摘要：最近刷屏的Flipbook，想把互联网彻底变成实时生成的无限世界.md)（硅星人Pro，2026-04-29）
