---
title: QUIC 代理
type: concept
tags:
- 开发工具
- 安全/隐私
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a9b110497b9542149563c590d1a0fb10
notion_id: a9b11049-7b95-4214-9563-c590d1a0fb10
---

## 定义

QUIC 代理是建立在 QUIC 传输层之上的代理通信方案，利用 UDP、TLS 1.3 和多路复用能力提升跨地域网络中的吞吐与时延表现。

## 关键要点

- 相比 TCP 代理，更适合高延迟与高丢包链路

- 适合追求速度和抗干扰能力的节点场景

- Hysteria 2、TUIC 等方案都属于这一思路

## 来源引用

- [原文链接](https://x.com/Zh_Crypto517/status/2042131083765150190)｜《Hysteria 2：用 UDP 黑科技把 VPS 带宽榨干到极限》｜源文章：Hysteria 2：用 UDP 黑科技把 VPS 带宽榨干到极限
