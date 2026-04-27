---
title: 摘要：free-claude-code：0元白嫖 Claude Code 全套工程能力
type: summary
tags:
- Harness 工程
- 代码生成
- CLI 工具
status: 已审核
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68816bae2fc77f6eb4ce70
notion_url: https://www.notion.so/Tizer/146f4b6ecf8545ee98c205248d26d9e0
notion_id: 146f4b6e-cf85-45ee-98c2-05248d26d9e0
---

## 一句话摘要

free-claude-code 是一个开源本地代理项目，可将 Claude Code 客户端的全部 harness 工程能力（上下文管理、记忆管理、skill 封装、工具调用、subagent）保留，同时将底层模型替换为免费或低成本替代方案。

## 关键洞察

- **Harness 与模型解耦**：该项目的核心价值在于证明 Claude Code 的 harness 工程能力（上下文管理、记忆、skill、工具调用、subagent 等）可以与底层模型完全解耦，用户可接入 GLM 4.7、Kimi K2 Thinking、DeepSeek R1 等免费模型

- **Thinking Blocks 对齐**：代理层对推理型模型（如 R1、Kimi）的思考链做了格式对齐，使 thinking blocks 在 Claude Code UI 中正常显示，而非混为一团

- **启发式工具调用解析**：针对不规范输出 tool call 的开源模型，代理内置启发式解析器，自动将输出转换为 Claude Code 可识别的格式

- **垃圾请求拦截与并发控制**：自动过滤 Claude Code 生成标题、探测网络等非核心请求，节省免费额度；并对 subagent 强制串行，适应免费模型的速率限制

- **远程操控能力**：内置 Discord/Telegram Bot + 语音消息（本地 Whisper 或 NVIDIA 转写），支持手机远程触发家中电脑执行编码任务

## 提取的概念

- [free-claude-code](entities/free-claude-code.md)

- [NVIDIA NIM](entities/NVIDIA NIM.md)

- [OpenRouter](entities/OpenRouter.md)

- [OpenAI 兼容 API 代理](concepts/OpenAI 兼容 API 代理.md)

## 原始文章信息

- **作者**：@VincentLogic

- **来源**：X书签

- **发布时间**：2026-04-23

- **原文链接**：[https://x.com/VincentLogic/status/2047310943202181608](https://x.com/VincentLogic/status/2047310943202181608)

- **GitHub 仓库**：[https://github.com/Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)

## 个人评注

该项目体现了 harness 与模型解耦的趋势：Claude Code 最有价值的不是底层模型，而是其 harness 工程层（上下文管理、skill 沉淀、subagent 编排）。对 Tizer 的 OpenClaw 项目而言，这验证了「Thin Harness, Fat Skills」理念的可行性——harness 层可以对接任意模型后端。不过评论区也指出，该方案本质上只是改环境变量就能实现的配置切换，且失去了 Claude 模型本身的智能，实际效果取决于替代模型的能力上限。
