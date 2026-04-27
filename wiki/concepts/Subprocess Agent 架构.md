---
title: Subprocess Agent 架构
type: concept
tags:
- 多Agent协作
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/407c6a7988d1440b92cb4442db2faaf8
notion_id: 407c6a79-88d1-440b-92cb-4442db2faaf8
---

## 定义

Subprocess Agent 架构是一种将 AI Agent 封装为子进程（subprocess）的集成模式。Agent 作为独立进程运行，通过 stdout 输出结构化 JSON 事件流（如 `tool_use`、`text`、`step_start`、`step_finish`），调用方只需 spawn 进程并解析 JSON 即可完成集成。

## 关键要点

- **语言无关**：任何能 spawn 子进程、解析 JSON 的语言均可接入（Java、Go、Python、Node 等）

- **不绑 SDK 版本**：无需安装特定语言的 SDK 包，避免依赖冲突

- **模型抽象**：模型作为 `provider/model` 字符串传入，一行参数切换模型

- **事件流可观测**：stdout 可直接 `> events.jsonl` 保存、`| tee | grep` 处理

- **vs SDK 集成**：SDK（如 Claude Agent SDK）在 Python 对象层集成，Subprocess 在 stdout 层集成，后者对非 Python 后端更友好

- **典型实现**：OpenCode 的 `opencode run --format json` 命令

## 适用场景

- 后端语言不是 Python（如 Java + Spring）

- 需要快速原型验证多 Agent 流水线

- 需要模型私有化部署、灵活切换

## 来源引用

- [摘要：OpenCode + OMO ：小白也能快速搭建AI Agent应用](summaries/摘要：OpenCode + OMO ：小白也能快速搭建AI Agent应用.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU0MDcyMDQ0Nw%3D%3D&mid=2247484791&idx=1&sn=8e0baa4136cf4b90cadf5e23e3dee12a&chksm=fa23c722fefdd30dfabd5ec53292f22f64bcd97ca133c36264b4804657c84ae1a0e8ed4e31c1#rd)）

## 关联概念

- [OpenCode](entities/OpenCode.md)

- [oh-my-opencode](entities/oh-my-opencode.md)

- [双 Agent 互查范式](concepts/双 Agent 互查范式.md)
