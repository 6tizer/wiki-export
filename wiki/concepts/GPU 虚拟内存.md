---
title: GPU 虚拟内存
type: concept
tags:
- 视频/3D
- 算力基础设施
- AI 设计
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/8f6d24e4ea904756a893dedd15ba875d
notion_id: 8f6d24e4-ea90-4756-a893-dedd15ba875d
---

### 定义

GPU 虚拟内存是在固定显存预算下，通过页表、驻留块和换出策略，把远大于显存容量的数据按需映射到 GPU 的机制。Spark 2.0 用它在移动端显存限制下管理超大 3DGS 场景。

### 关键要点

- 在 GPU 上维护固定大小的内存池，而不是试图一次装下全部场景

- 需要渲染的区域才调入对应数据块，内存满时换出最久未使用的块

- 使多个独立 3DGS 场景可以共享同一个内存池，支持更大范围的连续世界

### 来源引用

- [刚刚，李飞飞最新成果发布，手机也能跑亿级粒子的 3D 世界了｜附体验地址](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA%3D%3D&mid=2651087721&idx=1&sn=119485bcb1450f9f1e0d1319733528fa&chksm=bc0eb7380742222c99e0a18f40d5e0628cdf29eda89f2dcf858670859b610e225c78e4f98c8e#rd)｜源文章：刚刚，李飞飞最新成果发布，手机也能跑亿级粒子的 3D 世界了｜附体验地址

- [Three.js](https://x.com/sparkjsdev/status/2044090505982816449)｜源文章：Spark 2.0：把亿级 3D 高斯渲染带进浏览器的开源引擎

### 关联概念

- Spark 2.0

- 3D Gaussian Splatting

- 连续 LoD 树

- RAD 格式

- 注视点渲染
