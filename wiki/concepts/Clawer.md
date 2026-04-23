---
title: Clawer
type: concept
tags:
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b3dcaa770b2d49b3a6f327cf483618de
notion_id: b3dcaa77-0b2d-49b3-a6f3-27cf483618de
---

**定义**

Clawer 是基于 Rust 和 ReAct Agent 框架的 AI 驱动智能爬虫，让 LLM 成为爬虫的"大脑"，自主分析页面结构、决定操作策略和提取数据，实现"目标驱动"替代传统"规则驱动"的爬取模式。

**核心理念**

- 传统爬虫：`人类分析页面 → 编写选择器 → 处理翻页 → 处理异常 → 提取数据`（规则驱动）

- Clawer：`告诉 Agent 要什么 → Agent 自己看页面 → 自己决定怎么操作 → 自己提取数据`（目标驱动）

**架构（四层）**

1. CLI / Desktop UI（Tauri v2 桌面端 + React 前端）

1. ReAct Agent Loop（LLM 驱动的推理决策引擎）

1. 10 个内置工具（browse_page/click/input_text/scroll/extract/execute_js/screenshot/download/web_search/save_result）

1. chromiumoxide（CDP 协议控制真实 Chrome 浏览器）

**技术选型**

- 语言：Rust（高性能、内存安全、单二进制）

- 异步：Tokio

- 浏览器控制：chromiumoxide（CDP 协议）

- LLM：OpenAI 兼容 API（支持 DeepSeek/Ollama/GPT 等）

- 桌面端：Tauri v2（比 Electron 小 10 倍）

**核心优势**

- 真实浏览器：JS 渲染 SPA、需要登录的网站、动态加载内容均可处理

- 自适应：遇到报错自动换方案，遇到翻页自动翻，遇到弹窗自动处理

- 支持本地模型：通过设置 OPENAI_BASE_URL 接 Ollama 等本地部署模型

**来源引用**

- [摘要：我用纯 Rust 写了一个 AI Agent 驱动的爬虫，万物皆可爬](summaries/摘要：我用纯 Rust 写了一个 AI Agent 驱动的爬虫，万物皆可爬.md)（老码小张，2026-04-02）
