---
title: 摘要：Gemma 4 全系列在 M5 Max 本地运行测评
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/0d36b6d7da874591ac4ecde1709ce83f
notion_id: 0d36b6d7-da87-4591-ac4e-cde1709ce83f
---

**一句话摘要**：Google Gemma 4 全系列（E2B/E4B/26B/31B）在 Apple M5 Max 64GB 上运行流畅，31B 模型以 20-30 token/s 的速度超出预期，适合接入 OpenClaw 处理基础任务。

**关键洞察**

- **E2B/E4B**：可在 iPhone 17 Pro Max 上运行，适合翻译、菜单识别、图片识别等端侧场景

- **26B**：文本生成、文档提取、图片识别、基础代码均可处理，token 输出速度 50-100/s

- **31B**：64GB 内存占用约 55GB，输出速度 20-30 token/s，可作为 OpenClaw 的本地基础任务模型

- **实用建议**：基础任务可切换至 Gemma 4-31B 替代昂贵的云端模型，与 Anthropic 封杀 OpenClaw 订阅应对策略形成协同

**提取的概念**

- Gemma 4

**原始文章信息**

- 作者：一起 vibe

- 来源：微信公众号

- 发布时间：2026-04-04

- 链接：[https://mp.weixin.qq.com/s?__biz=MzY5NjE2Njc4NA==&mid=2247484673](https://mp.weixin.qq.com/s?__biz=MzY5NjE2Njc4NA%3D%3D&mid=2247484673)

**个人评注**：高度相关！在 Anthropic 封杀 OpenClaw 订阅额度后，Gemma 4-31B 作为本地部署模型的价值显著提升。可直接用于 OpenClaw 的基础任务分流，降低 API 成本。
