---
title: Forward Proxy
type: concept
tags:
- 安全/隐私
- 开发工具
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3785065bd47b4456b698be89e9f76b47
notion_id: 3785065b-d47b-4456-b698-be89e9f76b47
---

## 定义

Forward Proxy 是位于客户端与目标服务之间的中间代理层，客户端先把请求发给代理，再由代理代表客户端访问外部服务；在 Agent 基础设施里，它常被用来统一承接出站流量、附加认证信息和执行安全策略。

## 关键要点

- 对 Agent 来说，Forward Proxy 的价值在于把网络出口集中到一个可观测、可控制的边界点。

- 当代理层能够识别目标主机、请求方式和认证规则时，就可以在不修改上层工具调用方式的前提下完成凭证注入。

- 这种方式天然适配 API、CLI、SDK 与 MCP 等不同接口，因为它工作在更底层的网络流量层。

- 如果再结合网络层封锁直连出口，Forward Proxy 就能从“建议走代理”变成“必须走代理”的强约束机制。

## 来源引用

- [摘要：Agent Vault: The Open Source Credential Proxy and Vault for Agents](summaries/摘要：Agent Vault- The Open Source Credential Proxy and Vault for Agents.md)（[原文](https://x.com/dangtony98/status/2046982854710857762)）
