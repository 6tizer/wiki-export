---
title: 飞书 CLI
type: entity
tags:
- CLI 工具
- 多Agent协作
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e570cc2b9cef4267bc5eeef415317fa8
notion_id: e570cc2b-9cef-4267-bc5e-eef415317fa8
---

## 定义

飞书 CLI（lark-cli）是字节跳动飞书开源的命令行工具，支持 AI Agent 通过 CLI 直接操作飞书全套能力，绕开 MCP，采用三层架构覆盖 2500+ OpenAPI 端点。

GitHub: [https://github.com/larksuite/cli](https://github.com/larksuite/cli)

## 三层架构

1. **Shortcuts（****`+`**** 前缀）**：内置智能默认值的快捷命令，参数大幅简化，对 Agent 最友好

1. **API Commands**：100+ 条命令，与飞书平台 API 一一对应

1. **Raw API**：直接调用飞书底层 2500+ OpenAPI 端点，万能逃生舱

## 主要特性

- **`lark-cli schema`**：查看任何 API 方法的参数和所需权限

- **`lark-cli doctor`**：一键检查配置、认证和网络连通性

- **`--page-all`**：自动翻页，无需手动处理分页

- **`--as user/bot`**：切换用户/应用身份

- 内置 **19 个 AI Skill**，可直接装进 Claude Code

- 支持五种输出格式：JSON/NDJSON/table/CSV/pretty

## 来源引用

- [摘要：钉钉飞书集体抛弃 MCP，CLI 才是 Agent 的终局](summaries/摘要：钉钉飞书集体抛弃 MCP，CLI 才是 Agent 的终局.md)
