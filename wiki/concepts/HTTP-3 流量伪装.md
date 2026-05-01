---
title: HTTP/3 流量伪装
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/8c2a77a46d044ce69a85433f9b1cff71
notion_id: 8c2a77a4-6d04-4ce6-9a85-433f9b1cff71
---

## 定义

HTTP/3 流量伪装是把代理通信包装成看起来像标准 HTTP/3 请求的流量形态，以降低特征识别和针对性限速的概率。

## 关键要点

- 本质是借用正常协议外观隐藏代理特征

- 在高审查或强 QoS 环境下更有价值

- 它通常与 QUIC/UDP 代理方案配套出现

## 来源引用

- [原文链接](https://x.com/Zh_Crypto517/status/2042131083765150190)｜《Hysteria 2：用 UDP 黑科技把 VPS 带宽榨干到极限》｜源文章：Hysteria 2：用 UDP 黑科技把 VPS 带宽榨干到极限
