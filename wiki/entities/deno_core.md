---
title: deno_core
type: entity
tags:
- 模型部署
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/573689036cc34587b6680d8c588d4227
notion_id: 57368903-6cc3-4587-b668-0d8c588d4227
---

## 定义

deno_core 是 Deno 项目的核心运行时库，提供 V8 JavaScript 引擎的 Rust 绑定和运行时抽象。它允许 Rust 应用嵌入完整的 V8 引擎，实现真实 JavaScript 执行，而无需依赖完整的浏览器或 Node.js 环境。

## 关键要点

- 提供 V8 引擎的 Rust 封装，支持 module_loader、runtime、自定义 ops

- 被 Obscura 等项目用于在无头浏览器中嵌入真实 JS 执行能力

- 相比完整 Chromium 引擎，极大降低内存和二进制体积

- 当前版本 0.350（Obscura 使用版本）

- 首次编译时从源码构建 V8，后续有缓存

## 适用场景

- Rust 应用嵌入 JavaScript 运行时

- 轻量级浏览器引擎的 JS 执行层

- 服务端 JavaScript 执行

## 来源引用

- [摘要：30MB Rust无头浏览器Obscura：击败Chrome、V8真实JS+CDP全兼容，AI Agent与爬虫的隐形核武器](summaries/摘要：30MB Rust无头浏览器Obscura：击败Chrome、V8真实JS+CDP全兼容，AI Agent与爬虫的隐形核武器.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ%3D%3D&mid=2247485078&idx=1&sn=84152e9774e0eab3d16839db3a7657de&chksm=f5696523a9b95b45d7ce029701ad0acd68b9d573d010a44500be214374bde17f0b4b04c3dc08#rd)）

## 关联概念

- [Obscura](entities/Obscura.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [浏览器指纹模拟](concepts/浏览器指纹模拟.md)
