---
title: RAD 格式
type: concept
tags:
- 开发工具
- 内容创作
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a79717ec490d4b8085d906e4c1aa037c
notion_id: a79717ec-490d-4b80-85d9-06e4c1aa037c
---

### 定义

RAD 格式是 Spark 2.0 设计的 3DGS 数据封装格式，通过把 splat 数据切分为可独立压缩和随机访问的数据块，实现渐进式流式加载。

### 关键要点

- 每块约 64K 个 splat，并在文件头记录块偏移，便于随机读取

- 第一块保留场景最粗粒度轮廓，下载后即可快速显示整体形状

- 后续再按视角需求拉取更细数据块，让画面逐步清晰

- 兼顾压缩效率与边下边看的交付体验

### 来源引用

- [刚刚，李飞飞最新成果发布，手机也能跑亿级粒子的 3D 世界了｜附体验地址](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA%3D%3D&mid=2651087721&idx=1&sn=119485bcb1450f9f1e0d1319733528fa&chksm=bc0eb7380742222c99e0a18f40d5e0628cdf29eda89f2dcf858670859b610e225c78e4f98c8e#rd)｜源文章：刚刚，李飞飞最新成果发布，手机也能跑亿级粒子的 3D 世界了｜附体验地址

- [Three.js](https://x.com/sparkjsdev/status/2044090505982816449)｜源文章：Spark 2.0：把亿级 3D 高斯渲染带进浏览器的开源引擎

### 关联概念

- Spark 2.0

- 3D Gaussian Splatting

- 连续 LoD 树

- GPU 虚拟内存

- 注视点渲染
