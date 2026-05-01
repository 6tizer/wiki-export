---
title: Xray
type: entity
tags:
- Agent 安全
- 链上协议
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6776009aff834872b4d74e587d3b87e4
notion_id: 6776009a-ff83-4872-b4d7-4e587d3b87e4
---

## 定义

Xray 是一个面向代理与流量转发场景的开源网络工具，常被用作 VLESS、Reality 等协议组合的服务端核心组件。

## 关键要点

- 在这篇资料里，Xray 是整套随身 WiFi 代理方案的核心服务。

- 它负责承载 VLESS + Reality 配置，并与 UUID、密钥、端口和客户端参数共同构成可用连接。

- 实际落地时通常需要配合 systemd、自启脚本、看门狗和端口映射一起部署，才能保证长期稳定运行。

## 来源引用

- [摘要：VLESS + Reality 协议](summaries/摘要：VLESS + Reality 协议.md)（[原文](https://x.com/bailyLU/status/2045457857458647548)）

- [摘要：Remnawave：比 3x-ui 更现代的代理面板，俄罗斯团队打造的全自动化管理方案](summaries/摘要：Remnawave：比 3x-ui 更现代的代理面板，俄罗斯团队打造的全自动化管理方案.md)（[原文](https://x.com/dingyi/status/2045743670050353594)）
