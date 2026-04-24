---
title: 摘要：没想到！DeepSeek V4里，竟还藏着一个中国万亿开源模型
type: summary
tags:
- LLM
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: https://www.notion.so/34c701074b688177accce89c786d7c7e
notion_url: https://www.notion.so/620cdd459bb8460f9aae10aaf7dd682a
notion_id: 620cdd45-9bb8-460f-9aae-10aaf7dd682a
---

## 一句话摘要

DeepSeek V4 与 Kimi K2.6 在同一周发布，不只是两个中国万亿开源模型的并进，更显示出国产大模型在注意力机制、优化器、KV 缓存、长上下文和芯片适配等底层技术上已经形成相互借力、共同加速的开源竞争格局。

## 关键洞察

- DeepSeek 与 Kimi 在过去 15 个月里多次沿着相近方向推进，从推理、多模态思考到注意力改造、数学证明与万亿参数开源，呈现出持续的同步演进。

- Kimi K2.6 采用 DeepSeek 首创的 MLA 路线来压缩长上下文 KV 缓存，而 DeepSeek V4 又吸收了 Kimi 团队验证过的大规模 Muon 优化器路线，技术借力已经从“观点相似”进入“工程复用”。

- 两家分别沿稀疏注意力与线性注意力推进，本质上都在改造 Transformer 的成本结构，目标都是把超长上下文和高吞吐推理做成可产品化能力。

- 在生态层面，DeepSeek 与 Kimi 已被 NVIDIA、Meta、Cursor、Rakuten、OpenRouter 等当作性能基准或底座模型，中国开源模型开始从追赶者转向基准提供者。

- 在芯片层面，两家都在推进 NVIDIA 之外的国产算力适配，说明模型架构演进与推理基础设施国产化正在同步前进。

## 提取的概念

- [DeepSeek V4](entities/DeepSeek V4.md)

- [Kimi K2.6](entities/Kimi K2.6.md)

- [多潜在注意力](concepts/多潜在注意力.md)

- [MoE 架构](concepts/MoE 架构.md)

- [KV缓存压缩](concepts/KV缓存压缩.md)

- [线性注意力](concepts/线性注意力.md)

- [Muon 优化器](concepts/Muon 优化器.md)

- [稀疏注意力](concepts/稀疏注意力.md)

## 原始文章信息

- 作者：新智元

- 来源：微信

- 发布时间：2026-04-24 11:07

- 原文链接：[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695014&idx=1&sn=f81382e51e476c13729ea001ffe75420&chksm=f0c02cf19ac3820ed9dbd1dac8fdbc7a605ff4e7415e7f0073c959a057da3463cc44512e18b7#rd)

- 源文章页：没想到！DeepSeek V4里，竟还藏着一个中国万亿开源模型

## 个人评注

这类“底层技术 + 生态 adoption + 芯片路线”三线并进的文章，很适合进入 Tizer 的知识编译链路：summary 用来快速判断趋势，concept 与 entity 则把 MLA、Muon、稀疏注意力等拆成可复用积木，后续无论是做 OpenClaw 相关研究、内容选题还是模型路线对比，都可以直接复用这些结构化节点。
