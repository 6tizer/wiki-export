---
title: Burrows-Wheeler Transform
type: concept
tags:
- 开发工具
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e88a4b7b0d8342f08b1f24295a5bbb00
notion_id: e88a4b7b-0d83-42f0-8b1f-24295a5bbb00
---

> **🧩** Burrows-Wheeler Transform 是一种通过重排输入序列来聚集相似字符、为后续游程编码和熵编码创造条件的经典压缩变换。

### 定义

BWT 本身不是完整压缩器，而是无损压缩流水线中的关键预处理步骤。它常与游程编码、Move-to-Front、熵编码等环节配合，目标是让后续编码阶段更容易利用局部相似性。

### 关键要点

- 文章将 BWT 家族定位为兼顾压缩率与实用性的折中路线。

- 代表实现包括 bzip2、bsc，以及文章中的 STC 1.0。

- 相比 LZ77/LZMA 家族，BWT 在某些文本和长距离相关数据上可获得更高压缩率。

### 来源引用

- 2026-04-16｜微信｜[原文链接](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247491809&idx=1&sn=338ff5fa6bbe83739a7d9bf1a46d9c0d&chksm=c0f810af8bc0986d3e65466c8e924c9ba2d27660bdffca91fcfe62ea9f83716c525a489392ab#rd)｜清华沈阳团队发布：首个由 AI 自动化科研框架独立研发的新型压缩算法

### 关联概念

- STC 1.0

- LZ77/LZMA 家族

- Context Mixing
