---
title: WarpUI
type: entity
tags:
- CLI 工具
- 前端开发
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d1250d841bae44248d9ea0992e7383e2
notion_id: d1250d84-1bae-4424-8d9e-a0992e7383e2
---

## 定义

WarpUI 是 Warp 自研的 GPU 加速 UI 框架，采用 Entity-Component-Handle 模式（受 Flutter 启发），以 MIT 许可证开源。全局 App 对象拥有所有 entity，View 通过 ViewHandle 引用而非直接持有所有权。

> 别名：warpui、warpui_core

## 关键要点

- **架构模式**：Entity-Component-Handle，全局 App 对象统一管理所有实体，视图层通过 Handle 间接引用

- **GPU 加速**：自定义 GPU 渲染管线，非传统 DOM/Web 方案

- **许可证**：`warpui_core` 和 `warpui` crate 均为 MIT 许可证，可在闭源项目中复用

- **技术栈**：Rust 实现，属于 Warp 63-crate 工作空间的一部分

- **CRDT 文本编辑器**：内置 CRDT 作为基本原语，使协作编辑成为框架原生能力而非后期附加功能

## 关联概念

- Warp：WarpUI 的母产品

## 来源引用

- [摘要：Warp Goes Open-Source, And Oz Becomes Your First-Line Code Reviewer](summaries/摘要：Warp Goes Open-Source, And Oz Becomes Your First-Line Code Reviewer.md)（[原文](https://x.com/AlphaSignalAI/status/2049534207412871477)）
