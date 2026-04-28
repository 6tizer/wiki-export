---
title: MMX-CLI
type: entity
tags:
- Agent 技能
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/20a63c56a86e467593074075631eda7e
notion_id: 20a63c56-a86e-4675-9307-4075631eda7e
---

## 定义

MMX-CLI是MiniMax为AI Agent专门设计的全模态命令行工具，使Agent可在Claude Code、OpenClaw等环境中通过一条`mmx`命令原生调用MiniMax的全模态模型能力。

## Agent专项优化设计原则

1. **输出隔离与纯数据模式**：进度条划归stderr，stdout只输出干净的文件路径/JSON

1. **语义化状态码**：不同失败类型有独立退出码，Agent无需读英文报错即可判断重试逻辑

1. **非阻塞与异步任务控制**：`--async`支持并行多任务

## 七种全模态能力

1. 图片生成

1. 视频生成

1. 语音合成

1. 音乐创作

1. 图片理解

1. 实时搜索

1. 对话回应

## 安装

```bash
npx skills add MiniMax-AI/cli -y -g
npm install -g mmx-cli
```

无缝接入MiniMax Token Plan，无额外费用。

## 设计启示

MMX-CLI代表了面向Agent优化的CLI工具设计范式，其输出隔离、语义化错误码、非阻塞异步三大设计原则对开发任Agent可调用的工具有很大参考价值。

## 来源引用

- [摘要：MiniMax 发布 MMX-CLI：为 Agent 设计的全模态命令行工具](summaries/摘要：MiniMax 发布 MMX-CLI：为 Agent 设计的全模态命令行工具.md)（MiniMax 稀宇科技，2026-04-09）
