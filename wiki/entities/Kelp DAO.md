---
title: Kelp DAO
type: entity
tags:
- Crypto/DeFi
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4ccd48a40ead456dba9e9214737a8548
notion_id: 4ccd48a4-0ead-456d-ba9e-9214737a8548
---

## 定义

Kelp DAO 是以流动性质押与再质押资产为核心的 DeFi 协议实体，本文中的被攻击方就是其跨链 rsETH 资产通道与相关桥接库存。

## 关键要点

- 本次事件中，Kelp DAO 在 Unichain → Ethereum 路径上的 LayerZero 配置采用了 1-of-1 DVN。

- 攻击并非直接篡改 Kelp 的底层抵押品，而是通过伪造可执行的跨链消息，从真实库存中释放 rsETH。

- Kelp 团队在约 46 分钟内冻结接收地址，阻止了第二笔幽灵消息继续执行。

## 本文语境

Kelp DAO 在这篇复盘里是安全事件的核心实体，问题暴露在其跨链信任模型与应急处置链路上，而不是传统意义上的代币铸造漏洞。

## 来源引用

- [摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击](summaries/摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU5NzUwODcyMw%3D%3D&mid=2247557429&idx=1&sn=3e87878f5780c173731d547cb238ef88&chksm=ffac3d82d1c5e92f04e0b7e596d8a55e717cbd6fd94a59fda8f688728e54a7cef4124210bfc2#rd)）
