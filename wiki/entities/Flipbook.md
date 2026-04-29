---
title: Flipbook
type: entity
tags:
- AI 产品
- 图像生成
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/022b44cf6902478db39cf0fcd0f5674b
notion_id: 022b44cf-6902-478d-b39c-f0fcd0f5674b
---

## 定义

Flipbook 是一款实验性视觉浏览器产品，用实时生成的图像取代传统 HTML 网页，将整个互联网变成一张可以无限延展、按需生成的交互式图像。用户通过点击图像中的任意区域来触发新一帧图像的生成，实现逐层深入的信息探索。

**别名**：Visual Browser、视觉浏览器

## 关键要点

- 所有"页面"本质上都是由图像模型实时渲染的像素，没有 HTML、DOM 或传统链接

- 屏幕上的文字也是图像模型直接渲染的，而非叠加的文本层

- 信息来源结合了模型自身知识和具备行动能力的搜索系统

- 底层使用激活缓存、量化、torch.compile 和内存快照（CUDA Graph）实现低延迟推理

- 采用等距视角（isometric）插画风格，在可读性和表现力之间取得平衡

- 适合结构复杂、关系交错、需要建立整体认知的信息探索场景（如教育、旅行规划、复杂文学作品理解）

- 不适合高频、精确、效率优先的查询任务

## 团队与背景

- 创始团队成员包括 Zain（工程）和 EbbieJiao（设计）

- 画面风格经历上百次迭代，从 80 年代 CRT 复古科幻风、50 年代漫画风，最终选定等距视角编辑插画风

## 关联概念

- 视觉浏览器

- 激活缓存

- torch.compile

- Generative UI

## 来源引用

- [摘要：最近刷屏的Flipbook，想把互联网彻底变成实时生成的无限世界](summaries/摘要：最近刷屏的Flipbook，想把互联网彻底变成实时生成的无限世界.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ%3D%3D&mid=2247628305&idx=1&sn=1634861c0bf7ef88e8ea3c207591936f&chksm=c3b497c9c9527e8822c484d33b554e86ada2fad94d08f10aee624de72a30655b90d22527cb33#rd)）
