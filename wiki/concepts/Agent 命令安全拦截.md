---
title: Agent 命令安全拦截
type: concept
tags:
- Agent 安全
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0fd1a06895484800a43cefbc38c58f0d
notion_id: 0fd1a068-9548-4800-a43c-efbc38c58f0d
---

## 定义

Agent 命令安全拦截是一种在 AI Agent 执行系统命令前，对高危操作进行自动检测和人工确认的安全机制。属于 Agent 安全和 Harness 工程的关键组成部分，确保 Agent 在自主执行命令时不会造成不可逆的系统损害。

## 关键要点

- **拦截目标**：`rm -rf`、`sudo`、`kill -9`、`mkfs`、`dd`、`chmod 777` 等破坏性命令

- **确认机制**：检测到危险命令后暂停执行，等待人工确认（Y/N），超时自动拒绝

- **实现方式**：运行时动态替换工具函数指针（monkey-patching），插入确认逻辑层

- **远程场景尤为关键**：通过 Telegram 等远程控制 Agent 时，命令拦截是防止误操作的最后防线

- **与 HITL 的关系**：是 Human-in-the-Loop 在命令执行层面的具体实现

## 关联概念

- [c-agent](entities/c-agent.md)

- [端侧 Agent](concepts/端侧 Agent.md)

- [MCP 协议](concepts/MCP 协议.md)

## 来源引用

- [摘要：150KB 的 AI Agent，7200 行 C，一个简单的端侧龙虾，能跑在手机上](summaries/摘要：150KB 的 AI Agent，7200 行 C，一个简单的端侧龙虾，能跑在手机上.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493396&idx=1&sn=118ffd524f69ae2a0bdd990151d413ad&chksm=c0dc3bbbe08d86dc8407973601bc40896d35d4a47a401a25bc818298efde2401b9fb24437837#rd)）
