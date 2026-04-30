---
title: Peer Relay
type: concept
tags:
- 开发工具
- 安全/隐私
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/917b66336d6d4077ae4d80ec795477a3
notion_id: 917b6633-6d6d-4077-ae4d-80ec795477a3
---

## 定义

Peer Relay 是 Tailscale 在较新版本中提供的一种中继能力，允许任意已授权的 Tailnet 节点开放原生 WireGuard UDP 中继通道，用更轻量的方式替代传统 DERP 中继。

## 关键要点

- 不需要单独部署 derper、HTTPS 证书或 WebSocket 反代。

- 依赖 ACL 中对 `tailscale.com/cap/relay` 和 `tag:relay` 的显式授权。

- 本质上是复用现有 Tailscale 节点能力，而不是额外维护一台独立中继服务。

- 在国内设备互连场景中，若能把中继节点放到国内，通常能显著降低 RTT。

## 来源引用

- [摘要：国内自建 Peer Relay 实现 Tailscale 加速：RTT 160ms → 30ms](summaries/摘要：国内自建 Peer Relay 实现 Tailscale 加速：RTT 160ms → 30ms.md)（[原文](https://5km.studio/blog/tailscale-peer-relay)）

## 关联概念

- [Tailscale](entities/Tailscale.md)

- [WireGuard](entities/WireGuard.md)

- [DERP](concepts/DERP.md)

- [MagicDNS](concepts/MagicDNS.md)
