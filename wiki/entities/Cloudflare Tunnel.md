---
title: Cloudflare Tunnel
type: entity
tags:
- OpenClaw
- 算力基础设施
- AI 产品
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/08eae155272744a3b22b39763ea538bb
notion_id: 08eae155-2727-44a3-b22b-39763ea538bb
---

## 定义

Cloudflare Tunnel 是 Cloudflare Zero Trust 提供的内网穿透服务，允许服务器在不开放任何公网端口的情况下对外提供服务，并自动配置 HTTPS。

## 核心价值

- **隐藏真实 IP**：流量经过 Cloudflare 全球节点转发，服务器 IP 不暴露

- **免费 HTTPS**：自动配置 SSL 证书

- **防 DDoS**：利用 Cloudflare CDN 防护

- **无需开放端口**：不需在防火墙开放 80/443

## 在 AI 中转站中的应用

配合 Sub2Api 使用，将内网 8080 端口暴露为带域名的 HTTPS 服务。配置要点：URL 设为 `localhost:8080`，不是 443。

## 来源引用

- [摘要：一篇教你从0搭建中转站！超高性价比 token 自由，爽用 GPT-5.4](summaries/摘要：一篇教你从0搭建中转站！超高性价比 token 自由，爽用 GPT-5.4.md)

- [原文链接](https://x.com/Chris_Defi/status/2033462650932523473)｜《200U 换来的 45 天实战：OpenClaw 高 ROI 部署最佳实践》｜来源条目：[摘要：200U 换来的 45 天实战：OpenClaw 高 ROI 部署最佳实践](summaries/摘要：200U 换来的 45 天实战：OpenClaw 高 ROI 部署最佳实践.md)

- [摘要：VLESS + Reality 协议](summaries/摘要：VLESS + Reality 协议.md)（[原文](https://x.com/bailyLU/status/2045457857458647548)）
