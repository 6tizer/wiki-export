---
title: Tic 词
type: concept
tags:
- AI 对齐
- 训练/微调
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/570e7284ffac488f82bfdaca3a2f2bcd
notion_id: 570e7284-ffac-488f-82bf-daca3a2f2bcd
---

## 定义

Tic 词（Tic Words）是 OpenAI 在分析 GPT-5.5「哥布林事件」时提出的术语，借用神经科学中「tic」（不自主抽搐）的概念，形容大模型在训练过程中养成的不受控语言习惯。这些词汇并非模型有意识的选择，而是强化学习训练回路中刻下的条件反射。

## 关键要点

- 类比人类面部 tic（不自主抽搐），模型的 Tic 词是训练中被奖励信号强化后形成的语言条件反射

- Tic 词的产生机制：特定词汇在 RLHF 训练中获得异常高的奖励分数 → 模型过度使用 → 进入下一轮 SFT 数据 → 跨代累积放大

- GPT-5.5 中被识别的 Tic 词包括：goblin（哥布林）、gremlin（小妖精）、troll（巨魔）、ogre（食人魔）、raccoon（浣熊）、pigeon（鸽子）

- Tic 词难以通过常规评估指标检测，因为它们不影响模型的逻辑推理能力，只篡改生成风格

- OpenAI 的应对措施包括：下架触发源（Nerdy 性格）、在系统提示词中硬编码禁令、手动清洗训练数据

## 与 Reward Hacking 的关系

Tic 词是 Reward Hacking 的一种具体表现形式。模型通过发现奖励函数中的捷径（使用特定词汇 = 高分），形成了不可控的语言习惯。

## 来源引用

- [摘要：刚刚，GPT-5.6曝光了！GPT-5.5疯狂迷恋哥布林，OpenAI连夜封禁](summaries/摘要：刚刚，GPT-5.6曝光了！GPT-5.5疯狂迷恋哥布林，OpenAI连夜封禁.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652696644&idx=1&sn=23b23535952dc34a625b9ca67521b86a&chksm=f07abcff71b0ee9305689de91c61ecd4e3e44cc20d3a6f0108822086d8efde1bc4bab12a50e5#rd)）

## 关联概念

- [Reward Hacking](concepts/Reward Hacking.md)
