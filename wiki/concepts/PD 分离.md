---
title: PD 分离
type: concept
tags:
- 推理优化
- 链上协议
- AI 设计
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/405aee0265404e9a9c0bacd90df582c5
notion_id: 405aee02-6540-4e9a-9c0b-acd90df582c5
---

## 定义

PD 分离通常指在推理系统中将不同阶段或不同职责的处理过程拆分到分离的计算与服务路径中，使系统可以分别优化吞吐、时延和资源配置。

## 关键要点

- 在文章语境里，它强调缓存和数据不再总与计算节点共置。

- 一旦发生跨节点搬运，网络通信就会成为关键瓶颈。

- 该思路常用于提高系统伸缩性，但会引入新的调度与传输成本。

- 它帮助理解为什么推理时代的网络架构必须与模型执行方式协同设计。

## 来源引用

- [摘要：为了Token，阿里云竟然出了一个TPN？](summaries/摘要：为了Token，阿里云竟然出了一个TPN？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU1OTEwNDkwNw%3D%3D&mid=2247492725&idx=1&sn=05da9c55729b14a97d8fcbec7cadd3e2&chksm=fd6c11ebba90a0d90aec3ff46f46b00aea99a3b1e55e81bd81355a80b9e0f62dd360b6371d40#rd)）
