---
title: LZ77/LZMA 家族
type: concept
tags:
- 开发工具
status: 审核中
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/135454f411f64da3b9526574250ea1f4
notion_id: 135454f4-11f6-4da3-b952-6574250ea1f4
---

> **⚙️** LZ77/LZMA 家族指一类通过发现重复字符串并以引用或指针替换来实现压缩的主流无损压缩算法路线。

### 定义

这一路线强调**解压速度、压缩级别灵活性与工程可用性**，典型实现包括 zstd、xz、lz4 等。文章将其作为与 BWT 架构对照的工业主流方案。

### 关键要点

- 适合需要高吞吐和广泛工程落地的压缩场景。

- 文章认为它在压缩率上通常不如高优化的 BWT 路线。

- 它是理解 STC 1.0 定位时的重要参照系。

### 来源引用

- 2026-04-16｜微信｜[原文链接](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247491809&idx=1&sn=338ff5fa6bbe83739a7d9bf1a46d9c0d&chksm=c0f810af8bc0986d3e65466c8e924c9ba2d27660bdffca91fcfe62ea9f83716c525a489392ab#rd)｜清华沈阳团队发布：首个由 AI 自动化科研框架独立研发的新型压缩算法

### 关联概念

- STC 1.0

- Burrows-Wheeler Transform

- Context Mixing
