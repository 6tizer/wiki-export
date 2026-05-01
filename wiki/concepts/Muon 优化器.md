---
title: Muon 优化器
type: concept
tags:
- 训练/微调
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bc1d157ebccd40d8b2fc194eea38e0ed
notion_id: bc1d157e-bccd-40d8-b2fc-194eea38e0ed
---

## 定义

Muon 优化器是一种面向大模型训练的优化器路线，不再像 AdamW 那样逐参数独立缩放，而是对整个梯度矩阵进行 Newton-Schulz 正交化处理，以获得更均匀的更新方向、更快的收敛速度和更稳定的大规模训练过程。

## 关键要点

- Muon 的核心思路是把优化重点从“单参数自适应缩放”转向“矩阵空间中的整体更新方向校正”。

- 它最初只在较小模型上被验证，后续被 Kimi 团队扩展到大规模训练场景，进一步发展出 MuonClip 等工程化变体。

- 在本文语境里，DeepSeek V4 明确吸收了这一路线，说明 Muon 已从论文概念进入万亿参数模型训练实践。

- Muon 代表的是国产模型团队之间对训练方法论的相互借力，而不只是单纯的架构跟风。

## 来源引用

- [摘要：没想到！DeepSeek V4里，竟还藏着一个中国万亿开源模型](summaries/摘要：没想到！DeepSeek V4里，竟还藏着一个中国万亿开源模型.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695014&idx=1&sn=f81382e51e476c13729ea001ffe75420&chksm=f0c02cf19ac3820ed9dbd1dac8fdbc7a605ff4e7415e7f0073c959a057da3463cc44512e18b7#rd)）

- [摘要：聊几句 DeepSeek V4 的体感。](summaries/摘要：聊几句 DeepSeek V4 的体感。.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA%3D%3D&mid=2247582111&idx=1&sn=a4c61d4001c76f54e9f8203e84c223f4&chksm=c1b21cecf8ff7060b60328b74bcb9760f3878a2f81ff10dcb20da58dc509fc7954f851074859#rd)）

## 关联概念

- [DeepSeek V4](entities/DeepSeek V4.md)

- [mHC](concepts/mHC.md)

- [Kimi K2.6](entities/Kimi K2.6.md)

- [MoE 架构](concepts/MoE 架构.md)
