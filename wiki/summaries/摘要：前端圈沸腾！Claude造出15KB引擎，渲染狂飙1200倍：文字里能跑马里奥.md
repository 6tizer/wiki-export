---
title: 摘要：前端圈沸腾！Claude造出15KB引擎，渲染狂飙1200倍：文字里能跑马里奥
type: summary
tags:
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-26'
source_tags: Vibe Coding, 开源项目
source_article_url: ''
notion_url: https://www.notion.so/e6c45bba339245799a789c220ebb81f1
notion_id: e6c45bba-3392-4579-9a78-9c220ebb81f1
---

## 一句话摘要

Pretext 是 Midjourney 工程师 Cheng Lou 开源的 15KB 纯 TypeScript 文本排版引擎，通过 canvas.measureText() 绕过 DOM Reflow，在 Safari 上实现比传统方案快1242倍的渲染速度，彻底打破30年网页排版枷锁。

## 关键洞察

- **根本突破**：用 canvas 做文字测量不触发 Reflow，所有排版计算变成纯加减乘除

- **性能数据**：Chrome 快483倍，Safari 快1242倍，120fps 处理数十万文本框

- **精度验证**：Chrome/Safari/Firefox 三大浏览器7680项穷举测试全部满分

- **Claude Code 参与开发**：用 CC 和 Codex 在关键容器宽度下做测量和迭代比对，跑了好几周

- **开发者疯狂二创**：文字里跑马里奥、Bad Apple、流体文字、物理引擎等

- **架构意义**：从 CSS/DOM 约束中解放，迈向 Canvas/GPU 渲染时代

## 提取的概念

- Pretext

## 原始文章信息

- **作者**: 新智元

- **来源**: 微信公众号

- **发布时间**: 2026-03-30

- **GitHub**: [https://github.com/chenglou/pretext](https://github.com/chenglou/pretext)

## 个人评注

Pretext 对前端内容展示有革命性意义，对 Tizer 的内容 pipeline 中涉及 web 展示的部分可能有潜在价值。
