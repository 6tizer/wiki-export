---
title: 摘要：Open Design 正式开源最完整版 codex 同款 pets 宠物
type: summary
tags:
- AI 设计
- 代码生成
status: 已审核
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: https://www.notion.so/355701074b68814f8b04cdc35e978f86
notion_url: https://www.notion.so/Tizer/a80d64c55d2949208f6ea2a778f39326
notion_id: a80d64c5-5d29-4920-8f6e-a2a778f39326
---

## 一句话摘要

Open Design 正式开源最完整版本的 codex 同款 pets 宠物系统，支持 100+ 宠物、8 个默认角色和 4 种动作状态，同时项目整体已发展为支持 13 种 Coding Agent CLI、31 个 Skills 和 129 套 Design System 的全功能 Claude Design 开源替代方案。

## 关键洞察

- **Pets 功能全量开源**：超过 100 个 codex 同款宠物（包括 Sam Altman、Dario、OpenClaw 作者 steipete、Trump 等名人角色），支持 hover、拖拽等全部运动状态，超 1 万行代码实现

- **Agent 驱动的宠物生成**：支持 codex 的 `/hatch` skills，可通过 Agent 在线生成专属宠物

- **项目规模快速增长**：GitHub 已达 17,130 Stars，支持 13 个 Coding Agent CLI（Claude Code、Codex、Devin、Cursor Agent、Gemini CLI 等）自动检测

- **完整的 Skill + Design System 生态**：31 个文件式 Skills（基于 [SKILL.md](http://skill.md/) 规范）+ 129 套 Design System（基于 [DESIGN.md](http://design.md/) Schema），涵盖设计、营销、工程、产品等多个场景

- **Anti-AI-Slop 质量控制**：内置五维自我批评（philosophy/hierarchy/execution/specificity/restraint）、P0/P1/P2 检查清单、slop 黑名单等机制，确保生成设计不落入 AI 审美陷阱

- **多媒体生成能力**：集成 gpt-image-2（图像）、Seedance 2.0（视频）、HyperFrames（HTML→MP4 动效），附带 93 个即用 Prompt 模板

## 提取的概念

- [Open Design](entities/Open Design.md)

- [Codex Pets](concepts/Codex Pets.md)

- [Claude Design](entities/Claude Design.md)

- [SKILL.md](concepts/SKILL.md.md)

- [DESIGN.md](concepts/DESIGN.md.md)

- [Anti-AI-Slop](concepts/Anti-AI-Slop.md)

- [BYOK](concepts/BYOK.md)

## 原始文章信息

- **作者**：@tuturetom（Tom Huang）

- **来源**：X 书签

- **发布时间**：2026-05-02

- **链接**：[原文推文](https://x.com/tuturetom/status/2050604396531143131) ｜ [GitHub 仓库](https://github.com/nexu-io/open-design)

## 个人评注

Open Design 的 Pets 功能是一个有趣的开发者体验（DX）创新——将 Agent 工作状态拟人化为桌面宠物，通过情绪反馈降低等待焦虑。对 Tizer 的 OpenClaw 项目有参考价值：类似的游戏化反馈机制可以应用于 Agent 长时间执行任务时的用户等待体验设计。此外，Open Design 的 [SKILL.md](http://skill.md/) 文件式扩展架构和 Anti-AI-Slop 质量门控思路值得在内容自动化管线中借鉴。
