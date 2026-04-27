---
title: vllm-swift
type: entity
tags:
- 模型部署
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1dd1902d66c04bf4b0124b5f50046bcc
notion_id: 1dd1902d-66c0-4bf4-b012-4b5f50046bcc
---

## 定义

vllm-swift 是一个面向 Apple Silicon 的原生 Swift/Metal 推理后端，为 vLLM 提供无 Python 的推理热路径。由 Tom Turney（@no_stp_on_snek）开发并开源，通过 Homebrew 一键安装。

**别名**：vLLM Swift Backend

## 关键要点

- 推理热路径完全使用 Swift 实现，不依赖 Python，显著提升吞吐量和扩展性

- 基于 Apple Metal GPU 框架，原生支持 Apple Silicon（M1/M2/M3/M4）

- 支持 Homebrew 安装：`brew tap TheTom/tap && brew install vllm-swift`

- GitHub 仓库：[TheTom/vllm-swift](https://github.com/TheTom/vllm-swift)

- 目前处于 Beta 测试阶段，正在招募测试者

## 关联概念

- [vLLM](entities/vLLM.md)（父项目）

## 来源引用

- [摘要：Apple Silicon 上的 vLLM 终于原生 Swift/Metal 了！](summaries/摘要：Apple Silicon 上的 vLLM 终于原生 Swift-Metal 了！.md)（[原文](https://x.com/berryxia/status/2047523226272862372)）
