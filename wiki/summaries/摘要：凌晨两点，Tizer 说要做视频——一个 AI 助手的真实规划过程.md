---
title: 摘要：凌晨两点，Tizer 说要做视频——一个 AI 助手的真实规划过程
type: summary
tags:
- 内容自动化
- 视频/3D
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: https://www.notion.so/355701074b68810e868cc0527fb280d4
notion_url: https://www.notion.so/Tizer/95d45e46194a4900899a888a39025721
notion_id: 95d45e46-194a-4900-899a-888a39025721
---

## 一句话摘要

AI 助手 Alphana 通过 Wiki 知识库检索和迭代拆解，为 Tizer 规划了一条基于 LibTV + 后期补全工具的全自动化 AI 视频内容流水线，完成从技术选型到三阶段 MVP 的完整路径。

## 关键洞察

- **知识库是 AI 规划的核心外脑**：两次 Wiki 检索分别解决了「怎么做」和「缺什么补什么」，知识库的价值在于「随时可召回」而非单纯存储

- **路径选择对齐现有流水线**：选定 LibTV 的关键原因是其全链路架构可以复用已有公众号流水线的 HITL 模式（人类只做选题确认和成品审查）

- **诚实面对半成品是 AI 的核心能力**：发现 LibTV 输出在字幕、转场、背景一致性上存在缺口后立即承认，而非回避问题

- **后期缺口用专业工具逐个补全**：Whisper（字幕）、FunClip（语音精剪）、CutClaw（音乐驱动多 Agent 剪辑）、social-auto-upload（跨平台分发）四件套填补 LibTV 的不足

- **方法论可复用**：「Wiki 检索 → 分层拆解 → MVP 分阶段」适用于播客、课程等任何新业务探索

## 提取的概念

- [LibTV](entities/LibTV.md)

- [Seedance 2.0](entities/Seedance 2.0.md)

- [SkyReels V4](entities/SkyReels V4.md)

- [FunClip](entities/FunClip.md)

- [CutClaw](entities/CutClaw.md)

- [social-auto-upload](entities/social-auto-upload.md)

## 原始文章信息

- **作者**：Alphana和大船的AI工作区

- **来源**：微信公众号

- **发布时间**：2026-04-15

- **原文链接**：[凌晨两点，Tizer 说要做视频](https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw%3D%3D&mid=2247484142&idx=1&sn=43beb217d8e5f852bfc0214cf95b5eed&chksm=cf8bf31ce6636b221c266cb7bf06a61636464b8e2f0b41f79f60218898fdf7218e5ceb19ad33#rd)

## 个人评注

本文以第一人称视角记录了 Alphana（AI CEO 助手）为 Tizer 规划视频业务的全过程，直接展示了 OpenClaw 生态中 AI 助手如何利用 Wiki 知识库做战略级规划。文中提到的 LibTV OpenClaw Skill 调用、CutClaw 多 Agent 剪辑、以及公众号流水线的 HITL 模式，与 Tizer 当前的内容自动化体系高度相关。三阶段 MVP（工具验证→Skill 设计→首条视频跑通）的方法论可以直接迁移到其他新业务线探索中。
