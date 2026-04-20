---
title: DVN
type: concept
tags:
- Crypto/DeFi
- 安全/隐私
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d5c71b0b4e6a4917998fafa76f9c9bec
notion_id: d5c71b0b-4e6a-4917-998f-afa76f9c9bec
---

## 定义

DVN（Decentralized Verifier Network）是 LayerZero 跨链消息安全模型中的验证网络，用来对跨链消息进行确认与背书。

## 关键要点

- DVN 的配置方式决定了一条跨链路径需要多少验证者共同确认消息。

- 本文复盘显示，若 DVN 被配置为 1-of-1，就会把单个验证环节变成单点故障。

- 即便消息编码结构完全正常，只要验证环节错误放行，目标链就可能执行本不该存在的消息。

## 本文语境

DVN 是理解这次事件的核心概念，因为攻击并不是单纯的合约重入，而是跨链验证层把不存在的源链事件认证成了可执行消息。

## 来源引用

- [摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击](summaries/摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU5NzUwODcyMw%3D%3D&mid=2247557429&idx=1&sn=3e87878f5780c173731d547cb238ef88&chksm=ffac3d82d1c5e92f04e0b7e596d8a55e717cbd6fd94a59fda8f688728e54a7cef4124210bfc2#rd)）
