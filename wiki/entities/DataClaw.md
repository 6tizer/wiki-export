---
title: DataClaw
type: entity
tags:
- 知识管理
- CLI 工具
status: 审核中
confidence: medium
last_compiled: '2026-04-10'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a0ebe1a3e25c43c896106b9f4dac3f45
notion_id: a0ebe1a3-e25c-43c8-9610-6b9f4dac3f45
---

## 定义

DataClaw 是一个开源命令行工具（`pip install dataclaw`），允许开发者将本地 AI 编程工具（Claude Code、Codex、Gemini CLI 等）的对话记录整理成标准格式数据集，并可选择一键上传到 Hugging Face 公开共享。

## 关键要点

- 内置多层隐私保护：自动脱敏文件路径、用户名、密钥/令牌/密码

- 五步流程：选来源 → 确认范围 → 本地预览 → 隐私扫描 → 确认推送

- 每步需人工确认，不会自动上传

- 所有导出数据集在 Hugging Face 上统一标记 `dataclaw` 标签

- 诞生背景：回应 Anthropic 蒸馏争议，强调开发者数据主权

- 局限：自动脱敏非万能（作者坦承 "NOT foolproof"）

## 来源引用

- [摘要：Anthropic 破防，DataClaw 开源！](summaries/摘要：Anthropic 破防，DataClaw 开源！.md)（GitHubDaily，2026-02-28）— 介绍 DataClaw 工具的诞生背景和使用方式
