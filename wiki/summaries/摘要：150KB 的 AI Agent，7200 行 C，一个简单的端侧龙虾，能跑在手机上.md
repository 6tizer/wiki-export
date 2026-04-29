---
title: 摘要：150KB 的 AI Agent，7200 行 C，一个简单的端侧龙虾，能跑在手机上
type: summary
tags:
- CLI 工具
- 代码生成
- MCP 协议
- Agent 安全
- 多Agent协作
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881f0bf39e60e93883e8b
notion_url: https://www.notion.so/Tizer/611dce023966485bb1e3d4b8242d4a4f
notion_id: 611dce02-3966-485b-b1e3-d4b8242d4a4f
---

## 一句话摘要

用纯 C 语言编写的 150KB AI Coding Agent（c-agent），证明了完整 Agent 能力（多模型路由、MCP、工具调用、远程控制）可以在极致轻量的二进制中实现并跑在手机上。

## 关键洞察

- **极致轻量 = 新场景**：150KB 编译产物让 AI Agent 首次真正跑在手机（Termux）上，打开了端侧 Agent 的可能性——旧手机变 Agent 服务器、随身 Coding 助手

- **多模型路由 + pthread 并行**：主力/推理/快速三模型按任务类型自动路由，子 Agent 通过 pthread 真并行执行，不是串行等待

- **731 行 C 实现 MCP 客户端**：fork 子进程 + stdin/stdout 管道 + JSON-RPC 2.0，即插即用接入任意 MCP Server

- **危险命令拦截是远程 Agent 的安全底线**：通过运行时 monkey-patching 函数指针实现 rm/sudo/kill 等命令的人工确认机制

- **DeepSeek reasoning_content 全链路贯通**：SSE 解析→存储→序列化→API 回传→持久化→恢复，任何一环断裂都会导致多轮对话失败

## 提取的概念

- [c-agent](entities/c-agent.md)（entity）

- [端侧 Agent](concepts/端侧 Agent.md)

- [Agent 命令安全拦截](concepts/Agent 命令安全拦截.md)

- [模型路由](concepts/模型路由.md)

- [MCP 协议](concepts/MCP 协议.md)

## 原始文章信息

- **作者**：老码小张

- **来源**：微信公众号

- **发布时间**：2026-04-29

- **原文链接**：[https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247493396&idx=1&sn=118ffd524f69ae2a0bdd990151d413ad](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493396&idx=1&sn=118ffd524f69ae2a0bdd990151d413ad)

## 个人评注

c-agent 的核心启发不在于「用 C 写 Agent」本身，而在于证明了 Agent 核心循环（API 调用→JSON 解析→工具执行→上下文管理）的本质复杂度远低于现有工具链的体积所暗示的。对 OpenClaw 的参考价值：1) 多模型路由是降本增效的标准手段；2) 危险命令拦截模式可直接复用到 HITL 场景；3) Termux 硬件工具的思路可扩展到 Agent 与物理世界交互的更多场景。
