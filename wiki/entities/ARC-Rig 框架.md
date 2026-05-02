---
title: ARC/Rig 框架
type: entity
tags:
- 链上协议
- 量化交易
- AI 设计
status: 审核中
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d701c5291bde4f08ad35939865cc5865
notion_id: d701c529-1bde-4f08-ad35-939865cc5865
---

## 定义

ARC（AI Rig Complex）是由 Playgrounds（@Playgrounds0x）开发的 Rust 语言 AI Agent 框架，核心框架名为 **Rig**，主打高吞吐量、低延迟和内存安全，与 Solana 智能合约深度集成，适合性能极致要求的链上交易场景。

**GitHub**：0xPlaygrounds/rig | License: MIT | 代币：$ARC

## 核心特点

- **Rust 编写**：内存安全，性能优于 Python/TypeScript 方案

- **Solana 原生集成**：与 Solana 智能合约紧密绑定，提供统一 LLM Provider 抽象接口

- **模块化架构**：可按需组合不同 LLM 后端和向量存储

- **低延迟**：特别适合对延迟敏感的交易类场景

## 定位说明

相比 ElizaOS（快速部署派）和 ZerePy（社交媒体派），ARC 是「性能极客派」。适合构建 Solana 高频交易 Agent，但学习曲线较陡，不适合快速搭建社交媒体 Bot。

## 来源引用

- [摘要：2025 年初 AI Agent 框架全景：Swarms、ELIZA、ARC、ZerePy、Dolos 谁是真正的基础设施？](summaries/摘要：2025 年初 AI Agent 框架全景：Swarms、ELIZA、ARC、ZerePy、Dolos 谁是真正的基础设施？.md)

- [摘要：Crypto AI Agent 全景图：框架、Launchpad、Meme 币与应用的四维爆发](summaries/摘要：Crypto AI Agent 全景图：框架、Launchpad、Meme 币与应用的四维爆发.md)
