---
title: MagicDNS
type: concept
tags:
- 开发工具
- 安全/隐私
status: 草稿
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f91c18c2ef5148aab4787c2fa970a4ac
notion_id: f91c18c2-ef51-48aa-b478-7c2fa970a4ac
---

## 定义

MagicDNS 是 Tailscale 提供的内建 DNS 能力，用于在 Tailnet 内以稳定名称解析设备与服务，但在特定网络环境下也可能影响宿主机原有 DNS 行为。

## 关键要点

- 让 Tailnet 设备可以用名称而不是 IP 相互访问，简化内部网络寻址。

- 当 Tailscale 接管系统 DNS 时，可能与宿主机既有解析链路产生冲突。

- 在国内网络或已有业务服务的 VPS 上，DNS 接管问题可能表现为解析抖动、超时或 `no such host`。

- 因此部署 Peer Relay 时，`--accept-dns=false` 和系统 DNS 回退策略常常需要一起考虑。

## 来源引用

- [摘要：国内自建 Peer Relay 实现 Tailscale 加速：RTT 160ms → 30ms](summaries/摘要：国内自建 Peer Relay 实现 Tailscale 加速：RTT 160ms → 30ms.md)（[原文](https://5km.studio/blog/tailscale-peer-relay)）

## 关联概念

- [Tailscale](entities/Tailscale.md)

- [Peer Relay](concepts/Peer Relay.md)

- [DERP](concepts/DERP.md)
