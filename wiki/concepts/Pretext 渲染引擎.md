---
title: Pretext 渲染引擎
type: concept
tags:
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/feb4e117fb5e40b8a250b4241669f5e8
notion_id: feb4e117-fb5e-40b8-a250-b4241669f5e8
---

## 定义

Pretext 是 Midjourney 工程师 Cheng Lou 开发的开源网页文本渲染引擎，绕开传统 DOM 渲染的文本测量辞店，实现文字随任意形状流动和极高性能渲染，引爆前端圈。

## 核心突破

- 传统 DOM 限制：必须将文本挂载到 DOM 才能测量尺寸，导致渲染性能沉重、CSS/DOM Reflow 开销极大

- Pretext 自研文本测量引擎，完全跳过 DOM，文字可在任意几何形状中流动、跨栏自动分配

## 性能指标

- **渲染速度**：提升 **1200 倍**

- **帧率**：支持 **120fps** 极致丝滑

- **体积**：引擎本体仅 **15KB**

- **语言支持**：多语言包括 CJK

## 创作背景

- 项目由 Claude 协助开发（Vibe Coding 典型案例）

- Cheng Lou 有 ReasonML / React 社区背景

- 全网 1600 万人围观

## 来源引用

- [摘要：前端圈沸腾！Claude造出15KB引擎，渲染狂飙1200倍：文字里能跑马里奥](summaries/摘要：前端圈沸腾！Claude造出15KB引擎，渲染狂飙1200倍：文字里能跑马里奥.md)
