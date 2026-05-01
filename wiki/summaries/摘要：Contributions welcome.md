---
title: 摘要：Contributions welcome.
type: summary
tags:
- 社交媒体
- 提示工程
- 内容自动化
status: 已审核
confidence: medium
last_compiled: '2026-04-28'
source_tags: skills
source_article_url: https://www.notion.so/34f701074b6881d6bc48ceb0a91ca663
notion_url: https://www.notion.so/Tizer/7eacb414d104452886ebfb08dfe5bb9c
notion_id: 7eacb414-d104-4528-86eb-fb08dfe5bb9c
---

## 一句话摘要

Charlie Hills 将其个人内容矩阵背后的 17 个 Claude Skills 全部开源，形成一套覆盖语音定义、LinkedIn 写作、视频脚本、社群互动的模块化内容生产系统。

## 关键洞察

- **Voice Builder 架构**：整个技能体系以 `voice-builder` 为根基，生成 `about-me.md` 和 `voice.md` 两个上下文文件，其余 16 个技能统一读取，从而保证跨平台语调一致性

- **六大技能分区**：基础语音 → LinkedIn → 内容规划 → 图形设计 → 视频 → 社群，形成从策略到执行的完整 pipeline

- **外部服务集成**：post-scorer 和 reels-scripting 依赖 Apify 抓取历史数据，图像类技能输出 Gemini 提示词而非直接生图，降低 API 耦合

- **多种分发方式**：支持 Claude Code plugin marketplace、git clone、zip 上传、git submodule 四种安装路径，适配不同开发者习惯

- **实战验证**：作者在自己的 350k+ 粉丝账号上测试每个技能后才发布，具备一定可信度

## 提取的概念

- [social-media-skills](entities/social-media-skills.md)（本次新建 entity）

- [Claude Code Skills](concepts/Claude Code Skills.md)（已有 concept）

- [Skill Collection](concepts/Skill Collection.md)（已有 concept）

## 原始文章信息

- **作者**：@charliejhills（Charlie Hills）

- **来源**：X书签

- **发布时间**：2026-04-26

- **原文链接**：[https://x.com/charliejhills/status/2048428282174156996](https://x.com/charliejhills/status/2048428282174156996)

- **GitHub**：[charlie947/social-media-skills](https://github.com/charlie947/social-media-skills)（300★，MIT）

## 个人评注

这套技能库对 Tizer 的内容 pipeline 有直接参考价值：voice-builder 的「基础上下文 + 下游技能读取」模式与 OpenClaw 中 Skill 级联依赖思路一致；content-matrix 和 niche-research 可作为内容自动化流程的灵感来源。其中 post-scorer 用 Apify 拉取历史表现数据再打分的做法，也值得在 HITL 评审环节借鉴。
