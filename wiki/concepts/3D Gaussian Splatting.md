---
title: 3D Gaussian Splatting
type: concept
tags:
- 内容创作
- LLM
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/2075ecf9da4441e6a6f016a57c9db645
notion_id: 2075ecf9-da44-41e6-a6f0-16a57c9db645
---

### 定义

3D Gaussian Splatting（又称 3D 高斯泼溅），常简称为 3DGS，是一种用大量带透明度和空间参数的高斯椭球来表示真实场景的三维重建与渲染方法，能够用照片快速生成可交互的 3D 内容。

### 关键要点

- 不依赖传统三角网格建模，而是以大量 splat 表达几何与外观

- 每个 splat 携带位置、尺度、朝向、颜色与透明度等属性

- 软边界叠加带来更自然的砖墙、树叶、玻璃等视觉效果

- 高质量场景常包含数千万个 splat，因此对传输和渲染系统要求很高

### 来源引用

- [刚刚，李飞飞最新成果发布，手机也能跑亿级粒子的 3D 世界了｜附体验地址](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA%3D%3D&mid=2651087721&idx=1&sn=119485bcb1450f9f1e0d1319733528fa&chksm=bc0eb7380742222c99e0a18f40d5e0628cdf29eda89f2dcf858670859b610e225c78e4f98c8e#rd)｜源文章：刚刚，李飞飞最新成果发布，手机也能跑亿级粒子的 3D 世界了｜附体验地址

- [Three.js](https://x.com/sparkjsdev/status/2044090505982816449)｜源文章：Spark 2.0：把亿级 3D 高斯渲染带进浏览器的开源引擎

- [腾讯混元开源世界模型！2.0版本一键生成3D空间，游戏关卡随心造](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247883767&idx=2&sn=8df1b032989aae3535de8a333936c008&chksm=e9fc388108e5dbf1e19a2001085ecdd219342c067428ab8ea53af13379164860eb756ca8bc30#rd)｜源页面：腾讯混元开源世界模型！2.0版本一键生成3D空间，游戏关卡随心造

- [摘要：NVIDIA Lyra 2.0：从一张图片生成可探索的持久 3D 世界](summaries/摘要：NVIDIA Lyra 2.0：从一张图片生成可探索的持久 3D 世界.md)（[原文](https://x.com/HuggingModels/status/2045337281775718800)）

### 关联概念

- Spark 2.0

- 连续 LoD 树

- RAD 格式

- GPU 虚拟内存

- 注视点渲染

- HY-WorldMirror

- HY-World

- Lyra 2.0

- NVIDIA Isaac Sim
