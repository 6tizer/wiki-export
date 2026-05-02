---
title: 多 CLI 统一适配
type: concept
tags:
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2307977a0d9840058274fff3351612dd
notion_id: 2307977a-0d98-4005-8274-fff3351612dd
---

> 通过适配器层将多种 Agent CLI 统一为标准化事件流的工程模式。

## 定义

多 CLI 统一适配是一种系统工程模式，通过定义标准化的适配器接口（bin、buildArgs 闭包、streamFormat、能力探测标记等），将不同厂商的 Agent CLI（如 Claude Code、Codex、Cursor Agent、Gemini CLI 等）统一为一致的事件流输出。Open Design 用约 200 行的 `AGENT_DEFS` 数组完成了 10 个 CLI 的适配，每个 Agent 平均仅需约 20 行配置。

## 关键要点

- `buildArgs` 使用闭包而非纯数据，允许根据运行时参数动态构造命令行参数

- `capabilityFlags` 机制通过解析 `--help` 输出探测 CLI 支持的功能标记，实现版本兼容

- `promptViaStdin` 通过标准输入管道传送 Prompt，绕开 Windows 命令行长度限制（~32KB）

- 四种流式格式（claude-stream-json、json-event-stream、acp-json-rpc、plain）统一转换为类型化 UI 事件

- 新 Agent 接入只需添加约 20 行 TypeScript 配置

## 来源引用

- [摘要：Open Design源码分析](summaries/摘要：Open Design源码分析.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=2&sn=b09ff622c0ea5ba39d0f9533fa955bf6&chksm=cffc0736bf58f08e4a1ea67ea6600b291bf6061dbc64a8a0b30ed6f6576dceec616fc3f6dff0#rd)）
