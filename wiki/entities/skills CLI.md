---
title: skills CLI
type: entity
tags:
- Agent 技能
- Coding Agent
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f2ebb045e274418eb45215a348be33d5
notion_id: f2ebb045-e274-418e-b452-15a348be33d5
---

## 定义

skills CLI 是一个面向 agent 环境的技能安装工具，用于把带有规范说明文件的能力包快速接入 Claude Code、Cursor、Codex 等 AI 编程或代理执行环境。

## 关键要点

- 它把“工具怎么安装、怎么调用、适合解决什么问题”封装为可分发的技能包，降低 agent 获取外部能力的接入成本。

- 在这篇文章里，wx-cli 通过 skills CLI 暴露为一键安装的 agent 技能，使聊天记录查询能力能够进入 Coding Agent 工作流。

- 这种分发方式的意义不只是安装便利，更在于把原本偏个人脚本化的 CLI 工具包装成可被代理系统消费的能力模块。

- 对 Tizer 的内容与自动化体系来说，这种技能化封装有助于把零散工具逐步纳入统一的 Agent 工具层。

## 关联概念

- [Claude Code Skills](concepts/Claude Code Skills.md)

- [wechat-cli](entities/wechat-cli.md)

## 来源引用

- [摘要：从命令行查询本地微信数据](summaries/摘要：从命令行查询本地微信数据.md)（[原文](https://x.com/jakevin7/status/2044983033418461386)）
