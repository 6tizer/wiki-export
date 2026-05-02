---
title: MoE 架构
type: concept
tags:
- 推理优化
- 训练/微调
status: 已审核
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a9669a8629a347708a59fa2700716269
notion_id: a9669a86-29a3-4770-8a59-fa2700716269
---

## 定义

MoE（Mixture of Experts，混合专家）是一种模型架构，将参数分为多个「专家」模块，每次推理时只激活与当前输入最相关的少数专家，实现大参数量但低计算成本的高效推理。

## 核心要点

- 条件计算：不是每次都使用所有参数，而是通过路由机制选择最适合的专家

- 效率优势：总参数量大但激活参数少，如 Qwen3.5 的 397B/17B（总参/激活）

- 与线性注意力结合：Qwen3.5 使用 MoE + 线性注意力混合架构，进一步提升效率

- 吞吐量提升：在长上下文场景下优势明显，Qwen3.5 解码速度是密集模型的 7-19 倍

- 本地部署可行性：激活参数少使本地部署成为可能

## 关联概念

- [OpenMythos](entities/OpenMythos.md)

- [Claude Mythos](entities/Claude Mythos.md)

- [Recurrent-Depth Transformer](concepts/Recurrent-Depth Transformer.md)

- [自适应计算时间](concepts/自适应计算时间.md)

- [多潜在注意力](concepts/多潜在注意力.md)

- [Parcae 架构](concepts/Parcae 架构.md)

- [隐式思维链](concepts/隐式思维链.md)

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [Gemma4-26B-A4B](entities/Gemma4-26B-A4B.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)

- [混合注意力](concepts/混合注意力.md)

- [OpenAI Privacy Filter](entities/OpenAI Privacy Filter.md)

- [隐私脱敏](concepts/隐私脱敏.md)

- [长上下文](concepts/长上下文.md)

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)

- [Dense 模型](concepts/Dense 模型.md)

- [SWE-bench](concepts/SWE-bench.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

- [Expert parallelism](concepts/Expert parallelism.md)

- [Ling-2.6-flash](entities/Ling-2.6-flash.md)

- [线性注意力](concepts/线性注意力.md)

- [Multi-Token Prediction](concepts/Multi-Token Prediction.md)

- [自托管](concepts/自托管.md)

## 来源引用

- [摘要：Traditional ML Inference vs. LLM Inference](summaries/摘要：Traditional ML Inference vs. LLM Inference.md)（[原文](https://x.com/_avichawla/status/2026224423460843665)）

- [摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb](summaries/摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb.md)（[原文](https://x.com/hxiao/status/2047004358500614152)）

- [摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说](summaries/摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说.md)（[原文](https://x.com/KyeGomezB/status/2045659150340723107)）

- [摘要：Gemma 4 全系列在 M5 Max 本地运行测评](summaries/摘要：Gemma 4 全系列在 M5 Max 本地运行测评.md)（[原文](https://x.com/googlegemma/status/2042310203845329311)，Gemma，2026-04）

- [摘要：Qwen3.5 开源多模态大模型](summaries/摘要：Qwen3.5 开源多模态大模型.md)（开源星探，2026-02-17）

- [摘要：OpenClaw杀出中国黑马——Step 3.5 Flash 与 Agent 时代](summaries/摘要：OpenClaw杀出中国黑马——Step 3.5 Flash 与 Agent 时代.md)（新智元，2026-02-28）

- Qwen3.6-35B-A3B：用3B的算力跑35B的智慧，阿里最强开源编程模型来了（[原文](https://x.com/Alibaba_Qwen/status/2044768734234243427)，Qwen，2026-04）

- 摘要：OpenMythos：开源复现 Claude Mythos！想研究"推理时可以深入思考"的模型？也许这是你最好的开源选择！（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484602&idx=1&sn=48770b7f95580e4cee6d0027db347794&chksm=f53c2679a92de78400c852ff7bc6114b837ef81101bec148324968db0ce2f6ec182eac20d190#rd)）

- [摘要：都是你能部署的：Qwen3.6和Gemma4，谁更适合作为你的下一代本地MoE模型？](summaries/摘要：都是你能部署的：Qwen3.6和Gemma4，谁更适合作为你的下一代本地MoE模型？.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508057&idx=1&sn=623ac3d5cea6bb2fb7f65d8b28514e75&chksm=ce0870dc9fc80dacdba48c8c3e27ae39f6c6bb655f67fa6a631ff7b3946e041f012431b96de8#rd)）

- [摘要：OpenAI Privacy Filter：1.5B MoE 隐私脱敏模型支持 128k 上下文](summaries/摘要：OpenAI Privacy Filter：1.5B MoE 隐私脱敏模型支持 128k 上下文.md)（[原文](https://x.com/eliebakouch/status/2046979020890198503)）

- [摘要：后续来了兄弟们，卧槽真的太炸了，同样的任务，同样的配置，速度比Claude Sonnet 4.6还快 6 倍，成本低约 50 倍，](summaries/摘要：后续来了兄弟们，卧槽真的太炸了，同样的任务，同样的配置，速度比Claude Sonnet 4.6还快 6 倍，成本低约 50 倍，.md)（[原文](https://x.com/AYi_AInotes/status/2047364394229850188)）

- [摘要：没想到！DeepSeek V4里，竟还藏着一个中国万亿开源模型](summaries/摘要：没想到！DeepSeek V4里，竟还藏着一个中国万亿开源模型.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695014&idx=1&sn=f81382e51e476c13729ea001ffe75420&chksm=f0c02cf19ac3820ed9dbd1dac8fdbc7a605ff4e7415e7f0073c959a057da3463cc44512e18b7#rd)）

- [摘要：DeepSeek-V4 Preview 正式发布并开源，开启低成本百万上下文时代](summaries/摘要：DeepSeek-V4 Preview 正式发布并开源，开启低成本百万上下文时代.md)（[原文](https://x.com/deepseek_ai/status/2047516922263285776)）（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695014&idx=1&sn=f81382e51e476c13729ea001ffe75420&chksm=f0c02cf19ac3820ed9dbd1dac8fdbc7a605ff4e7415e7f0073c959a057da3463cc44512e18b7#rd)）

- [摘要：3B的成本，35B的智力：Qwen 3.6 正在暴力拆解 AI 商业化的成本围墙](summaries/摘要：3B的成本，35B的智力：Qwen 3.6 正在暴力拆解 AI 商业化的成本围墙.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU4OTY4MDU4MQ%3D%3D&mid=2247490900&idx=1&sn=823e360812006af69f9c2e01cf2d3601&chksm=fc955696662d95b68a7dfab13245552377720ba90794116217337957a434e9e8544f71d19a9d#rd)）

- [摘要：DeepSeek V4 is a Serious Threat](summaries/摘要：DeepSeek V4 is a Serious Threat.md)（[原文](https://x.com/MatthewBerman/status/2047843625510609373)）

- [摘要：4.3 小时写完一个编译器！小米凌晨开源 MiMo-V2.5，反超 DeepSeek V4](summaries/摘要：4.3 小时写完一个编译器！小米凌晨开源 MiMo-V2.5，反超 DeepSeek V4.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU3NTg5MjU1Mw%3D%3D&mid=2247497120&idx=1&sn=adb691fd7cb52fb63f3ab6f69fa5011b&chksm=fcc107b09a5c6e5f3ac7df70dcd88c86ac115110d41477790ef5d97e8fc7336b219c3d6bb535#rd)）

- [摘要：实测Hy3 preview后我发现小看腾讯做大模型决心了](summaries/摘要：实测Hy3 preview后我发现小看腾讯做大模型决心了.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247506706&idx=1&sn=0ddf8c92a703a8eba003560eb9cc75b5&chksm=cf3b2d9a092249426bcaaeec74a3511426d134adae8ec03e81caae3124cbb7db3151e8dc023f#rd)）
