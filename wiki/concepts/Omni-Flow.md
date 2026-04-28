---
title: Omni-Flow
type: concept
tags:
- 多模态
- 模型部署
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a265b224f1714fbebf3a95bba8da03e7
notion_id: a265b224-f171-4fbe-bf3a-95bba8da03e7
---

## 定义

Omni-Flow 是面壁智能与清华大学联合研发的流式全模态框架，首次在 MiniCPM-o 4.5 技术报告中公开。该框架创造了一个共享的「时间轴」，将视觉、音频、语言等所有信息流对齐到毫秒级的时间片上，模型在每个极小的时间片内完成一次「感知-思考-响应」循环，从而原生支持全双工多模态交互。

别名：Omni-Flow 流式全模态框架

## 关键要点

- 将多模态交互从「回合制」重塑为「连续过程」，所有输入/输出流在时间维度上精确切片和对齐

- 采用时分复用（Time-Division Multiplexing）机制，将并行多模态流划分为周期性时间片内的顺序信息组

- 模型以极高频率（如每秒一次）持续刷新「世界观」，自主决定何时介入（说话或提醒）

- 原生支持打断、插话等高级交互行为，摆脱对外部 VAD（语音活动检测）的依赖

- 支持 general 声音感知（环境噪音、音乐等），不仅限于语音

## 来源引用

- [摘要：MiniCPM-o 4.5技术报告发布：全双工全模态API开放，RTX5070即可实时运行](summaries/摘要：MiniCPM-o 4.5技术报告发布：全双工全模态API开放，RTX5070即可实时运行.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719918&idx=1&sn=cbff45b94902b42d7fd45f6fb079edc9&chksm=97101f37ad8063e784cbc767f4e95f0508b405d9e1139ea77dab6c3182100c13acef9d1b40d5#rd)，PaperWeekly，微信，2026-04-28）
