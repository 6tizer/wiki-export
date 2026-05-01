---
title: OpenFang
type: entity
tags:
- 多Agent协作
- MCP 协议
status: 审核中
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/850ba7b88f8f4d2baa507f6626f550d8
notion_id: 850ba7b8-8f8f-4d2b-aa50-7f6626f550d8
---

## 定义

OpenFang 是用纯 Rust 编写的开源 AI Agent 操作系统（Agent OS），将 Agent 视为可自主运行的系统进程而非被动响应的聊天机器人。

## 关键要点

- 13.7 万行 Rust 代码，MIT 协议，零 Clippy 警告

- 核心创新 **Hands 机制**：Agent 按预设计划主动运行，持续生成结果并汇报

- 每个 Agent 在 WASM 沙箱中运行，拥有内核级调度和资源计量

- 16 层深度防御安全系统（WASM 计量、Ed25519 签名、Merkle 审计链等）

- 单一二进制文件约 32MB，一行命令安装

- 支持 40 个消息频道、27 个 LLM 提供商、38 个内置工具、MCP 协议

- 提供从 OpenClaw 一键迁移工具

- GitHub: [https://github.com/RightNow-AI/openfang](https://github.com/RightNow-AI/openfang)

- 官网: [https://openfang.sh](https://openfang.sh/)

## 来源引用

- [摘要：一个 Rust 写的 Agent OS——OpenFang](summaries/摘要：一个 Rust 写的 Agent OS——OpenFang.md)（老码小张，2026-02-28）

- [摘要：CoPaw、OpenFang、ClawPhD、Eggent、RedBookSkills 工具合集](summaries/摘要：CoPaw、OpenFang、ClawPhD、Eggent、RedBookSkills 工具合集.md)（每日AI新工具，2026-02-28）

- [摘要：OpenClaw 生态七件套：那些大项目之外值得关注的小众开源神器](summaries/摘要：OpenClaw 生态七件套：那些大项目之外值得关注的小众开源神器.md)（@_0xKenny (Kenny.eth)，X书签，2026-03）

- [摘要：OpenClaw 生态七件套：那些大项目之外值得关注的小众开源神器](summaries/摘要：OpenClaw 生态七件套：那些大项目之外值得关注的小众开源神器.md)（X书签，2026-03）
