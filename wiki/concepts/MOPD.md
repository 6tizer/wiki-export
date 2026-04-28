---
title: MOPD
type: concept
tags:
- 训练/微调
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c13f41414abf4bc6a1f31418ffc9435e
notion_id: c13f4141-4abf-4bc6-a1f3-1418ffc9435e
---

## 定义

MOPD（Multi-teacher Online Policy Distillation，多教师在线策略蒸馏）是一种后训练方法，核心思路是先对多个领域分别训练专家模型（如数学专家、安全专家、工具使用专家），再通过在线策略蒸馏将多个专家的能力合并回一个统一模型。与传统离线蒸馏不同，MOPD 在蒸馏阶段保持学生模型在线生成轨迹，教师模型实时提供反馈信号，从而减少分布偏移。

## 关键要点

- 后训练三段式中的最后一环：SFT → 领域专家 RL → MOPD 统一蒸馏

- 每个领域专家可以独立迭代，不受其他领域干扰

- 蒸馏过程在线进行，学生模型生成 → 教师模型评分 → 策略更新

- 小米 MiMo-V2.5-Pro 采用此方案，与 DeepSeek、Kimi 的多教师蒸馏思路有共通之处

## 来源引用

- [摘要：4.3 小时写完一个编译器！小米凌晨开源 MiMo-V2.5，反超 DeepSeek V4](summaries/摘要：4.3 小时写完一个编译器！小米凌晨开源 MiMo-V2.5，反超 DeepSeek V4.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU3NTg5MjU1Mw%3D%3D&mid=2247497120&idx=1&sn=adb691fd7cb52fb63f3ab6f69fa5011b&chksm=fcc107b09a5c6e5f3ac7df70dcd88c86ac115110d41477790ef5d97e8fc7336b219c3d6bb535#rd)）
