---
title: Open Design
type: entity
tags:
- AI 设计
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/895b6cbeb1e64dc9a4a5c8f28e56d051
notion_id: 895b6cbe-b1e6-4dc9-a4a5-c8f28e56d051
---

> Anthropic Claude Design 的开源替代方案，由 nexu-io 团队开发的 AI 辅助设计工具。

## 定义

Open Design 是一个开源的 AI 辅助设计平台，采用 Apache-2.0 许可证，约 18,700 行 TypeScript/JavaScript 代码。其核心理念是「Web App + 本地 Daemon + 用户已有的 Agent CLI」，本身不包含任何 AI 模型运行时，全部价值集中在三个层次：统一适配不同 Agent CLI、组装结构化 Prompt Stack、将 Agent 输出解析为可渲染的 Artifact。

## 关键要点

- 支持 10 种 Agent CLI（Claude Code、Codex、Cursor Agent、Gemini CLI 等），通过约 200 行适配器配置实现统一接口

- 技术栈：Next.js 16 + React 18 + Node.js Express Daemon + SQLite + child_process.spawn

- 三种部署拓扑：全本地、Vercel + 本地 Daemon、Vercel 直连 API（BYOK）

- 六重反 AI-Slop 质量控制机制，全部以 Prompt 指令实现

- Skill 和 Design System 采用文件式零注册扩展架构

- 项目地址：[https://github.com/nexu-io/open-design](https://github.com/nexu-io/open-design)

## 来源引用

- [摘要：Open Design源码分析](summaries/摘要：Open Design源码分析.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=2&sn=b09ff622c0ea5ba39d0f9533fa955bf6&chksm=cffc0736bf58f08e4a1ea67ea6600b291bf6061dbc64a8a0b30ed6f6576dceec616fc3f6dff0#rd)）
