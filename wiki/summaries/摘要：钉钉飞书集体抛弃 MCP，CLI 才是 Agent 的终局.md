---
title: 摘要：钉钉飞书集体抛弃 MCP，CLI 才是 Agent 的终局
type: summary
tags:
- MCP 协议
- CLI 工具
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: MCP, Agent, 行业观察
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1603d950c2e843b8ad55ea3615a7da85
notion_id: 1603d950-c2e8-43b8-ad55-ea3615a7da85
---

## 一句话摘要

钉钉和飞书相继推出官方 CLI 工具（dws 和 lark-cli），绕开 MCP 协议，以命令行作为 Agent 操作软件的接口，基准测试显示 CLI 比 MCP 成本低17倍、可靠性高28%。

## 关键洞察

- **MCP vs CLI 成本差距**：CLI 1,365 tokens vs MCP 44,026 tokens（查仓库语言任务，32倍差距），每月1万次操作成本 CLI $3.2 vs MCP $55.2（17倍）

- **MCP 的根本问题**：schema bloat，每次对话把所有工具定义塞进上下文，GitHub MCP 服务器43个工具定义光一个就4026 tokens

- **飞书三层架构**：Shortcuts（+前缀快捷命令）、API Commands（100+条）、Raw API（2500+端点全覆盖）

- **钉钉企业管理优势**：OA 审批、考勤、DING 消息是飞书 CLI 没有的

- **CLI 是 LLM 的母语**：训练数据有数十亿行 shell 命令，pipe/组合/文本流是天然接口

- **MCP 不会死**：退回到开放生态接入协议层，类似 SOAP 的命运

## 提取的概念

- CLI-first 架构

- MCP 协议（已存在）

- lark-cli

- dingtalk-workspace-cli

## 原始文章信息

- **作者**: AGI Hunt

- **来源**: 微信公众号

- **发布时间**: 2026-03-28

## 个人评注

CLI-first 架构对 Tizer 的 OpenClaw 工作流设计有重要参考意义，飞书 CLI 的2500+ API 端点覆盖可以大幅扩展 Agent 操作飞书的能力。
