---
title: DisTrO
type: concept
tags:
- 训练/微调
- 算力基础设施
status: 草稿
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f1d31574ca9d4a4d8307baf11fb776d7
notion_id: f1d31574-ca9d-4a4d-8307-baf11fb776d7
---

## 定义

DisTrO（Distributed Training Optimization）是 NousResearch 于 2024 年 8 月发布的分布式训练优化技术，核心突破是将 GPU 之间的通信量降低 1000 到 10000 倍，使得普通家用宽带即可让全球分散的 GPU 协作训练大模型，打破了传统训练必须依赖同一数据中心内高带宽 InfiniBand 互联的限制。

## 关键要点

- 传统大模型训练要求所有 GPU 集中在同一数据中心，通过 InfiniBand（数十 GB/s 带宽）互联；DisTrO 将通信开销压缩至家用宽带可承受的级别

- VentureBeat 以「This could change everything」为标题报道，Hacker News 直接顶至首页

- DisTrO 的技术突破直接催生了 Psyche Network（基于 Solana 的去中心化训练网络），解决了「谁来贡献 GPU」的激励问题

- DeMo 论文的合著者中包括 Diederik P. Kingma（Adam 优化器作者），标志着主流学术界开始认真对待去中心化训练方向

- DisTrO 是 NousResearch 从纯 AI 回归 web3 的关键技术节点——被工程问题推回去，而非意识形态驱动

## 来源引用

- [摘要：7 周 128K stars 爆火的 Hermes Agent，背后是 NousResearch 这群 web3 来的加密原住民](summaries/摘要：7 周 128K stars 爆火的 Hermes Agent，背后是 NousResearch 这群 web3 来的加密原住民.md)（[原文](https://x.com/Xudong07452910/status/2050493896237396410)）

## 关联概念

- [Nous Research](entities/Nous Research.md)

- [Psyche Network](entities/Psyche Network.md)

- [YaRN](concepts/YaRN.md)

- [中立对齐](concepts/中立对齐.md)

- [Hermes Agent](entities/Hermes Agent.md)
