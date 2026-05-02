---
title: Midscene
type: entity
tags:
- 浏览器自动化
- 多模态
- AI 产品
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b47f0ecf37cf4ca8a26997bcfa810f30
notion_id: b47f0ecf-37cf-4ca8-a269-97bcfa810f30
---

## 定义

Midscene 是字节跳动开源的一款基于 AI 视觉驱动的 UI 自动化框架。与传统基于 DOM 选择器的自动化方案不同，Midscene 的核心思路是先通过多模态模型理解页面截图内容（元素位置、文字、按钮等），再决定下一步操作动作。

**别名**：无

## 关键要点

- **视觉优先**：不依赖 DOM 结构，而是通过截图理解页面，适用于 Shadow DOM 等传统选择器难以处理的场景

- **字节出品**：由字节跳动团队开发并开源

- **补位方案**：适合在复杂页面结构（如微信视频号后台 wujie Shadow DOM）中作为 DOM 自动化的补充

- **代价明确**：比纯 DOM 自动化更慢（多一层视觉理解）、有模型调用成本、稳定性依赖视觉理解质量而非精确选择器

## 适用场景

- Shadow DOM 密集的页面（如视频号后台）

- 页面结构不规整、常规选择器不稳定的场景

- 需要跨结构理解能力的 UI 自动化任务

## 关联概念

- Chrome DevTools Protocol（底层浏览器控制协议）

- Playwright（DOM 自动化框架）

- browser-use（面向 AI Agent 的浏览器操作封装）

- BrowserMCP（基于当前浏览器上下文的 MCP 方案）

## 来源引用

- [摘要：一文彻底了解浏览器自动化，cdp、playwright、browser-user、midscene、browsermcp](summaries/摘要：一文彻底了解浏览器自动化，cdp、playwright、browser-user、midscene、browsermcp.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU5ODg1NDk1Ng%3D%3D&mid=2247484662&idx=1&sn=86710f5235fc8287ed0fdf470145617d&chksm=ffb825b8a302ea2f0bb235145fc1d6b62eb3c0ad603642f1d2e993302656ef5c5996f49a76c5#rd)）
