---
title: oMLX
type: entity
tags:
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/25ac279d908b4fb295b1d118afc1f1c6
notion_id: 25ac279d-908b-4fb2-95b1-d118afc1f1c6
---

**定义**：oMLX 是专为 Apple Silicon 深度优化的本地大语言模型服务，基于苹果官方 MLX framework 开发，核心创新是**将 KV Cache 持久化到 SSD**。

**核心创新：SSD KV Cache**

- 热数据放内存，冷数据放 SSD

- 无需重新计算上下文，直接从高速 SSD 读取

- TTFT 从 30-90 秒降至 5 秒以内

**与 Ollama/LM Studio 的对比**

|  | oMLX | Ollama | LM Studio |

| --- | --- | --- | --- |

| SSD KV Cache | ✅ | ❌ | ❌ |

| 连续批处理 | ✅ | ❌ | ❌ |

| 菜单栏操作 | ✅ | ❌ | ❌ |

| MCP 支持 | ✅ | ❌ | ✅ |

**实测数据（16GB M1 Mac mini）**

- 内存占用：13.5GB vs Ollama 14GB+

- 交换区：2.5-4GB vs Ollama 7GB+

- 提示词处理：126.6 tokens/s

**适用场景**

- Mac 用户，尤其内存有限设备（16GB）

- 需要多任务并发的场景

- 节省 Token 的 OpenClaw 日常聊天需求

**TurboQuant 集成（v0.3.4+）**

支持 TurboQuant KV 缓存压缩，配合 Gemma-4-31B 等模型在 128K-256K 极限上下文下效果最显著。短上下文日常聊天时开销不划算。

**来源引用**

- [摘要：部署 Mac 本地大模型新利器--oMLX 实测](summaries/摘要：部署 Mac 本地大模型新利器--oMLX 实测.md)

- 摘要：Mac 用户可以在 oMLX 中使用 TurboQuant 了，Gemma-4-31B 实测
