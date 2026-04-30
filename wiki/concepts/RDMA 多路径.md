---
title: RDMA 多路径
type: concept
tags:
- 算力基础设施
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/57d55c3c3441469d9495f3a8d95fe034
notion_id: 57d55c3c-3441-469d-9495-f3a8d95fe034
---

## 定义

RDMA 多路径（Multi-path RDMA）是一种在远程直接内存访问（RDMA）网络中同时利用多条物理路径进行数据传输的技术。通过逐包喷洒（packet spraying）、乱序接收和选择性重传，将数据流分散到多条链路上并行传输，突破单路径带宽瓶颈，同时降低交换机端口拥塞。

## 关键要点

- 传统 RDMA 仅走单条路径，容易受限于单链路带宽上限

- 多路径 RDMA 通过逐包喷洒将数据分散到多条路径，最终按序重组

- 支持乱序接收和选择性重传，保证数据完整性

- 可将交换机端口缓冲区水线降低 90%，显著减少丢包和重传

- 磐脉 920 实现单 QP 打满 400G 带宽，同类产品仅约一半

- 是解决万卡智算集群网络瓶颈的核心技术之一

## 来源引用

- [摘要：平头哥发布首款智能网卡「磐脉 920」，补齐 AI 算力最后一块短板](summaries/摘要：平头哥发布首款智能网卡「磐脉 920」，补齐 AI 算力最后一块短板.md)（[原文](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ%3D%3D&mid=2653104984&idx=1&sn=dc42411b03a4365b9d390640bb35848e&chksm=7f4ed32fd3c8f23ff8d29cf54119c4b95f1ff7a7698fd3d3a7b20602a6d711630c73383a2ace#rd)）
