---
title: Programmatic Tool Calling
type: concept
tags:
- Harness 工程
- 代码生成
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c76e369c6e5748e598287b2940504cec
notion_id: c76e369c-6e57-48e5-9828-7b2940504cec
---

## 定义

Programmatic Tool Calling（PTC）是一种 Agent 执行范式，将工具调用逻辑从对话式逐轮调用转移到沙箱化代码执行环境中。模型编写 Python 程序，在单次沙箱运行中完成检索、过滤、分支、循环、写盘和操作，而非跨多轮对话重复推导执行计划。

别名：Sandbox Tool Calling、Code-as-Execution-Primitive

## 关键要点

- 工具以 Python 可调用函数形式暴露给模型，模型生成调用脚本而非逐轮 JSON tool_call

- 20+ 次工具调用可在一次沙箱运行中完成，编排器仅接收摘要和结构化元数据

- 中间数据存储在 Python 变量和文件中，不回流到上下文窗口

- 四大优势：降低延迟（并行批量执行）、提升可靠性（代码分支替代脆弱对话链）、增强一致性（脚本可保存为 Skill 复用）、上下文效率（仅返回摘要/最终输出）

- 与 Sub-agent 协同时，编排 Agent 可通过代码批量启动并行子 Agent

## 来源引用

- [摘要：The harness as the context manager](summaries/摘要：The harness as the context manager.md)（[原文](https://x.com/tonygentilcore/status/2049482833111232694)）
