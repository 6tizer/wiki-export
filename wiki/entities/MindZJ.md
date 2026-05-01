---
title: MindZJ
type: entity
tags:
- 知识管理
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c0d319af83084ecdbd445186216c5b29
notion_id: c0d319af-8308-4ecd-bd44-5186216c5b29
---

## 一句话定义

MindZJ 是一个 AI 原生、CLI 优先、本地离线的开源笔记应用，试图把本地知识管理、模型调用与自动化接口统一到同一套 Rust 内核中。

## 关键要点

- 使用 Tauri 2.0、SolidJS、CodeMirror 6、Rust 与 tantivy 构建，多平台可运行

- 支持本地 Markdown 文件存储，并接入 Ollama、Claude、OpenAI

- CLI 与桌面 GUI 共用核心 API，适合脚本化搜索与 AI 问答

- 插件设计强调 WebWorker 沙盒与权限 manifest，但生态仍处早期

## 关联概念

- [本地优先](concepts/本地优先.md)

- [内核级 AI 集成](concepts/内核级 AI 集成.md)

- [CLI/GUI 共享内核](concepts/CLI-GUI 共享内核.md)

- [插件权限 Manifest](concepts/插件权限 Manifest.md)

## 来源引用

- [摘要：MindZJ：用 Claude Opus 4.7 一周造出的本地优先 Obsidian 开源替代品](summaries/摘要：MindZJ：用 Claude Opus 4.7 一周造出的本地优先 Obsidian 开源替代品.md)（[原文](https://x.com/claudeai/status/2045248224659644654)）
