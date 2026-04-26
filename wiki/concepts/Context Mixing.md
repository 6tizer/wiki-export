---
title: Context Mixing
type: concept
tags:
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/184968c771e8467eb90292d0d88cb48f
notion_id: 184968c7-71e8-467e-b902-92d0d88cb48f
---

> **📊** Context Mixing 是一类通过组合多个上下文统计模型来预测下一个符号概率、从而逼近极限压缩率的无损压缩方法。

### 定义

CM 家族通常依赖复杂概率建模与多上下文混合策略，在压缩率上表现极强，但代价是压缩与解压都较慢，且内存消耗大。

### 关键要点

- 文章把它描述为追求极限压缩率的路线。

- 它与 BWT、LZ77/LZMA 一起构成文中比较的三类代表性压缩架构。

- 它帮助说明 STC 1.0 为何强调在压缩率与实用性之间做平衡。

### 来源引用

- 2026-04-16｜微信｜[原文链接](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247491809&idx=1&sn=338ff5fa6bbe83739a7d9bf1a46d9c0d&chksm=c0f810af8bc0986d3e65466c8e924c9ba2d27660bdffca91fcfe62ea9f83716c525a489392ab#rd)｜清华沈阳团队发布：首个由 AI 自动化科研框架独立研发的新型压缩算法

### 关联概念

- STC 1.0

- Burrows-Wheeler Transform

- LZ77/LZMA 家族
