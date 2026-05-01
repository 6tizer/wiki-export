---
title: TLS 拦截
type: concept
tags:
- Agent 安全
- Harness 工程
- 链上协议
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/515efffe7e074282bbcd56207420f76d
notion_id: 515efffe-7e07-4282-bbcd-56207420f76d
---

## 定义

TLS 拦截是指代理在客户端与目标服务之间分别建立两段 TLS 连接，中间对流量进行解密、检查和再加密，从而让原本不可见的 HTTPS 请求变得可审计、可执行策略控制。

## 关键要点

- 常用于需要对加密出站流量做安全检查、审计或合规控制的场景

- 典型实现方式是代理为每个目标主机动态签发证书，并使用自有 CA 与客户端建立受信任连接

- 它让 HTTPS 请求可被规则引擎或安全模型读取，但也引入了根证书管理与信任集中风险

- 在 Agent 场景下，TLS 拦截让网络出口真正成为统一策略执行点

## 来源引用

- [摘要：CrabTrap: an LLM-as-a-judge HTTP proxy to secure agents in production](summaries/摘要：CrabTrap- an LLM-as-a-judge HTTP proxy to secure agents in production.md)（[原文](https://x.com/pedroh96/status/2046604993982009825)）

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [LLM-as-judge](concepts/LLM-as-judge.md)
