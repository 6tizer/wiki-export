---
title: 摘要：国内自建 Peer Relay 实现 Tailscale 加速：RTT 160ms → 30ms
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b688115a09bde547a7828d4
notion_url: https://www.notion.so/Tizer/291ac9e2807a4cdfad5f3ba36ef5d23c
notion_id: 291ac9e2-807a-4cdf-ad5f-3ba36ef5d23c
---

## 一句话摘要

作者用一台国内 VPS 启用 Tailscale 的 Peer Relay，替代传统自建 DERP，使国内两台设备之间的中继链路从约 160ms 降到约 30ms，并以更低运维成本获得接近局域网的远程访问体验。

## 关键洞察

- Peer Relay 是对现有 Tailscale 节点能力的升级，不需要单独维护 derper、HTTPS 证书、反代和 derpmap。

- 在“国内设备互连 + 国内 VPS”场景下，Peer Relay 通过原生 WireGuard UDP 中继，明显优于走香港官方 DERP 的延迟表现。

- 真正落地的关键不只是开端口，还包括 ACL 中的 `tag:relay` 授权、正确的 `tailscale up` 顺序，以及 DNS 接管风险控制。

- Peer Relay 不是 Exit Node，也不是 Subnet Router；它解决的是 Tailnet 设备之间的中继路径问题，而不是统一出口或子网转发。

- 对已有跑着 frps、Caddy、Docker 的 VPS 来说，新增一个 UDP 端口即可复用现有节点，适合低侵入式加速远程开发和运维访问。

## 提取的概念

- [Peer Relay](concepts/Peer Relay.md)

- [Tailscale](entities/Tailscale.md)

- [WireGuard](entities/WireGuard.md)

- [DERP](concepts/DERP.md)

- [MagicDNS](concepts/MagicDNS.md)

## 原始文章信息

- 作者：@okooo5km

- 来源：X书签 / 5km

- 发布时间：2026-04-23

- 原文链接：[https://5km.studio/blog/tailscale-peer-relay](https://5km.studio/blog/tailscale-peer-relay)

- 源文章页面：Tailscale Peer Relay：比自建 DERP 更轻量的国内加速方案，RTT 从 160ms 降到 30ms

## 个人评注

这类方案对 Tizer 的远程工作流很有启发：如果后续有家庭设备、云主机、Coding Agent 运行节点或 OpenClaw 相关服务需要低延迟互联，Peer Relay 比自建 DERP 更像一种“轻运维基础设施组件”，能把远程 SSH、屏幕共享、代码同步和内部服务访问的体验拉近到局域网级别，同时减少额外中继服务的维护负担。
