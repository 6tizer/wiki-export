---
title: CodeBrain
type: concept
tags:
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6f0ed5d633cb44699cd00dec4e8bc7c4
notion_id: 6f0ed5d6-33cb-4469-9cd0-0dec4e8bc7c4
---

## 定义

CodeBrain是Feeling AI开发的代码智能增强框架，能在Terminal-Bench 2.0指标上领跑全球，并将各种底座模型的Token成本大幅降低。

## 常见痛点：缺乏编译器级别的诊断

当前顶尖Agent在处理中小型文件时表现惊艳，但进入多语言、数百万行代码的Monorepo时，依赖原始的文本搜索（grep）和文件读取（cat）导致低效、模糊和脂弱。

## 五层架构

1. **核心层**：模型、配置、工作区、工具链

1. **引擎层**：LSP引擎+降级链，tree-sitter搜索

1. **工具层**：8个原子操作

1. **技能层**：上下文诊断，影响分析，符号搜索

1. **MCP服务器**：11个面向意图的工具

## 核心指标

- CodeBrain-1.5：Terminal-Bench 2.0成绩81.3%，领跑全球

- 在Claude Opus 4.6上节省63.9% Token成本（$313.0降至$112.9）

- 优雅降级链：LSP不可用时自动切换到CLI工具

## GitHub

[https://github.com/feelingai-team/CodeBrain](https://github.com/feelingai-team/CodeBrain)

## 来源引用

- [摘要：最强大脑组合！全球SOTA的逻辑和记忆CodeBrain-1&MemBrain1.5同时开源](summaries/摘要：最强大脑组合！全球SOTA的逻辑和记忆CodeBrain-1&MemBrain1.5同时开源.md)（机器之心，2026-04-08）
