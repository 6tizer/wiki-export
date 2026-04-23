---
title: AI 沙箱
type: concept
tags:
- 安全/隐私
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/872d2907b6fb403c99d6d1e7b367b55b
notion_id: 872d2907-b6fb-403c-99d6-d1e7b367b55b
---

## 定义

AI 沙箱是为 AI Agent 提供安全隔离执行环境的基础设施，防止 Agent 执行的代码或操作影响宿主系统或泄漏敏感数据。是 Agent 基础设施层的关键组件。

## 关键要点

- **核心价值**：在 Agent 和外部数字世界之间设立防火墙，拦截敏感信息泄漏、恶意指令注入和有害代码执行

- **多层级隔离**：

  - **Session 级**：如 OpenClaw 的 `sandbox.mode`（non-main / all）

  - **代码执行级**：如 OpenSandbox，提供独立容器运行环境

  - **网络级**：网络隔离防止数据外泄

- **代表项目**：OpenSandbox（阿里开源）、E2B、各云厂商沙箱服务

- **发展趋势**：随着 OpenClaw 等 Agent 平台的爆发，沙盒托管成为新的基础设施需求

## 代表项目：OpenSandbox

OpenSandbox 是阿里开源的 AI 智能体生产级沙盒，支持多语言安全代码执行、浏览器自动化和网络隔离，兼容 Docker 和 Kubernetes 部署。

- **双模式部署**：Docker（快速测试）+ Kubernetes（生产部署）

- **社区热度**：GitHub 2000+ 星标

- **规划功能**：Go SDK、持久化存储等企业级特性

- **与 OpenClaw sandbox 的关系**：互补——OpenClaw 的 `sandbox.mode` 是 session 级隔离，OpenSandbox 提供更底层的代码执行隔离

## 来源引用

- [摘要：Foundry Hosted Agents：每个 Agent 都需要自己的“电脑”](summaries/摘要：Foundry Hosted Agents：每个 Agent 都需要自己的“电脑”.md)（[原文](https://x.com/satyanadella/status/2047033636923568440)）

- [摘要：ThinkInAI Weekly AI周刊 VOL.42 Opus 4.7 来了、Qwen 开源 35B、Agent 工具链全面升级](summaries/摘要：ThinkInAI Weekly AI周刊 VOL.42 Opus 4.7 来了、Qwen 开源 35B、Agent 工具链全面升级.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA4ODg0NDkzOA%3D%3D&mid=2247514009&idx=1&sn=bf15a5a46c8fceb7d84d0b3760d4ade9&chksm=91d6d8d58aad639487948529ced9d124bf6b7e77e01022df6a25570b93843ec362146982cbe9#rd)）

- [摘要：阿里开源 OpenSandbox：让 AI Agent 不再「裸奔」的沙箱基础设施](summaries/摘要：阿里开源 OpenSandbox：让 AI Agent 不再「裸奔」的沙箱基础设施.md)（AI工程化, 2026-03-01）

- [摘要：OpenClaw正在成为新的交互入口，AI投资人：这4个生态位，短期内会爆发机会](summaries/摘要：OpenClaw正在成为新的交互入口，AI投资人：这4个生态位，短期内会爆发机会.md)（Bob/Founder Park, 2026-02-28）— 提及安全层和沙盒托管作为 Infra 层重构的一部分

- [原文链接](https://x.com/Gorden_Sun/status/2033941005368774953)｜[摘要：阿里开源 OpenSandbox：让 AI Agent 不再「裸奔」的沙箱基础设施](summaries/摘要：阿里开源 OpenSandbox：让 AI Agent 不再「裸奔」的沙箱基础设施.md)

- [摘要：OpenClaw龙虾之父演讲：从0-1打造突破性AI Agent的复盘回顾](summaries/摘要：OpenClaw龙虾之父演讲：从0-1打造突破性AI Agent的复盘回顾.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzE5ODAwODU4Mw%3D%3D&mid=2247488510&idx=1&sn=9980ddbc1a5ed9c25fd0ee17afa33be3&chksm=97308abf31546c3a1117f4ed73d18e9836b956478477907f2783685a2c3eea9b61b55f810691#rd)）

## 关联概念

- [Foundry Agent Service](entities/Foundry Agent Service.md)

- [持久状态](concepts/持久状态.md)

- [OpenClaw](entities/OpenClaw.md)

- [个人 AI 操作系统](concepts/个人 AI 操作系统.md)

- [心跳系统](concepts/心跳系统.md)

- [Multi-Agent 群聊](concepts/Multi-Agent 群聊.md)
