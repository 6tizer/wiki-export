---
title: Video Use
type: entity
tags:
- 内容创作
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/33d15d9620e145199826491d8c15cbcf
notion_id: 33d15d96-20e1-4519-9826-491d8c15cbcf
---

## 定义

Video Use 是 browser-use 团队推出的一个 Claude Code Skill，用自然语言驱动视频剪辑流程，把转录、粗剪、调色、字幕、动画叠加与自检整合成一条可自动执行的命令行流水线。

## 关键要点

- 输入是一组原始素材视频，输出目标是可直接发布的 `final.mp4`。

- 通过 transcript 作为主上下文、timeline PNG 作为按需视觉补充，尽量避免让 LLM 直接处理海量视频帧。

- 支持去填充词、自动调色、烧录字幕、Manim/Remotion 动画叠加与渲染后自检。

- 依赖 ElevenLabs Scribe 提供词级时间戳，说明高质量转录是整条流水线的关键中间层。

## 来源引用

- [摘要：Video Use：用 Claude Code 把「对着镜头说话」变成一键出片](summaries/摘要：Video Use：用 Claude Code 把「对着镜头说话」变成一键出片.md)（[原文](https://x.com/gregpr07/status/2044554557221675380)）

- [摘要：🚨 Goodbye Video editing](summaries/摘要：🚨 Goodbye Video editing.md)（[原文](https://x.com/TawohAwa/status/2046566836012306544)）

- [摘要：SOMEONE OPEN-SOURCED VIDEO EDITING FOR AI AGENTS.](summaries/摘要：SOMEONE OPEN-SOURCED VIDEO EDITING FOR AI AGENTS.md)（[原文](https://x.com/socialwithaayan/status/2047568884304367722)）

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Browser Use](entities/Browser Use.md)

- [Remotion](entities/Remotion.md)

- [视频再利用流水线](concepts/视频再利用流水线.md)

- [ElevenLabs Scribe](entities/ElevenLabs Scribe.md)

- [Manim](entities/Manim.md)

- [Agent 原生视频编辑](concepts/Agent 原生视频编辑.md)
