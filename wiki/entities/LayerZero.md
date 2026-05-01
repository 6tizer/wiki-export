---
title: LayerZero
type: entity
tags:
- 链上协议
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b94a24719c1f4c5a88b5150054f1660c
notion_id: b94a2471-9c1f-4c5a-88b5-150054f1660c
---

## 定义

LayerZero 是一类跨链消息传递基础设施。本文讨论的攻击并不是协议消息格式异常，而是在其验证与执行链路中，一条源链并不存在的消息被目标链端点当作合法消息接收并执行。

## 关键要点

- Kelp DAO 在 Unichain → Ethereum 路径上使用了 LayerZero 的 DVN 机制做消息验证。

- 文章指出攻击包的结构与合法消息几乎无法区分，异常点在于源链没有对应的真实触发事件。

- LayerZero 的验证与执行解耦，使得消息一旦被验证通过，执行环节可被无需许可地触发。

## 本文语境

LayerZero 在这里既是跨链基础设施，也是这次安全复盘里必须被审视的信任边界所在：真正的问题不只是“有没有 bug”，还包括安全模型如何把单点验证放大成系统风险。

## 来源引用

- [摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击](summaries/摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU5NzUwODcyMw%3D%3D&mid=2247557429&idx=1&sn=3e87878f5780c173731d547cb238ef88&chksm=ffac3d82d1c5e92f04e0b7e596d8a55e717cbd6fd94a59fda8f688728e54a7cef4124210bfc2#rd)）

- [摘要：DAU暴跌60%：跨链桥的前端正在消失](summaries/摘要：DAU暴跌60%：跨链桥的前端正在消失.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU3ODUyMDgwMQ%3D%3D&mid=2247500756&idx=1&sn=45a17a842903736eb55fccbde7e931c7&chksm=fc7f069a6737210b9f8e864d755f0af3b7b6f75966df16b1625afc7f7104f623edd5fea711da#rd)）
