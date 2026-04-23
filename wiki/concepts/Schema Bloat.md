---
title: Schema Bloat
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d5ca6bdfdd954db2b97887a5cc6d2b5d
notion_id: d5ca6bdf-dd95-4db2-b978-87a5cc6d2b5d
---

## 定义

Schema Bloat（工具模式膨胀）是 MCP 协议的核心效率问题：每次对话将所有已注册工具的完整描述（JSON Schema）全部塞入上下文窗口，导致 Token 消耗成本暴增，是 CLI 相比 MCP 有巨大优势的根本原因。

## 数据证据

- GitHub MCP Server 工具数：43 个，一个工具定义占 4,026 tokens

- 单项查询：MCP 消耗 44,026 tokens vs CLI 仅 1,365 tokens（32 倍差距）

- 每月成本：MCP $55.2 vs CLI $3.2（17 倍差距）

## 为什么难修复

Schema 膨胀的机制恰恰是 MCP 设计的核心（工具自描述），无法绕开。CLI 通过 `--help` 按需读取单个子命令的参数说明，不会将所有命令的文档一股脑塞进上下文。

## 来源引用

- 摘要：Solana AI 黑客松：400+ 项目角逐，哪些已发币项目值得关注？
