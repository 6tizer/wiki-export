---
title: 摘要：Three.js
type: summary
tags:
- 前端开发
- 视频/3D
- AI 设计
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68815fbe6cebca6bdff645
notion_url: https://www.notion.so/Tizer/2c655c459e8349e0bfd838eb2bf13914
notion_id: 2c655c45-9e83-49e0-bfd8-38eb2bf13914
---

### 一句话摘要

Spark 2.0 通过连续 LoD 树、RAD 渐进式流式加载和 GPU 虚拟内存三套机制，让 3D Gaussian Splatting 场景首次能在基于 Three.js 的 WebGL2 栈上，以网页方式流畅承载 100M+ splats，并覆盖手机到 VR 设备。

### 关键洞察

- 这条技术线程把 3DGS 的规模瓶颈拆成三件事：细节层级选择、数据传输带宽、GPU 显存预算，并分别给出对应工程解法

- 连续 LoD 树让系统可以按视角动态选择 splat 切片，在不同设备上维持相对稳定的帧率与渲染预算

- RAD 格式把场景切成可随机访问的数据块，配合渐进式流式加载，让用户先看到粗略轮廓，再逐步补细节

- GPU 虚拟内存把操作系统的分页思路搬到显存管理里，使超大场景不必一次性装入移动端 GPU

- 整个方案坚持 WebGL2 与 Three.js 兼容路线，核心价值是把大规模 3DGS 从实验性 demo 推向可在浏览器普遍分发的基础设施

### 提取的概念

- [Spark 2.0](entities/Spark 2.0.md)

- [3D Gaussian Splatting](concepts/3D Gaussian Splatting.md)

- [连续 LoD 树](concepts/连续 LoD 树.md)

- [RAD 格式](concepts/RAD 格式.md)

- [GPU 虚拟内存](concepts/GPU 虚拟内存.md)

- [注视点渲染](concepts/注视点渲染.md)

### 原始文章信息

- 作者：@sparkjsdev

- 来源：X书签

- 发布时间：2026-04-14

- 链接：[https://x.com/sparkjsdev/status/2044090505982816449](https://x.com/sparkjsdev/status/2044090505982816449)

### 个人评注

这类技术线程非常适合进入 Tizer 的知识管线：一方面可快速沉淀成“摘要 + 概念卡片”的 Wiki 结构，另一方面也能为后续追踪 Web 原生 3D、实时渲染基础设施与内容创作工具机会提供稳定素材。
