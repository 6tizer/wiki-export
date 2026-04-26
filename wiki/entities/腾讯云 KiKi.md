---
title: 腾讯云 KiKi
type: entity
tags:
- AI 产品
status: 审核中
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b1676c85106443e7b3d02ed1746e6a79
notion_id: b1676c85-1064-43e7-b3d0-2ed1746e6a79
---

## 定义

腾讯云 KiKi 是内置在腾讯云环境中的部署 Agent，能够根据自然语言需求执行资源购买、环境初始化、应用部署等云上操作。

## 核心特性

- **双执行模式**：同时提供界面模式与编程模式，分别对应模拟操作页面与直接调用 API。

- **对话式部署**：把购买资源、初始化环境、部署应用等流程压缩为自然语言任务。

- **HITL 确认机制**：在关键节点保留人工确认，降低高风险操作的误执行概率。

## 使用边界

- 编程模式在复杂任务中仍可能执行到一半报错。

- 线上问题如 Nginx 缓存仍需要人工排查和兜底。

- 历史记录不透明会增加复盘和调试成本。

## 来源引用

- [摘要：关于我花了1天时间，用AI全驱动做了一个网站，不得不说的故事](summaries/摘要：关于我花了1天时间，用AI全驱动做了一个网站，不得不说的故事.md)（[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg3NDkwOTQyNA%3D%3D&mid=2247488992&idx=1&sn=a57af915b8cad477765a18199a70b9b6&chksm=cf0234d86fdd9d2c9243710041680eaa4eab26399f11b26dce450987db383cbbdc933e9413de#rd)，来源：微信｜作者：圣Sheng）
