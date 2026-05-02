---
title: Anti-AI-Slop
type: concept
tags:
- AI 设计
- 提示工程
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3d646ce6748e4359a81fe5e45855932b
notion_id: 3d646ce6-748e-4359-a81f-e5e45855932b
---

## 定义

Anti-AI-Slop（反 AI-Slop 机制）是一种针对 AI 生成设计内容的多层质量控制机制，旨在防止 AI 输出低质量、千篇一律的「AI 味」设计（即 AI Slop）。该概念在 Open Design 项目中被系统化实现为 6 重质量门禁。

## 关键要点

- **AI Slop 的典型特征**：紫色渐变背景、通用 Emoji 图标、圆角左边框卡片、Inter 作 Display 字体、编造虚假数据（如 "10× faster"）

- **6 重质量控制层**：

  1. 强制初始化表单（Discovery Form）——首轮必须收集需求，禁止直接生成

  1. 品牌资产五步协议——定位、下载、提取色值、编码规范、复述确认

  1. 五维自评——预输出质量门禁，每维度 1-5 分，低于 3 分需修复

  1. P0/P1/P2 检查清单——分级质量检查

  1. AI Slop 黑名单——明确禁止的设计模式列表

  1. 诚实占位符——无真实数据时用 — 或灰块标注，不编造数据

- 核心原则：Agent 绝不允许从记忆中猜测品牌色值，必须从实际品牌资产中提取

## 关联概念

- [Open Design](entities/Open Design.md)

- [Prompt Stack](concepts/Prompt Stack.md)

- [DESIGN.md](concepts/DESIGN.md.md)

## 来源引用

- [摘要：Open Design开源AI设计平台操作指南](summaries/摘要：Open Design开源AI设计平台操作指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=1&sn=b7e340057327e37eaa414da8f73f2c54&chksm=cf03bb2e5e663169f8ac4d30e861142ad85293ab74b7795fb00b0d259549bef37aa984e1a38e#rd)）

- [摘要：Open Design源码分析](summaries/摘要：Open Design源码分析.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=2&sn=b09ff622c0ea5ba39d0f9533fa955bf6&chksm=cffc0736bf58f08e4a1ea67ea6600b291bf6061dbc64a8a0b30ed6f6576dceec616fc3f6dff0#rd)）
