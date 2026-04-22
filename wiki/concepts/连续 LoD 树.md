---
title: 连续 LoD 树
type: concept
tags:
- 开发工具
- 内容创作
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ba7e37faccbd4b88945dcf49e069f254
notion_id: ba7e37fa-ccbd-4b88-945d-cf49e069f254
---

### 定义

连续 LoD 树是一种把不同细节层级组织成树状结构的表示方式。Spark 2.0 用它在视角变化时持续选择“刚好够用”的 splat 数量，而不是在少数离散版本之间硬切换。

### 关键要点

- 每个内部节点都是其子节点 splat 的近似融合结果

- 渲染时根据视角在树上动态选择近处高细节、远处低细节

- 让移动端和桌面端始终受固定 splat 预算约束，从而稳定帧率

- 相比离散 LoD 切换，更能减少画面跳变

### 来源引用

- [刚刚，李飞飞最新成果发布，手机也能跑亿级粒子的 3D 世界了｜附体验地址](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA%3D%3D&mid=2651087721&idx=1&sn=119485bcb1450f9f1e0d1319733528fa&chksm=bc0eb7380742222c99e0a18f40d5e0628cdf29eda89f2dcf858670859b610e225c78e4f98c8e#rd)｜源文章：刚刚，李飞飞最新成果发布，手机也能跑亿级粒子的 3D 世界了｜附体验地址

- [Three.js](https://x.com/sparkjsdev/status/2044090505982816449)｜源文章：Spark 2.0：把亿级 3D 高斯渲染带进浏览器的开源引擎

### 关联概念

- Spark 2.0

- 3D Gaussian Splatting

- RAD 格式

- GPU 虚拟内存

- 注视点渲染
