---
title: Pixelle-Video
type: entity
tags:
- 内容自动化
- 视频/3D
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/444148d511394043873d581f91cd8469
notion_id: 444148d5-1139-4043-873d-581f91cd8469
---

## 定义

Pixelle-Video 是阿里 AIDC（阿里巴巴国际站数字商务集团人工智能团队）开源的 **AI 全自动短视频引擎**。用户只需提供一个主题，即可在几分钟内自动生成包含文案、画面、配音、BGM 的完整短视频。

**别名**：Pixelle Video

## 关键要点

- 采用模块化流水线架构，将短视频生产拆分为写稿（LLM）、出图（ComfyUI / RunningHub）、配音（TTS / 声音克隆）、视频合成四个环节

- 支持通义千问、GPT-4o、DeepSeek 等多种 LLM 作为脚本生成后端

- 内置声音克隆功能（Index-TTS），可用用户自己的声音配音

- 提供 Windows 一键整合包和 macOS/Linux 命令行部署，对非开发者极度友好

- 支持本地零成本运行（Ollama + ComfyUI 本地部署）

- 生成作品可自动推送到微信、飞书、钉钉、Telegram 等平台

- GitHub 6.2k star，生态包含多种 TTS 工作流、视频模板、ComfyUI 节点集成

- 配套项目：Pixelle-MCP（将 ComfyUI 变为 MCP 服务器）、FlowGram（AI 应用流程框架）

## 来源引用

- [摘要：阿里把视频生产线开源了：一个人，真的能干翻整个MCN](summaries/摘要：阿里把视频生产线开源了：一个人，真的能干翻整个MCN.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzYzNzgzNzQ0OQ%3D%3D&mid=2247483895&idx=1&sn=7346fd7d8397d1271cd0c780157dfefc&chksm=f1e707ee7416ed4be2b8d89c794c3153196290af1006554d832ff3bef8d31ff55e3366242af5#rd)）
