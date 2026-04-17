---
title: Cloudflare WARP
type: entity
tags:
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/9416847581bb4198b9588ecd866594e5
notion_id: 94168475-81bb-4198-b958-8ecd866594e5
---

## 定义

Cloudflare WARP 是 Cloudflare 提供的免费网络代理服务，基于 WireGuard 协议，可将服务器出境流量通过 Cloudflare 全球节点转发，在 AI API 自建中常用于防风控。

## 常用场景

在自建 AI API 中转站时，配置为 SOCKS5 代理模式监听本地端口，将对 OpenAI API 的请求通过 Cloudflare 转发，避免被识别为数据中心开源请求而被风控。

## 配置方式

```bash
warp-cli --accept-tos registration new
warp-cli mode proxy
warp-cli proxy port 40000
warp-cli connect
# 验证
curl --socks5-hostname 127.0.0.1:40000 https://1.1.1.1/cdn-cgi/trace
# 返回 warp=on 则成功
```

## 来源引用

- 摘要：一篇教你从0搭建中转站！超高性价比 token 自由，爽用 GPT-5.4
