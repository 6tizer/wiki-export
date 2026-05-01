---
title: DERP
type: concept
tags:
- 商业/生态
- 知识管理
- 多Agent协作
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/881866c3187a4b7c8daf76872bdf8ebe
notion_id: 881866c3-187a-4b7c-8daf-76872bdf8ebe
---

## 定义

DERP 是 Tailscale 用来在直连失败时兜底转发流量的中继机制，传统实现通常基于 HTTPS 与 WebSocket，通过官方节点或自建 derper 提供可达性保障。

## 关键要点

- 主要解决 NAT 打洞失败后的连通性问题，是一种兜底路径。

- 传统自建 DERP 往往需要处理证书、反代、DNS 和 derpmap 维护，运维成本较高。

- 在高延迟场景下，DERP 的 TCP/TLS 封装通常比 Peer Relay 的 UDP 中继更重。

- 它强调“保证能连上”，而不是“以最低延迟连上”。

## 来源引用

- [摘要：国内自建 Peer Relay 实现 Tailscale 加速：RTT 160ms → 30ms](summaries/摘要：国内自建 Peer Relay 实现 Tailscale 加速：RTT 160ms → 30ms.md)（[原文](https://5km.studio/blog/tailscale-peer-relay)）

## 关联概念

- [Tailscale](entities/Tailscale.md)

- [Peer Relay](concepts/Peer Relay.md)

- [WireGuard](entities/WireGuard.md)
