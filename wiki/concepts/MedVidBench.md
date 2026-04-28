---
title: MedVidBench
type: concept
tags:
- 模型评测
- 多模态
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/148c1b1d26364f2c8f9d9aaf6fa30dd4
notion_id: 148c1b1d-2636-4f2c-8f9d-9aaf6fa30dd4
---

## 定义

MedVidBench 是全球首个面向医疗视频理解领域的大规模评测基准数据集，由联影智能研究团队构建。包含 53 万余条视频-指令对，覆盖 8 个专业医学数据源，横跨腹腔镜、开放手术、机器人手术及护理操作等核心临床场景。

## 关键要点

- 包含 53 万+视频-指令对，覆盖 8 个医学数据源（CholecT50、CholecTrack20、Cholec80-CVS、CoPESD、AVOS、EgoSurgery、JIGSAWS、NurViD）

- 设计三层任务粒度架构：视频级（VS 视频摘要、NAP 下一步预测）、片段级（TAG 时间动作定位、STG 时空定位、DVC 密集描述）、帧级（RC 区域描述、CVS 安全视野评估、SA 技能评估）

- 数据质量通过专家引导式提示词工程 + 双模型交叉验证（GPT + Gemini）保障

- 提供大规模版（53 万样本）和标准版（5.15 万样本）两个版本

- 已上线公开排行榜（Leaderboard），面向全球开发者开放提交

- 排行榜地址：[https://huggingface.co/spaces/UII-AI/MedVidBench-Leaderboard](https://huggingface.co/spaces/UII-AI/MedVidBench-Leaderboard)

## 来源引用

- [摘要：让大模型理解真实医疗视频，全球首个开源技术方案来了！](summaries/摘要：让大模型理解真实医疗视频，全球首个开源技术方案来了！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651030763&idx=1&sn=9c3e8e595c0f07a91388a3bb94a271ab&chksm=854fb7d136df13086ee1a41b12aa402ab1c7c4fce28d91dbf4f46dc0d1a0cc280c2f0dd9a785#rd)）
