---
title: 端侧 Agent
type: concept
tags:
- 模型部署
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/da9f9272e2bd4e0489ce8842d0d776da
notion_id: da9f9272-e2bd-4e04-89ce-8842d0d776da
---

## 定义

端侧 Agent 指在移动设备、嵌入式设备等边缘终端直接运行的 AI Agent，区别于依赖云端服务器的传统方案。核心挑战是在极有限的存储、内存和算力下实现完整的 Agent 循环（感知→规划→执行→反馈）。

与「端侧模型」的区别：端侧模型侧重模型推理的本地化部署，端侧 Agent 则强调完整的 Agent 工具链（文件操作、命令执行、多轮对话、工具调用）在终端设备上的运行。

## 关键要点

- **体积约束**：运行时 + 二进制需控制在 MB 级以内（c-agent 实现了 150KB）

- **无依赖运行**：不依赖 Node.js、Python、Docker 等重量级运行时

- **硬件交互**：可调用设备传感器和系统 API（相机、通知、TTS、剪贴板等）

- **远程协作**：通过 Telegram Bot 等方式实现远程控制，将旧手机变成 Agent 服务器

- **模型调用仍依赖云端**：Agent 本体在端侧运行，但 LLM 推理通常仍调用云端 API

## 关联概念

- [c-agent](entities/c-agent.md)

- [Agent 命令安全拦截](concepts/Agent 命令安全拦截.md)

- [模型路由](concepts/模型路由.md)

## 来源引用

- [摘要：150KB 的 AI Agent，7200 行 C，一个简单的端侧龙虾，能跑在手机上](summaries/摘要：150KB 的 AI Agent，7200 行 C，一个简单的端侧龙虾，能跑在手机上.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493396&idx=1&sn=118ffd524f69ae2a0bdd990151d413ad&chksm=c0dc3bbbe08d86dc8407973601bc40896d35d4a47a401a25bc818298efde2401b9fb24437837#rd)）
