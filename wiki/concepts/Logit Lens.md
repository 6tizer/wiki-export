---
title: Logit Lens
type: concept
tags:
- 模型评测
- AI 对齐
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/68b14d17912c48ba96bfeb199e1ba244
notion_id: 68b14d17-912c-48ba-96bf-eb199e1ba244
---

## 定义

Logit Lens 是一种模型可解释性技术，能够可视化大模型每一层神经网络的输出分布。通过将中间层的隐藏状态投影到词汇表空间，可以观察模型在推理过程中逐层构建答案的过程。

## 关键要点

- 将 Transformer 中间层的隐藏状态通过 unembedding 矩阵映射为 token 概率分布

- 可揭示模型在哪一层「做出决定」，帮助理解内部推理流程

- 在 Introspection Adapters 研究中被用于揭示：大模型微调后的行为信号最集中在第 20-30 层（模型「腰部」）

- 证实了「大模型早就知道自己学了什么」的关键发现——行为信息已编码在内部激活中

## 来源引用

- [摘要：AI 终于学会「自我坦白」！Anthropic最新论文震撼来袭，「内省适配器」让黑盒模型自己说出隐藏行为](summaries/摘要：AI 终于学会「自我坦白」！Anthropic最新论文震撼来袭，「内省适配器」让黑盒模型自己说出隐藏行为.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA%3D%3D&mid=2247734195&idx=1&sn=e7ba307d92b758071f43af149a7c046d&chksm=91713367fb3fc33423f2b8e18868422e6dc43147b49cc046fac49f82b538c031b07ca5b4be66#rd)）
