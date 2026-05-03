---
title: Open Design
type: entity
tags:
- AI 设计
- 代码生成
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/49d51ec0bf4d4e25943420ad2b3f8027
notion_id: 49d51ec0-bf4d-4e25-9434-20ad2b3f8027
---

## 定义

Open Design 是由 nexu-io 团队开发的本地优先（Local-first）、完全开源（Apache-2.0）的 AI 设计生成平台，定位为 Anthropic Claude Design 的开源替代方案。其核心设计理念是「不内置 AI Agent」——将 Agent 运行委托给用户本地已安装的 CLI 工具（Claude Code、Codex CLI、Cursor Agent、Gemini CLI 等），自身只负责 Skill 编排、Design System 注入、Prompt Stack 组装和沙盒化预览渲染。

别名：open-design

## 关键要点

- 项目在 Claude Design 发布后约 72 小时内完成核心逆向工程，编写超过 18,700 行代码，还原 95%+ 核心体验

- 截至 2026 年 4 月，GitHub 超 4,500 Star

- 内置 19 个可组合 Skills（原型设计、演示文稿、办公文档）和 71 套品牌级 Design Systems

- 文件式扩展：Skill 即文件夹（[SKILL.md](http://skill.md/) + assets + references），Design System 即单个 Markdown 文件（9 段式 [DESIGN.md](http://design.md/) Schema）

- 6 重 Anti-AI-Slop 质量控制机制

- 支持 BYOK（Bring Your Own Key）模式，可接入 Anthropic 官方或第三方 API 中转

- 三种部署拓扑：全本地、Vercel + 本地 Daemon、Vercel 直连 API

- 多格式导出：HTML、PDF、PPTX、ZIP、Markdown

## 技术架构

- Web App + 本地 Daemon + 用户已有的 Agent CLI

- Daemon 负责 Skill 注册、Design System 加载、Agent CLI 调度

- 三层 Prompt Stack：基础系统提示词 + Design System 内容 + Skill 工作流

- 沙盒 iframe 渲染预览（sandbox="allow-scripts"）

- SQLite 存储项目数据

## 关联概念

- [Anti-AI-Slop](concepts/Anti-AI-Slop.md)

- [Prompt Stack](concepts/Prompt Stack.md)

- [Claude Design](entities/Claude Design.md)

- [DESIGN.md](concepts/DESIGN.md.md)

- [BYOK](concepts/BYOK.md)

## 来源引用

- [摘要：Open Design开源AI设计平台操作指南](summaries/摘要：Open Design开源AI设计平台操作指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=1&sn=b7e340057327e37eaa414da8f73f2c54&chksm=cf03bb2e5e663169f8ac4d30e861142ad85293ab74b7795fb00b0d259549bef37aa984e1a38e#rd)）

- [摘要：Open Design源码分析](summaries/摘要：Open Design源码分析.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=2&sn=b09ff622c0ea5ba39d0f9533fa955bf6&chksm=cffc0736bf58f08e4a1ea67ea6600b291bf6061dbc64a8a0b30ed6f6576dceec616fc3f6dff0#rd)）

- [摘要：Open Design × Kami：让你的 AI Coding Agent 变身专业排版设计师](summaries/摘要：Open Design × Kami：让你的 AI Coding Agent 变身专业排版设计师.md)（[原文](https://x.com/tuturetom/status/2050542908713910316)）

- [摘要：Open Design 正式开源最完整版 codex 同款 pets 宠物](summaries/摘要：Open Design 正式开源最完整版 codex 同款 pets 宠物.md)（[原文](https://x.com/tuturetom/status/2050604396531143131)）
