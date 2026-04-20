---
title: 摘要：Kelp DAO 漏洞深度复盘：揭秘 LayerZero 幽灵消息攻击
type: summary
tags:
- Crypto/DeFi
- 安全/隐私
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b6881e8b2e5d0747afc4607
notion_url: https://www.notion.so/5f10c10ed26c4cc0a3596991b27e58a4
notion_id: 5f10c10e-d26c-4cc0-a359-6991b27e58a4
---

## 一句话摘要

Kelp DAO 此次大额失窃的本质，不是铸造或重入漏洞，而是在 LayerZero 跨链路径采用 1-of-1 DVN 单点信任的前提下，一条源链并不存在的“幽灵消息”被目标链当作合法消息执行，最终从真实库存中释放了大量 rsETH。

## 关键洞察

- 这次事件最关键的链上证据，是 Unichain 源端 outboundNonce 与以太坊目标端 lazyInboundNonce 的真实失配：目标端接受了 nonce 308，但源端从未发送过对应消息。

- Kelp 将 Unichain → Ethereum 路径配置为 1-of-1 DVN，意味着只要唯一验证环节被攻破、出错或接收异常输入，就可能把伪造消息送入执行阶段。

- 这不是典型的 mint 漏洞或重入攻击；问题在于一条结构正常、编码无异常的跨链消息，在源链没有真实触发事件的情况下仍被验证通过。

- LayerZero 将验证与执行解耦，导致攻击者在消息一旦被验证后，可以利用无需许可的执行路径自行投递并完成资产释放。

- Kelp 在 46 分钟内冻结接收地址并阻止了第二笔幽灵消息执行，说明应急响应有效，但也进一步暴露出单点验证配置在高价值跨链路径上的风险。

## 提取的概念

- [Kelp DAO](entities/Kelp DAO.md)

- [LayerZero](entities/LayerZero.md)

- [DVN](concepts/DVN.md)

- [1-of-1 DVN 配置](concepts/1-of-1 DVN 配置.md)

- [幽灵消息攻击](concepts/幽灵消息攻击.md)

- [rsETH](entities/rsETH.md)

## 原始文章信息

- 作者：登链社区

- 来源：微信

- 发布时间：2026-04-20

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzU5NzUwODcyMw%3D%3D&mid=2247557429&idx=1&sn=3e87878f5780c173731d547cb238ef88&chksm=ffac3d82d1c5e92f04e0b7e596d8a55e717cbd6fd94a59fda8f688728e54a7cef4124210bfc2#rd)

## 个人评注

这篇复盘对 Tizer 的启发很直接：无论是跨链协议、Agent 工具链还是内容编译流水线，只要把单点校验当成最终真相，就会把错误放大成系统性事故。真正可靠的系统，需要多重验证、来源回溯，以及在关键节点保留可审计的证据链。
