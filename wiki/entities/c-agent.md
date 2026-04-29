---
title: c-agent
type: entity
tags:
- CLI 工具
- 代码生成
- MCP 协议
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3205e1f780804746964ffe94caac39be
notion_id: 3205e1f7-8080-4746-964f-fe94caac39be
---

## 定义

c-agent 是一个用纯 C 语言编写的开源 AI Coding Agent，编译后仅 150KB，可在手机（Termux）、服务器等任意 POSIX 环境运行。功能对标 Claude Code、Aider，支持文件读写、命令执行、多轮对话、工具调用。

## 关键要点

- **极致轻量**：7200 行 C 代码，150KB 二进制，无需 Node.js/Python/Docker 运行时

- **多模型路由**：主力 Agent + Planner（推理模型）+ Explorer（快速模型），子 Agent 通过 pthread 真并行执行

- **MCP 客户端**：731 行 C 实现完整 MCP 协议支持（fork 子进程、JSON-RPC 2.0、工具发现与执行）

- **Telegram 远控**：Long Polling 模式，内置危险命令拦截（rm、sudo、kill -9 等）

- **Termux 硬件集成**：9 个 Termux:API 工具（通知、TTS、剪贴板、相机、电量等）

- **DeepSeek CoT 全链路**：reasoning_content 的流式解析→存储→序列化→持久化→恢复

- **上下文管理**：CJK 友好 token 估算（strlen/3+1），工具配对感知截断

## 档案信息

- **作者**：老码小张（brzhang）

- **语言**：纯 C

- **开源地址**：[https://github.com/coder-brzhang/c-agent](https://github.com/coder-brzhang/c-agent)

- **许可**：未明确

- **适用平台**：Linux/macOS/Android（Termux）

## 关联概念

- [端侧 Agent](concepts/端侧 Agent.md)

- [Agent 命令安全拦截](concepts/Agent 命令安全拦截.md)

- [模型路由](concepts/模型路由.md)

- [MCP 协议](concepts/MCP 协议.md)

## 来源引用

- [摘要：150KB 的 AI Agent，7200 行 C，一个简单的端侧龙虾，能跑在手机上](summaries/摘要：150KB 的 AI Agent，7200 行 C，一个简单的端侧龙虾，能跑在手机上.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493396&idx=1&sn=118ffd524f69ae2a0bdd990151d413ad&chksm=c0dc3bbbe08d86dc8407973601bc40896d35d4a47a401a25bc818298efde2401b9fb24437837#rd)）
