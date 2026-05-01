---
title: 摘要：llm Wiki 养了三周，开始出毛病了
type: summary
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: https://www.notion.so/34c701074b688161bb0bc10f1d0b1837
notion_url: https://www.notion.so/Tizer/ac7c0c677d3249e789ec3a9d508ab95f
notion_id: ac7c0c67-7d32-49e7-89ec-3a9d508ab95f
---

## 一句话摘要

这篇文章基于三周维护 LLM Wiki 的实践，指出知识漂移、孤岛条目与检索失灵是编译式知识库扩张后的三个核心问题，并提出用行号级溯源、周期性健康检查和确定性检索来降低失真与失控风险。

## 关键洞察

- AI 生成摘要本质上是有损压缩，单次偏差也许很小，但在页面相互引用后会沿知识链不断放大，最终形成“摘要之间一致、但与原文不一致”的知识漂移。

- 防漂移的关键不是只检查 Wiki 内部一致性，而是把关键数字、百分比和具体结论重新锚定到原始材料的具体位置，最好精确到行号。

- 健康检查不应只做表面 lint，还要覆盖矛盾、过时、孤岛、断链和随机抽样回源核对，才能真正发现结构性失真。

- 当 Wiki 规模超过几十页后，单靠 `index.md` 导航会开始失效，Agent 需要可调用的搜索入口，才能避免“不是忘了，而是找不到”的检索退化。

- 更稳健的知识库范式，是把“找范围”交给确定性工具，把“做推理”交给 AI：先检索，再综合，而不是让模型直接在大索引里猜相关页面。

## 提取的概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Wiki 健康检查](concepts/Wiki 健康检查.md)

- [QMD](entities/QMD.md)

- [知识漂移](concepts/知识漂移.md)

- [行号级溯源](concepts/行号级溯源.md)

- [确定性检索](concepts/确定性检索.md)

## 原始文章信息

- 作者：AI赋能说

- 来源：微信

- 发布时间：2026-04-22 18:56（Asia/Shanghai）

- 原文链接：[llm Wiki 养了三周，开始出毛病了](https://mp.weixin.qq.com/s?__biz=MzI3NjE4OTAyMg%3D%3D&mid=2247488578&idx=1&sn=bd42d9c055bdc8ed9b7c46feb5b0e26d&chksm=ea6d6762607f43554101098e9913cd15d2e58637de0dbb68b7f67d697c0f2d68b998beff99e7#rd)

## 个人评注

这篇文章对当前 Wiki Compiler 流程很有提醒意义：自动编译只解决了“沉淀速度”，没有自动解决“事实保真”。如果后续要把摘要、concept、entity 继续串成知识图谱，就需要把溯源、lint 和检索当成编译流程的一部分，而不是事后补救。
