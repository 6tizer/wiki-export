---
title: PersonalAgent
type: entity
tags:
- Harness 工程
- AI 产品
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/994cd01a2ba247c09f84751bf4615161
notion_id: 994cd01a-2ba2-47c0-9f84-751bf4615161
---

## 定义

PersonalAgent 是由 @trashpandaemoji 开发的桌面级 Agent Harness，基于 Electron 构建，底层使用 @badlogicgames 的 Pi coding agent。它是一个完全通过 vibe coding 生成的个人化 Agent 控制台，强调「拥有自己的 harness」，不依赖大厂锁定。

别名：PA

## 关键要点

- 基于 Electron 的桌面应用，支持多线程对话管理，灵感来自 OpenAI Codex CLI

- 可搭配任意模型和任意 harness，不受大厂锁定

- 内置 iOS 伴侣应用，通过 Tailscale 网络远程监控 Agent 运行

- 实现了 Agent Lifecycle Management：定时任务、Deferred Resume、队列跟进

- Auto Mode 延续模式：注入 continuation prompt 让 Agent 自主循环工作

- 内嵌 Excalidraw 用于向 Agent 传递手绘图和截图标注

- 内置语音输入（基于 OpenAI dictation endpoint）

- 内嵌知识库：Skills + [AGENTS.md](http://agents.md/) + 自由笔记，采用纯 Markdown 文件夹方案（无 RAG）

- 参考了 Karpathy 的 Obsidian 知识库思路，但将其集成到 harness 内部

## 技术细节

- 运行平台：Electron（桌面）+ iOS（监控伴侣）

- 底层 Agent：Pi coding agent

- 网络：Tailscale 用于远程访问

- 语音：OpenAI dictation / Whisper

- 知识库：Git 仓库 + 自动同步引擎，纯 Markdown，无 RAG

## 来源引用

- [摘要：Personal Agent](summaries/摘要：Personal Agent.md)（[原文](https://x.com/trashpandaemoji/status/2048026069375029267)）
