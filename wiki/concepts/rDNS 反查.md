---
title: rDNS 反查
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/37c5613f9d274aada91c9b1219cbd0bd
notion_id: 37c5613f-9d27-4aad-a91c-9b1219cbd0bd
---

## 定义

rDNS 反查是通过 IP 地址反向解析出主机名的过程。平台或运维人员可以借此快速判断一个地址是否带有明显的机房、静态服务器或代理特征。

## 关键要点

- 许多机房 IP 的反向解析结果会直接暴露 `static`、机房域名或批量服务器命名规则。

- rDNS 反查本身不是唯一依据，但它常与 ASN、欺诈值一起构成风控判断链条。

- 在检查 VPS IP 纯净度时，rDNS 是低成本、可快速验证的辅助信号。

## 来源引用

- [摘要：同样十几刀的 VPS，凭什么有的能开 Netflix，有的连 ChatGPT 都被风控？IP 类型全解析](summaries/摘要：同样十几刀的 VPS，凭什么有的能开 Netflix，有的连 ChatGPT 都被风控？IP 类型全解析.md)（[原文](https://x.com/legacyvps/status/2045785107022393710)）

## 关联概念

- [ASN（自治系统号）](concepts/ASN（自治系统号）.md)

- [欺诈值](concepts/欺诈值.md)

- [机房 IP](concepts/机房 IP.md)

- [原生 IP](concepts/原生 IP.md)
