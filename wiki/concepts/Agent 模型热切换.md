---
title: Agent 模型热切换
type: concept
tags:
- 模型部署
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/96dc5e788bf44dccabf9d7d7bd7791df
notion_id: 96dc5e78-8bf4-4dcc-abf9-d7d7bd7791df
---

## 定义

Agent 模型热切换是指在 Agent 类 CLI 工具（如 Claude Code、Codex、OpenClaw 等）运行过程中，无需重启终端或关闭当前会话，即可实时更换底层 LLM 模型供应商或模型版本的技术能力。切换后下一轮对话立即使用新模型响应。

## 关键要点

- 热切换的前提是 Agent 工具在每轮对话前动态读取模型配置（如 settings.json），而非启动时一次性加载

- 切换时机必须在模型空闲状态（即上一轮响应完成后），否则会因请求中断导致报错

- 典型应用场景：日常小任务用低成本模型，关键任务切换到高性能模型，实现成本管理

- 代表工具：CC Switch 通过修改配置文件实现跨 Agent 工具的热切换

## 关联概念

- [CC Switch](entities/CC Switch.md)

- [API 故障转移路由](concepts/API 故障转移路由.md)

## 来源引用

- [摘要：这个51K星标的开源神器，让任何Agent都能一键切换所有模型。](summaries/摘要：这个51K星标的开源神器，让任何Agent都能一键切换所有模型。.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681944&idx=1&sn=e3f6218daedb4dbfc9931b6a3adcbc8c&chksm=f16914fa8815127eb4dc837b85b4005493b1572de01a24a2ae5d1a9a48a47169742d7150ac69#rd)）
