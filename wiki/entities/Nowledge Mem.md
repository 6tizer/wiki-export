---
title: Nowledge Mem
type: entity
tags:
- 知识管理
- 长期记忆
- AI 产品
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/56c1d38ef2164faf9fd8b7e28cbed358
notion_id: 56c1d38e-f216-4faf-9fd8-b7e28cbed358
---

## 定义

Nowledge Mem 是 Nowledge Labs 开发的桌面端个人知识管理应用，核心理念是将用户日常使用 AI 时产生的知识自动捕获、组织并沉淀为可长期复用的知识图谱。v0.8 版本全面拥抱 Karpathy 的 LLM Wiki 方法论，为知识图谱加上了完整的 Wiki 阅读层。

别名：Mem、Nowledge Mem

## 关键要点

- 以「超图」知识图谱为底层数据结构，支持记忆、资料、结晶（Crystal）之间的多维连接

- Background Intelligence 后台持续运行，自动识别主题聚类、演化关系和矛盾点

- v0.8 新增 Wiki 标签、实体页、[[wikilink]] 可点击、「和 AI 一起精读」、Wiki 导出（兼容 Obsidian/Logseq）、按页取的 Wiki API

- 支持 CLI/API/MCP/插件/Skills 多种接入方式

- 支持 Linux 服务器无头部署，远程通过 Web/Mobile 访问

- 「深入研究」功能将 Wiki 页面与 Graph Intelligence 打通，可在图谱上做探索和协作

## 产品架构

- **写入路径**：记忆保存 → 资料导入 → 浏览器扩展抓取 → Agent 决策提炼 → 超图知识图谱

- **阅读路径（v0.8）**：Wiki 标签 → 主题页 → 实体页 → 结晶页 → [[wikilink]] 跳转

- **导出**：纯 Markdown 文件夹（[index.md](http://index.md/)、topics/、entities/、crystals/），兼容 Obsidian

## 关联概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Background Intelligence](concepts/Background Intelligence.md)

- [OpenKB](entities/OpenKB.md)

- [PageIndex](entities/PageIndex.md)

## 来源引用

- [摘要：Nowledge Mem 0.8：LLM Wiki](summaries/摘要：Nowledge Mem 0.8：LLM Wiki.md)（[原文](https://x.com/wey_gu/status/2049720331850625229)）
