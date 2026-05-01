---
title: TurboQuant
type: entity
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5c276dfb5f564d84bfaacd1c113a97bb
notion_id: 5c276dfb-5f56-4d84-bfaa-cd1c113a97bb
---

## 定义

TurboQuant 是谷歌 Research 2026-03-24 发布的面向大模型与向量检索场景的高压缩量化算法，实现显著降低内存占用。

## 核心指标

- **KV Cache 压缩**：Qwen 3.5 35B-A3B 上验证 4.6x 压缩比

- **格式**：turbo2、turbo3、turbo4 三种格式

- **Apple Silicon 优化**：内置 Metal kernel，测试在 Apple Silicon 上达到接近 q8_0 的 prefill 表现

## 开源实现

turboquant_plus 是个人开发者 Tom Turney 借助 Claude Code + Codex 在 7 天内完成的开源实现版本。GitHub: [https://github.com/TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus)

## 来源引用

- [摘要：7天用Claude+Codex实现谷歌 TurboQuant 算法（已开源）](summaries/摘要：7天用Claude+Codex实现谷歌 TurboQuant 算法（已开源）.md)

- 摘要：Mac用户可以在oMLX中使用TurboQuant了，Gemma-4-31B实测
