---
title: 摘要：MiniCPM-o 4.5技术报告发布：全双工全模态API开放，RTX5070即可实时运行
type: summary
tags:
- 多模态
- 模型部署
- AI 产品
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/350701074b6881b3a4bfd11add61a44d
notion_url: https://www.notion.so/Tizer/7edb0b01d680405991ed11d2979b3b50
notion_id: 7edb0b01-d680-4059-91ed-11d2979b3b50
---

## 一句话摘要

面壁智能发布 MiniCPM-o 4.5 技术报告，首次公开 Omni-Flow 流式全模态框架，以 9B 参数实现业界首个端到端全双工全模态大模型，单卡 RTX 5070（12GB 显存）即可本地流畅运行。

## 关键洞察

- **Omni-Flow 框架首次公开**：创造共享时间轴，将视觉、音频、语言等信息流对齐到毫秒级时间片，模型在每个时间片内完成「感知-思考-响应」循环，原生支持打断、插话等全双工交互行为

- **端到端 9B 架构高效协同**：SigLIP-ViT（0.4B 视觉）+ Whisper-Medium（0.3B 音频）+ Qwen3-8B（LLM 基座）+ 轻量语音解码器（~0.3B），LLM 只生成文本 Token，语音合成外包给专业小模型

- **TAIL 语音生成方案**：Time-Aligned Interleaving 让语音块紧跟文本块生成，配合轻量 pre-look 机制保证跨词发音连贯，将全双工场景下语音延迟降到最低

- **消费级显卡可部署**：INT4 量化版仅需 11GB 显存，解码速度 212 tokens/s，比 Qwen3-Omni 快 40%+；同步开源桌面安装包 Comni（Windows/macOS）和完整 Demo 前后端代码

- **性能对标顶尖**：视觉基准与 Gemini 2.5 Flash 相当，全模态全双工基准全面超越 Gemini 2.5 Flash 和 Qwen3-Omni，语音生成质量优于 CosyVoice2

## 提取的概念

- [MiniCPM](entities/MiniCPM.md)（MiniCPM-o 4.5 属于该系列的全模态版本）

- [Omni-Flow](concepts/Omni-Flow.md)（本文首次公开的流式全模态框架）

- [TAIL](concepts/TAIL.md)（Time-Aligned Interleaving 语音生成方案）

## 原始文章信息

- **作者**：PaperWeekly

- **来源**：微信公众号

- **发布时间**：2026-04-28

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719918&idx=1&sn=cbff45b94902b42d7fd45f6fb079edc9&chksm=97101f37ad8063e784cbc767f4e95f0508b405d9e1139ea77dab6c3182100c13acef9d1b40d5#rd)

## 个人评注

MiniCPM-o 4.5 的全双工全模态方向对 Tizer 的内容管道有参考价值：Omni-Flow 的时间轴对齐思路可以类比到多源信息流的实时编排场景（如同时监听多个 feed 并自主决策何时触发编译）。端侧部署能力（RTX 5070 即跑）也意味着未来可考虑在本地环境运行轻量多模态模型辅助内容理解，减少对云端 API 的依赖。
