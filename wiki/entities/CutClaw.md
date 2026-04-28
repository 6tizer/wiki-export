---
title: CutClaw
type: entity
tags:
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/af23b2528875440691857ddeb6ecb1f7
notion_id: af23b252-8875-4406-9185-7ddeb6ecb1f7
---

## 定义

CutClaw（大湾区大学GVC实验室 + 北交大开源）是一个音乐驱动的AI视频剪辑系统，先分析音乐结构（节拍/重拍/音高/能量曲线）再决定剪辑点，生成音画合一的电影感短片。

## 核心区别：音乐驱动 vs 后配音乐

- 大多数AI剪辑工具：先剪辑→再配音乐

- CutClaw：先分析音乐结构（主歌/副歌等单元）→再科学属配视觉叙事

## 多智能体流水线

1. 视频和音频分别拆解为结构化字幕

1. 多智能体规划镜头、选择片段时间戳

1. 验证最终质量

1. 渲染生成成片

## 关键功能

- **一键解构**：第一次处理后缓存结构化素材，第二次可复用

- **内容感知裁剪**：适配各社交平台比例

- **一句话指令**：用户只需文字指令，CutClaw执行剪辑任务

## GitHub

[https://github.com/GVCLab/CutClaw](https://github.com/GVCLab/CutClaw)

## 来源引用

- [摘要：其他家在接入龙虾的时候，快手默默上线了一套硬核技术](summaries/摘要：其他家在接入龙虾的时候，快手默默上线了一套硬核技术.md)
