---
title: 1-of-1 DVN 配置
type: concept
tags:
- Crypto/DeFi
- 安全/隐私
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9c2606d78f104612ba3e7da4bf3f8f43
notion_id: 9c2606d7-8f10-4612-ba3e-7da4bf3f8f43
---

## 定义

1-of-1 DVN 配置是指一条跨链消息路径只依赖一个验证器完成确认，只要这一唯一验证者放行，消息就会被视为有效。

## 关键要点

- 这种配置把跨链安全性压缩为单点信任，缺少冗余验证。

- 在高价值桥接路径中，1-of-1 设计会把验证器失误、被攻破或异常输入放大成系统级风险。

- 本文还指出，Kelp 不仅在 Unichain 路径上使用这一模式，而是在多数入站路径上都采取了类似做法。

## 本文语境

1-of-1 DVN 配置是这篇复盘里最明确的架构层教训：当系统把“唯一验证者”当作充分条件时，消息真实性就失去了多重校验的缓冲层。

## 来源引用

- [摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击](summaries/摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU5NzUwODcyMw%3D%3D&mid=2247557429&idx=1&sn=3e87878f5780c173731d547cb238ef88&chksm=ffac3d82d1c5e92f04e0b7e596d8a55e717cbd6fd94a59fda8f688728e54a7cef4124210bfc2#rd)）
