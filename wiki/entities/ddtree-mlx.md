---
title: ddtree-mlx
type: entity
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/205c7188d6a64ecdb1d949faf88c053a
notion_id: 205c7188-d6a6-4ecd-b1d9-49faf88c053a
---

## 定义

ddtree-mlx 是把 DDTree 树形 speculative decoding 落到 Apple Silicon 与 MLX 生态中的开源实现，目标是在本地大模型推理中进一步压榨 DFlash 之上的吞吐收益。

## 核心要点

- 它把 DFlash 的单链式草稿扩展成 draft tree，并让目标模型一次验证多个候选分支。

- 项目围绕 MLX 与 Metal 内核做了工程化实现，包含 tree verify、cache commit 与 OpenAI 兼容服务接口。

- 在 M3 Ultra 上配合 Qwen 3.5 27B 4-bit，文中给出的实测吞吐达到 42.3 tok/s，明显高于自回归与纯 DFlash。

- 更适合代码生成、结构化输出等高接受率任务，不适合直接外推到低接受率的开放式创作场景。

## 来源引用

- [摘要：Tree-based speculative decoding for Apple Silicon.](summaries/摘要：Tree-based speculative decoding for Apple Silicon.md)（[原文](https://x.com/QingQ77/status/2045500092527087861)）

## 关联概念

- [DDTree](concepts/DDTree.md)

- [DFlash](concepts/DFlash.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

- [MLX 框架](entities/MLX 框架.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)
