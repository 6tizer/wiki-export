---
title: 摘要：一个 Rust 写的 Agent OS——OpenFang
type: summary
tags:
- Agent 协作模式
- MCP 协议
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/dcdcd38f38c845fea561bd9007b86cdf
notion_id: dcdcd38f-38c8-45fe-a561-bd9007b86cdf
---

## 一句话摘要

OpenFang 是用纯 Rust 编写的开源 AI Agent 操作系统，将 Agent 从「聊天工具」提升为可自主运行的「系统进程」。

## 关键洞察

- **Agent as Process**：每个 Agent 在 WASM 沙箱中运行，拥有内核级调度、资源计量（fuel + epoch）和隔离机制

- **Hands 机制**：核心创新概念，Agent 按预设计划主动运行并持续生成结果，打包了 HAND.toml、多阶段 Prompt、[SKILL.md](http://skill.md/) 和仪表盘追踪

- **16 层安全系统**：WASM 双重计量沙箱、Ed25519 签名校验、Merkle 审计链、Taint 追踪、SSRF 保护、密钥 zeroization 等

- **极致轻量**：单一二进制文件约 32MB，一行命令安装，不依赖 Python/Docker

- **广泛集成**：支持 40 个消息频道、26 个 LLM 提供商、38 个内置工具、MCP 协议

## 提取的概念

- OpenFang

- [Agent OS](concepts/Agent OS.md)

- Hands 机制

- WASM 沙箱

## 原始文章信息

- **作者**：老码小张

- **来源**：微信公众号

- **发布时间**：2026-02-28

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247492718&idx=1&sn=1fb9d120ba73727335635e89f69d640d)

## 个人评注

OpenFang 的「Agent as Process」理念非常有启发性——调度器不依赖用户输入就能触发 Agent，这正是 Tizer 需要的自动化模式。Hands 机制的设计思路可借鉴到 Wiki Compiler Agent 的定时任务架构中。16 层安全系统在 v0.1 就做到这种程度，体现了对 Agent 生产可用性的严肃态度。
