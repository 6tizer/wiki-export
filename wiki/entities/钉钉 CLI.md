---
title: 钉钉 CLI
type: entity
tags:
- CLI 工具
- Agent 协作模式
- 多Agent协作
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/291ed3c9259f48108ce250e80d888578
notion_id: 291ed3c9-259f-4810-8ce2-50e80d888578
---

## 定义

钉钉 CLI（dingtalk-workspace-cli）是阿里钉钉开源的命令行工具，支持 AI Agent 通过 CLI 命令直接调用钉钉底层能力，专为 Agent 模式设计。

GitHub: [https://github.com/open-dingtalk/dingtalk-workspace-cli](https://github.com/open-dingtalk/dingtalk-workspace-cli)

## 12 个服务模块

aitable、attendance、bot、calendar、chat、contact、devdoc、ding、oa、report、todo、workbench

## Agent 专属功能

- **`--yes`**** 参数**：跳过交互式确认（专为 AI Agent 模式）

- **`--mock`**** 参数**：模拟数据测试，无需连钉钉后台

- **`--dry-run`**** 预览**：所有副作用操作先预览再执行

- 批量熔断：防止 Agent 失控批量操作

- 安全沙箱：所有操作在沙箱内执行

## 来源引用

- [摘要：钉钉飞书集体抛弃 MCP，CLI 才是 Agent 的终局](summaries/摘要：钉钉飞书集体抛弃 MCP，CLI 才是 Agent 的终局.md)
