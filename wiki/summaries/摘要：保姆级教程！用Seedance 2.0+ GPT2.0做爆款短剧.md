---
title: 摘要：保姆级教程！用Seedance 2.0+ GPT2.0做爆款短剧
type: summary
tags:
- 视频/3D
- 图像生成
- 内容自动化
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b68816087bdca0850b13bf2
notion_url: https://www.notion.so/Tizer/0e5d5ef32a15453aa6c4d65acdf1636f
notion_id: 0e5d5ef3-2a15-453a-a6c4-d65acdf1636f
---

## 一句话摘要

本文是一篇从零开始的 AI 短视频制作全流程教程，教你用 GPT Image 2.0 生成分镜图 + Seedance 2.0（即梦）生成视频片段 + 剪映剪辑成片。

## 关键洞察

- **故事先行**：AI 视频不是一句提示词就能生成的，需要先把想法拆成脚本→段落→分镜，每个镜头只描述静止的单帧画面

- **三视图锁定角色**：在生成任何分镜前，先用 ChatGPT 生成角色的正面/侧面/背面三视图，后续每段视频都上传这张图作为参考，否则角色外貌会偏移

- **四宫格/九宫格控制节奏**：慢节奏段落用四宫格（4个镜头），快节奏用九宫格（9个镜头），通过镜头密度控制叙事节奏

- **视频提示词只写动作**：即梦已经能看到上传的参考图，提示词不要重复描述画面，只写「什么在动、怎么动、镜头运动、时间段」

- **声音一致性**：用第一段视频的音频做参考，或通过 Fish Audio 找统一参考音色，解决多段视频人声不一致问题

## 提取的概念

- [Seedance 2.0](entities/Seedance 2.0.md)（AI 视频生成模型，即梦平台核心引擎）

- [GPT-Image-2](entities/GPT-Image-2.md)（用于生成角色三视图和分镜参考图）

- [文本分镜设计](concepts/文本分镜设计.md)（从脚本到逐镜头描述的设计流程）

- [人物一致性](concepts/人物一致性.md)（通过三视图 + 每段上传参考图实现跨片段角色一致）

- [Fish Audio](entities/Fish Audio.md)（声音克隆平台，用于统一参考音色）

## 原始文章信息

- **作者**：Biteye 核心贡献者 Changan

- **来源**：Biteye中文（微信公众号）

- **发布时间**：2026-04-29

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzkxMjg4NDA4MA%3D%3D&mid=2247485201&idx=1&sn=761932ad14d55afec2386d56deb0da2c&chksm=c008f6758eaa1b093d3a668d2acd94d1eb5243fa03e46224a93f6ba078afead9f7eb221e4393#rd)

## 个人评注

这篇教程把 AI 视频制作的完整链路（脚本→分镜→生图→生视频→剪辑）拆解得非常清晰，适合作为 AI 视频工作流的入门参考。对 Tizer 的内容自动化流水线有启发：如果未来 OpenClaw 需要生成产品演示视频，这套「三视图 + 分镜 + 即梦」的流程可以模块化复用。标点符号控制 AI 配音语气的技巧也值得记录。
