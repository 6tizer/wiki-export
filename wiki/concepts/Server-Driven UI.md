---
title: Server-Driven UI
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/4a9a38d01ab34c1399be96106f680003
notion_id: 4a9a38d0-1ab3-4c13-99be-96106f680003
---

## 定义

Server-Driven UI（SDUI）是一种由服务端生成 UI 描述、客户端负责渲染的架构模式，适合确定性的展示型界面场景。

## 关键要点

- 服务端生成 UI 描述（如 DivKit JSON），客户端渲染为原生组件

- 适合确定性 UI：天气卡片、相册画廊、商品展示等，模板预定义，数据填充

- 优势：视觉表现力强、像素级可控

- 劣势：对 LLM 不友好（JSON 结构太复杂，错误率超 50%）、不擅长表单类交互

- 代表工具：Yandex DivKit

- 与 A2UI（Generative UI）形成互补：SDUI 处理展示型、A2UI 处理交互型

## 来源引用

- [摘要：从千问点奶茶说起——Generative UI 协议架构实践](summaries/摘要：从千问点奶茶说起——Generative UI 协议架构实践.md)（老码小张，2026-02-28）
