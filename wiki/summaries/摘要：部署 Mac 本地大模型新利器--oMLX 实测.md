---
title: 摘要：部署 Mac 本地大模型新利器--oMLX 实测
type: summary
tags:
- 推理优化
- 模型部署
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: 本地部署, 工具推荐
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fe5a55f8243749aaba1033a29265723f
notion_id: fe5a55f8-2437-49aa-ba10-33a29265723f
---

**一句话摘要**：oMLX 是专为 Apple Silicon 深度优化的本地大语言模型服务，核心创新将 KV Cache 持久化到 SSD，将首次响应时间从 30-90 秒降至 5 秒以内。

**关键洞察**

- 核心创新：热数据放内存+冷数据放 SSD，无需重新计算上下文，直接从高速 SSD 读取

- 与 Ollama 对比：内存占用更稳定，交换区使用显著减少（Ollama 7GB vs oMLX 2.5-4GB）

- 支持连续批处理（多任务并发），在 Ollama 几乎掉崩的并发场景下 oMLX 稳定完成

- 提示词处理 126.6 tokens/s，支持 OpenAI/Anthropic 兼容 API，可接入 OpenClaw

- 适合节省 Token 的日常聊天需求

**提取的概念**

- oMLX（专为 Apple Silicon 的本地 LLM 服务，KV Cache SSD 持久化）

**原始文章信息**

- 作者：陈佬昔编程人生 | 来源：微信公众号 | 发布时间：2026-03-15

- 链接：[https://mp.weixin.qq.com/s?__biz=MzkxNzY1MzA5Nw==&mid=2247485023](https://mp.weixin.qq.com/s?__biz=MzkxNzY1MzA5Nw%3D%3D&mid=2247485023)

**个人评注**

对于 Mac 用户有实际价值，尤其是内存有限设备（16GB）。可以作为 OpenClaw 日常聊天、节省 Token 的本地替代方案。
