---
title: PipeLive
type: entity
tags:
- LLM
- 推理优化
- 模型部署
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/4694b9707305497bb3260139df23431e
notion_id: 4694b970-7305-497b-b326-0139df23431e
---

## 定义

PipeLive 是一个面向大语言模型在线服务的系统，核心能力是在**不中断服务**的前提下，对运行中的流水线并行配置进行在线、原位重构，以适配动态负载与异构 GPU 环境。

## 关键要点

- 基于 vLLM 构建，关注的是服务期内的运行时重构，而不是离线部署优化。

- 重点解决三类难题：模型层迁移的显存冲突、KV 缓存容量重分配、迁移过程中的状态一致性。

- 通过动态 KV 缓存管理、层堆叠与增量 KV 修补，将配置切换的服务停顿压缩到毫秒级。

- 适用于 Prefill-heavy 与 Decode-heavy 交替、且底层 GPU 算力与带宽特征不同的场景。

## 关联概念

- [摘要：大模型服务新范式：PipeLive突破在线流水线并行重构难题，自适应异构GPU环境，性能提升超30%](summaries/摘要：大模型服务新范式：PipeLive突破在线流水线并行重构难题，自适应异构GPU环境，性能提升超30%.md)

## 来源引用

- [摘要：大模型服务新范式：PipeLive突破在线流水线并行重构难题，自适应异构GPU环境，性能提升超30%](summaries/摘要：大模型服务新范式：PipeLive突破在线流水线并行重构难题，自适应异构GPU环境，性能提升超30%.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA%3D%3D&mid=2247557871&idx=1&sn=93ad2f6963d089262651c0d240c0e4f8&chksm=cf61645b6cd81036051aff2da5c3faf13afa936640bf4670322c43996fa2c291fc30415885df#rd)）
